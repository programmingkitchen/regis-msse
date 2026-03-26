# GitHub Copilot Models Guide

## Scope

This document summarizes the GitHub Copilot models currently documented by GitHub as of March 26, 2026. It explains:

- what each model is good at
- how model-related cost works in Copilot
- which plans typically include each model
- when to use each model and when to choose something else

Because GitHub changes model availability over time, treat this file as a snapshot rather than a permanent guarantee.

## How Cost Works In GitHub Copilot

GitHub Copilot cost has two separate parts:

1. The monthly Copilot subscription plan
2. Premium request usage for some models and features

### Monthly Plan Pricing

According to GitHub Docs, the Copilot plans are:

| Plan | Price | Included premium requests |
| --- | ---: | ---: |
| Free | $0/month | 50/month |
| Student | Free for verified students | 300/month |
| Pro | $10/month | 300/month |
| Pro+ | $39/month | 1500/month |
| Business | $19/user/month | 300/user/month |
| Enterprise | $39/user/month | 1000/user/month |

Additional premium requests can be purchased on eligible paid plans for $0.04 per request.

### What A Premium Request Means

In Copilot Chat, one prompt usually counts as one request multiplied by the model rate.

Examples:

- a `1x` model consumes 1 premium request per prompt
- a `0.33x` model consumes one-third of a premium request per prompt
- a `3x` model consumes 3 premium requests per prompt
- a `0x` model does not consume premium requests on paid plans where that model is available

### Effective Extra Cost If You Exceed Your Allowance

If your plan allows paid overages, the approximate extra cost per prompt is:

| Multiplier | Approximate overage cost per prompt |
| --- | ---: |
| `0x` | $0.00 |
| `0.25x` | $0.01 |
| `0.33x` | about $0.0132 |
| `1x` | $0.04 |
| `3x` | $0.12 |
| `30x` | $1.20 |

### Important Cost Notes

- On paid plans, `GPT-5 mini`, `GPT-4.1`, and `GPT-4o` are the included models that do not consume premium requests.
- Copilot Free is different: chat interactions count against the monthly premium request allowance.
- GitHub states that auto model selection in Copilot Chat on paid plans can apply a 10% multiplier discount.
- Model multipliers and plan availability can change.

## Quick Model Selection Tips

### Best Defaults

- Use `GPT-5 mini` for everyday coding, writing, and explanations.
- Use `GPT-5.4` when the task is hard, ambiguous, or spread across many files.
- Use `GPT-5.3-Codex` for agentic coding tasks, multi-step implementation, and codebase work.
- Use `Claude Haiku 4.5` or `Gemini 3 Flash` for quick, lightweight questions.
- Use `Claude Sonnet 4.6` for a balanced high-quality coding assistant.
- Use `Gemini 3.1 Pro` for long-context technical analysis and research-heavy work.

### When Not To Overpay For A Model

- Do not use `Claude Opus 4.6` or `Claude Opus 4.5` for simple syntax questions or small edits.
- Do not use `Claude Opus 4.6 (fast mode)` casually. Its `30x` multiplier makes it the most expensive option in this list.
- Do not use deep-reasoning models by default when a fast model can answer the question immediately.

## OpenAI Models

### GPT-4.1

| Detail | Information |
| --- | --- |
| Provider | OpenAI |
| Status | GA |
| Premium multiplier | `0x` on paid plans, `1x` on Free |
| Typical plan access | Free, Student, Pro, Pro+, Business, Enterprise |
| Best use | General-purpose coding and writing |

Use this when you want a stable, lower-cost general model for common chat and coding work.

Choose something else when the work needs deeper multi-step reasoning across a larger codebase.

### GPT-5 mini

| Detail | Information |
| --- | --- |
| Provider | OpenAI |
| Status | GA |
| Premium multiplier | `0x` on paid plans, `1x` on Free |
| Typical plan access | Free, Student, Pro, Pro+, Business, Enterprise |
| Best use | Default choice for coding, explanations, and writing |

This is the best everyday Copilot default for most users. It is fast, broadly capable, and inexpensive to run.

Use it for:

- everyday coding assistance
- documentation and summaries
- quick debugging
- small to medium code reviews

