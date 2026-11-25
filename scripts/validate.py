"""Validate this distributable skill; no network or third-party dependencies."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills' / 'codex-gemini-collaboration'


def validate(root=ROOT):
    errors = []
    required = ['SKILL.md', 'agents/openai.yaml', 'references/prompts.md',
                'references/browser-handoff.md', 'references/records.md', 'references/sources.md']
    skill = root / 'skills' / 'codex-gemini-collaboration'
    for name in required:
        if not (skill / name).is_file():
            errors.append(f'Missing skill resource: {name}')
    if not (skill / 'SKILL.md').is_file():
        return errors
    text = (skill / 'SKILL.md').read_text(encoding='utf-8')
    front = re.match(r'\A---\n(.*?)\n---\n', text, re.S)
    if not front or not re.search(r'^name: codex-gemini-collaboration$', front[1], re.M):
        errors.append('Invalid skill identity/frontmatter')
    if not front or not re.search(r'^description: .+', front[1], re.M):
        errors.append('Missing skill description')
    for path in root.rglob('*.md'):
        if '.git' in path.parts:
            continue
        content = path.read_text(encoding='utf-8')
        if '[TODO' in content or '\ufffd' in content:
            errors.append(f'Unfinished scaffold or encoding problem: {path.relative_to(root)}')
        if re.search(r'(?i)(?<![a-z])[a-z]:[/\\]|/Users/|/home/[^/]+/', content):
            errors.append(f'Machine-specific path: {path.relative_to(root)}')
        for target in re.findall(r'\]\(([^)]+)\)', content):
            if '://' in target or target.startswith('#'):
                continue
            target = target.split('#', 1)[0]
            resolved = (path.parent / target).resolve()
            if not resolved.is_relative_to(root.resolve()) or not resolved.is_file():
                errors.append(f'Invalid local link: {path.relative_to(root)} -> {target}')
    return errors


if __name__ == '__main__':
    problems = validate()
    if problems:
        print('\n'.join(problems))
        sys.exit(1)
    print('PASS: skill identity, required files, UTF-8, local links, portability')
