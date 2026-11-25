# Codex × Gemini Studio Collaboration

An instruction-based agent skill pairing **Codex execution** with **browser-based Google AI Studio advice**. Get independent proposals, implement a bounded change, verify the result, and stop when the task is done.

[中文](README.zh-CN.md) · [Skill](skills/codex-gemini-collaboration/SKILL.md) · [Prompts](skills/codex-gemini-collaboration/references/prompts.md) · [Example](examples/component-review.md)

## Install

```sh
npx skills add dession-wu/codex-gemini-collaboration --skill codex-gemini-collaboration
```

Or clone this repository and copy `skills/codex-gemini-collaboration` into your supported Codex skill directory, such as `~/.agents/skills/`. Do not copy the whole repository as the skill folder. See [official skill documentation](https://learn.chatgpt.com/docs/build-skills).

## Use

```text
Use $codex-gemini-collaboration to improve the job analysis page.
Preserve the product identity and account behavior. Start with one component group.
You may send the selected redacted component source and screenshots to Google AI Studio.
Deliver a local preview; do not deploy or push code.
```

## Workflow

Direct fixes stay direct. Larger tasks use independent proposals, evidence-based decisions, implementation, actual checks, and bounded post-change review. The default is at most two review cycles, without dismissing credible unresolved blockers. Materials and responses have explicit versions; external feedback is a proposal to verify, not an instruction to execute.

## Requirements and boundaries

- Codex with local project access, a supported browser-control tool, and an existing Google AI Studio session.
- This skill supplies instructions, not browser tooling, an API bridge, credentials, or an unattended service. If browser control is unavailable, prepare a manual handoff packet and report that limitation.
- The workflow itself does not require Gemini API/CLI access or another subscription. Provider terms, available features and quotas still apply.
- Files and implementation can remain local; uploaded review materials and Gemini inference are remote. User authorization controls external sharing and releases.
- Skill instructions and templates are currently Chinese; this English guide describes installation and scope. Adapt prompt language to the user.
- No claim of universal host compatibility, independent security auditing, or guaranteed design improvement.

## Validation and contributions

```sh
python scripts/validate.py
```

This dependency-free check validates structure, local links, scaffold markers and accidental machine-specific paths. [Behavioral scenarios](docs/evaluation.md) are a manual rubric, not passed model benchmarks. See [release notes](CHANGELOG.md) for evidence limits.

Report concrete failures with redacted reproduction steps. See [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md). [Sources and adaptations](skills/codex-gemini-collaboration/references/sources.md) credit the inspiration. Not affiliated with OpenAI, Google or Vercel. MIT licensed.