Choose something else when you need advanced architecture reasoning or specialized agentic behavior.

### GPT-5.1

| Detail | Information |
| --- | --- |
| Provider | OpenAI |
| Status | Closing down on 2026-04-01 |
| Premium multiplier | `1x` |
| Typical plan access | Student, Pro, Pro+, Business, Enterprise |
| Best use | Deep reasoning and debugging |

This model is still documented, but GitHub lists it as closing down soon. Prefer `GPT-5.4` or `GPT-5.3-Codex` for new work.

### GPT-5.1-Codex

| Detail | Information |
| --- | --- |
| Provider | OpenAI |
| Status | Closing down on 2026-04-01 |
| Premium multiplier | `1x` |
| Typical plan access | Student, Pro, Pro+, Business, Enterprise |
| Best use | Deep reasoning and debugging with Codex flavor |

Use only if you are already on a workflow that depends on it. For new work, move to `GPT-5.3-Codex`.

### GPT-5.1-Codex-Max

| Detail | Information |
| --- | --- |
| Provider | OpenAI |
| Status | Closing down on 2026-04-01 |
| Premium multiplier | `1x` |
| Typical plan access | Student, Pro, Pro+, Business, Enterprise |
| Best use | Agentic software development |

Historically aimed at agentic coding tasks. Prefer `GPT-5.3-Codex` now.

### GPT-5.1-Codex-Mini

| Detail | Information |
| --- | --- |
| Provider | OpenAI |
| Status | Closing down on 2026-04-01 |
| Premium multiplier | `0.33x` |
| Typical plan access | Student, Pro, Pro+, Business, Enterprise |
| Best use | Lower-cost Codex-style reasoning |

This is a cheaper transitional option, but it is also near retirement. Prefer `GPT-5.4 mini` or `GPT-5.3-Codex` depending on the task.

### GPT-5.2

| Detail | Information |
| --- | --- |
| Provider | OpenAI |
| Status | GA |
| Premium multiplier | `1x` |
| Typical plan access | Student, Pro, Pro+, Business, Enterprise |
| Best use | Deep reasoning and debugging |

Use this for difficult debugging, root-cause analysis, and more deliberate code understanding.

Choose `GPT-5 mini` if the task is routine and speed matters more than reasoning depth.

### GPT-5.2-Codex

| Detail | Information |
| --- | --- |
| Provider | OpenAI |
| Status | GA |
| Premium multiplier | `1x` |
| Typical plan access | Student, Pro, Pro+, Business, Enterprise |
| Best use | Agentic software development |

This is a strong option for implementation-oriented workflows that require tool use and multi-step editing.

### GPT-5.3-Codex

| Detail | Information |
| --- | --- |
| Provider | OpenAI |
| Status | GA |
| Premium multiplier | `1x` |
| Typical plan access | Student, Pro, Pro+, Business, Enterprise |
| Best use | Agentic software development and high-quality engineering work |

This is one of the strongest choices for feature work, tests, refactors, and code review when the task spans multiple steps.

Use it when you want:

- better code generation on non-trivial tasks
- agent-style workflows
- reliable handling of large change sets

### GPT-5.4

| Detail | Information |
| --- | --- |
| Provider | OpenAI |
| Status | GA |
| Premium multiplier | `1x` |
| Typical plan access | Pro, Pro+, Business, Enterprise |
| Best use | Deep reasoning, debugging, and technical decision-making |

Use this for the hardest reasoning-heavy tasks:

- architecture decisions
- subtle bug analysis
- multi-file refactoring plans
- trade-off analysis between designs

Do not use it by default for simple edits because `GPT-5 mini` is cheaper and faster.

### GPT-5.4 mini

| Detail | Information |
| --- | --- |
| Provider | OpenAI |
| Status | GA |
| Premium multiplier | `0.33x` |
| Typical plan access | Pro, Pro+, Business, Enterprise |
| Best use | Lightweight agentic work and codebase exploration |

GitHub specifically recommends it for codebase exploration and grep-style workflows. It is a good middle ground when you want more than a basic model but less cost than a full `1x` premium model.

## Anthropic Models

### Claude Haiku 4.5

