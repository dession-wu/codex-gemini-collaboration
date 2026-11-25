# Codex 与 Gemini Studio 协作

面向Codex＋网页版Google AI Studio的协作技能。Codex负责本地核实、实施与验收，Gemini提供独立方案和视觉、文案、交互建议。

[English](README.md) · [技能正文](skills/codex-gemini-collaboration/SKILL.md) · [五组Prompt](skills/codex-gemini-collaboration/references/prompts.md)

## 安装与调用

```sh
npx skills add dession-wu/codex-gemini-collaboration --skill codex-gemini-collaboration
```

也可下载仓库，将skills中的codex-gemini-collaboration文件夹复制到当前Codex支持的技能目录，例如 ~/.agents/skills/。

> 使用 $codex-gemini-collaboration 优化岗位分析页。保留风格和账号行为，先做一个组件组。允许将本轮必要的脱敏组件源码和截图发送到Google AI Studio。只交付本地预览，不部署、不推送。

## 能做什么

小改直接做；大方案双方先独立提案；组件打磨先保留有效设计，再做少量可定位改进；最后用真实截图和实际检查复核。默认最多两轮，无阻断后收敛。记录材料版本和提交状态，支持中断恢复。

## 需要什么

可用的Codex浏览器控制工具和已登录AI Studio。技能不自带浏览器、不申请API、不绕过登录、不保证无限额度或后台运行。没有浏览器时准备手动交接包并说明缺口。上传材料会离开本机，外发和发布以用户授权为准。

运行 `python scripts/validate.py` 可检查结构。格式通过不代表设计有效，场景表不是模型基准测试。合成示例见examples，验证边界见CHANGELOG。欢迎通过Issue提供脱敏复现。MIT许可证；参考文章仅借鉴分工原则，不照搬作者脚本或权限规则。与OpenAI、Google、Vercel无隶属关系。
