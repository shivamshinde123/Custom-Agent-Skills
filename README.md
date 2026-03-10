# Custom Agent Skills

A collection of **agent skills** that extend AI assistants (e.g. Claude, Cursor) with specialized workflows, domain knowledge, and tool integrations. Each skill is a self-contained package with instructions and optional references, scripts, and templates.

## What’s in this repo

| Location | Skill | Description |
|----------|--------|-------------|
| `Skills/YC_Company_Analysis/` | **YC Company Analyzer** | Researches Y Combinator companies for job applications: company intelligence (funding, founders, product, bottlenecks), AI/ML job analysis (roles, skills, tech stack), and application strategy. Use when analyzing a YC company, researching YC jobs, or preparing for [Work at a Startup](https://www.workatastartup.com). |
| `Skills/Startup-Analyzer/` | **Startup Analyzer** | Comprehensive startup intelligence for job search strategy: product, team, funding, tech stack, bottlenecks, hiring signals, and where your DS/AI background fits. Use when you want a full “research this company before I apply” report (not limited to YC). |
| `Skills/cover-letter-generator/` | **Cover Letter Generator** | Generates personalized cover letters from a job description and resume using a 4-step workflow: pain point analysis, hook generation, full letter composition (≤250 words), and grammatical/style refinement (with a change tracking table). |
| `Skills/skill-creator/` | **Skill Creator** | Guidance for creating or updating skills: how to structure `SKILL.md`, what to put in `references/`, `scripts/`, and `assets/`, and how to keep skills concise and effective. |
| `Skills/AI-Startup-Radar/` | **AI Startup Radar** *(no `SKILL.md` yet)* | Folder present under `Skills/`, but no `SKILL.md`/docs found yet. Add `SKILL.md` to describe what it does and when it should trigger. |
| `Skills/LinkedIn-Message-Generator/` | **LinkedIn Message Generator** *(no `SKILL.md` yet)* | Folder present under `Skills/`, but no `SKILL.md`/docs found yet. Add `SKILL.md` to describe what it does and when it should trigger. |

## Skill structure

Each skill lives in its own folder and includes:

- **`SKILL.md`** (required) — YAML frontmatter (`name`, `description`) plus markdown instructions for when and how to use the skill.
- **`reference/`** (optional) — Docs, templates, and checklists the skill can reference (e.g. job-analysis templates, application templates, data sources).
- **`scripts/`** (optional) — Executable helpers for repeatable or fragile steps.

Skills are intended to be loaded by your agent/runtime when relevant to the user’s request (e.g. by name or description).

## Using skills

- **YC Company Analyzer**: Ask the agent to analyze a specific YC company, research AI/ML roles at YC startups, or prepare for applications on Work at a Startup. The skill walks through company intelligence, job analysis, and application strategy.
- **Startup Analyzer**: Ask the agent to research any startup/company for job opportunities and produce a detailed markdown report (team, product, funding, stack, bottlenecks, hiring signals, and fit).
- **Cover Letter Generator**: Provide the job description and your resume; the agent will produce pain point analysis, a hook, a complete cover letter (≤250 words), and a change tracking table.
- **Skill Creator**: Ask the agent to create a new skill or improve an existing one; it provides best practices for skill metadata, structure, and bundled resources.
- **AI Startup Radar**: Add `SKILL.md` under `Skills/AI-Startup-Radar/` to enable this skill to trigger and document how it should be used.
- **LinkedIn Message Generator**: Add `SKILL.md` under `Skills/LinkedIn-Message-Generator/` to enable this skill to trigger and document how it should be used.

## Adding a new skill

1. Add a new folder under `Skills/` (e.g. `Skills/MySkill/`).
2. Create `SKILL.md` with frontmatter and clear instructions (see `Skills/YC_Company_Analysis/SKILL.md` and its references for the expected format and structure).
3. Optionally add `reference/`, `scripts/`, or other assets.
4. Register or configure the skill in your agent environment so it can be selected when relevant.

## License

Per-skill. See each skill’s folder for any `LICENSE` or terms.