| Detail | Information |
| --- | --- |
| Provider | Anthropic |
| Status | GA |
| Premium multiplier | `0.33x` on paid plans, `1x` on Free |
| Typical plan access | Free, Student, Pro, Pro+, Business, Enterprise |
| Best use | Fast help with simple or repetitive tasks |

Use this for quick syntax help, tiny utilities, lightweight code explanations, and rapid prototyping.

Do not use it for large-scale design or high-stakes debugging if a deeper model is available.

### Claude Opus 4.5

| Detail | Information |
| --- | --- |
| Provider | Anthropic |
| Status | GA |
| Premium multiplier | `3x` |
| Typical plan access | Pro, Pro+, Business, Enterprise |
| Best use | Complex reasoning and debugging |

This is a high-cost, high-capability model for complex engineering questions.

Use it when the prompt is difficult enough to justify the cost.

### Claude Opus 4.6

| Detail | Information |
| --- | --- |
| Provider | Anthropic |
| Status | GA |
| Premium multiplier | `3x` |
| Typical plan access | Pro, Pro+, Business, Enterprise |
| Best use | Anthropic's strongest deep-reasoning option in Copilot |

Use this for:

- difficult system design discussions
- advanced debugging
- multi-file interpretation where correctness matters more than cost

Avoid it for routine work because it burns premium requests quickly.

### Claude Opus 4.6 (fast mode) (preview)

| Detail | Information |
| --- | --- |
| Provider | Anthropic |
| Status | Public preview |
| Premium multiplier | `30x` |
| Typical plan access | Pro+ and Enterprise |
| Best use | Specialized high-end preview use only |

This is the most expensive model in the current GitHub Copilot list. Use it only when you have a strong reason to test the preview behavior and the result quality justifies the cost.

### Claude Sonnet 4

| Detail | Information |
| --- | --- |
| Provider | Anthropic |
| Status | GA |
| Premium multiplier | `1x` |
| Typical plan access | Pro, Pro+, Business, Enterprise |
| Best use | Balanced coding workflows |

This is a practical middle-tier model for coding, reasoning, and editing tasks.

### Claude Sonnet 4.5

| Detail | Information |
| --- | --- |
| Provider | Anthropic |
| Status | GA |
| Premium multiplier | `1x` |
| Typical plan access | Pro, Pro+, Business, Enterprise |
| Best use | General-purpose coding and agent tasks |

Use this when you want a balanced premium model that handles both implementation and reasoning well.

### Claude Sonnet 4.6

| Detail | Information |
| --- | --- |
| Provider | Anthropic |
| Status | GA |
| Premium multiplier | `1x` |
| Typical plan access | Pro, Pro+, Business, Enterprise |
| Best use | Balanced premium coding assistant with stronger reasoning than 4.5 |

This is one of the best premium all-around choices when you want better reasoning than the included models without jumping to a `3x` Opus model.

Use it for:

- serious debugging
- well-structured feature work
- medium to large refactors
- visually informed work where multimodal support matters

## Google Models

### Gemini 2.5 Pro

| Detail | Information |
| --- | --- |
| Provider | Google |
| Status | GA |
| Premium multiplier | `1x` |
| Typical plan access | Student, Pro, Pro+, Business, Enterprise |
| Best use | Deep reasoning and debugging |

Use this for complex code generation, debugging, and research-heavy technical questions.

### Gemini 3 Flash

| Detail | Information |
| --- | --- |
| Provider | Google |
| Status | Public preview |
| Premium multiplier | `0.33x` |
| Typical plan access | Student, Pro, Pro+, Business, Enterprise |
| Best use | Fast, lightweight help |

This is a low-cost premium model for quick responses when you still want access to the Gemini family.

### Gemini 3.1 Pro

| Detail | Information |
| --- | --- |
| Provider | Google |
| Status | Public preview |
| Premium multiplier | `1x` |
| Typical plan access | Student, Pro, Pro+, Business, Enterprise |
| Best use | Long-context reasoning and technical analysis |

GitHub recommends this for efficient edit-then-test loops and high tool precision. It is a strong choice for larger codebases and analytical tasks.

### Gemini 3 Pro

| Detail | Information |
| --- | --- |
| Provider | Google |
| Status | Retirement date listed as 2026-03-26 |
| Premium multiplier | `1x` |
| Typical plan access | Student, Pro, Pro+, Business, Enterprise |
| Best use | Deep reasoning and debugging |

GitHub still references this model in plan and client tables, but the retirement history points to `Gemini 3.1 Pro` as the replacement. For new work, prefer `Gemini 3.1 Pro`.

## xAI Model

### Grok Code Fast 1

| Detail | Information |
| --- | --- |
| Provider | xAI |
| Status | GA |
| Premium multiplier | `0.25x` on paid plans, `1x` on Free |
| Typical plan access | Free, Student, Pro, Pro+, Business, Enterprise |
| Best use | Fast general-purpose coding and writing |

This is a cost-efficient fast coding model. It is useful when you want something quick but do not want to spend a full `1x` premium request.

## Specialized And Fine-Tuned Models

### Raptor mini

| Detail | Information |
| --- | --- |
| Provider | Fine-tuned GPT-5 mini |
| Status | Public preview |
| Premium multiplier | `0x` on paid plans where available, `1x` on Free |
| Typical plan access | Free, Student, Pro, Pro+ |
| Best use | Fast inline suggestions and explanations |

GitHub describes this as specialized for fast, accurate inline suggestions and explanations. Use it when you want a quick assistant tuned for day-to-day coding flow.

### Goldeneye

| Detail | Information |
| --- | --- |
| Provider | Fine-tuned GPT-5.1-Codex |
| Status | Public preview |
| Premium multiplier | Not applicable on paid plans, `1x` on Free |
| Typical plan access | Free only |
| Best use | Complex reasoning in limited preview availability |

GitHub describes this as strong for complex problem-solving and sophisticated reasoning, but its availability is narrow. Use it only if your Copilot setup exposes it.

## Practical Advice By Task

### Use These For Everyday Work

- `GPT-5 mini`
- `GPT-4.1`
- `Grok Code Fast 1`
- `Claude Haiku 4.5`
- `Raptor mini`

These are the best value options for most daily tasks.

### Use These For Hard Debugging And Design Questions

- `GPT-5.4`
- `GPT-5.2`
- `Claude Sonnet 4.6`
- `Claude Opus 4.6`
- `Gemini 3.1 Pro`

These are better when the task spans many files, requires trade-off analysis, or involves ambiguous failures.

### Use These For Agentic Or Multi-Step Software Development

- `GPT-5.3-Codex`
- `GPT-5.2-Codex`
- `GPT-5.4 mini`
- `Claude Sonnet 4.5`
- `Claude Sonnet 4.6`

These are the best choices when Copilot needs to plan, edit, inspect, and iterate.

### Use These For Lowest Premium Cost

- `GPT-5 mini` on paid plans
- `GPT-4.1` on paid plans
- `Raptor mini` on paid plans where available
- `Grok Code Fast 1`
- `Claude Haiku 4.5`
- `Gemini 3 Flash`
- `GPT-5.4 mini`

## When Not To Choose By Model Name Alone

Do not assume the newest or most expensive model is always the best choice.

Model choice should depend on:

- task complexity
- response speed needs
- premium request budget
- whether your plan includes the model
- whether your client supports the model

In practice:

- start with `GPT-5 mini` for common work
- move to `GPT-5.4`, `Claude Sonnet 4.6`, or `Gemini 3.1 Pro` when reasoning quality matters more
- move to `GPT-5.3-Codex` for implementation-heavy, agentic tasks
- reserve `Claude Opus` models for difficult problems where their higher cost is justified

## Notes On Availability

- Some models are only available in specific Copilot clients or only on certain plans.
- Preview models can change quickly or disappear.
- GitHub lists `GPT-5.1` and its Codex variants as closing on April 1, 2026.
- GitHub lists `Gemini 3 Pro` with a retirement date of March 26, 2026, and recommends `Gemini 3.1 Pro` instead.

## Sources Used

- GitHub Docs: Supported AI models in GitHub Copilot
- GitHub Docs: AI model comparison
- GitHub Docs: Plans for GitHub Copilot
- GitHub Docs: Requests in GitHub Copilot