# Custom Agent Skills

A collection of **agent skills** that extend AI assistants (e.g. Claude, Cursor) with specialized workflows, domain knowledge, and tool integrations. Each skill is a self-contained package with instructions and optional references, scripts, and templates.

## What’s in this repo

| Location | Skill | Description |
|----------|--------|-------------|
| `Skills/YC_Company_Analysis/` | **YC Company Analyzer** | Researches Y Combinator companies for job applications: company intelligence (funding, founders, product, bottlenecks), AI/ML job analysis (roles, skills, tech stack), and application strategy. Use when analyzing a YC company, researching YC jobs, or preparing for [Work at a Startup](https://www.workatastartup.com). |

## Skill structure

Each skill lives in its own folder and includes:

- **`SKILL.md`** (required) — YAML frontmatter (`name`, `description`) plus markdown instructions for when and how to use the skill.
- **`reference/`** (optional) — Docs, templates, and checklists the skill can reference (e.g. job-analysis templates, application templates, data sources).
- **`scripts/`** (optional) — Executable helpers for repeatable or fragile steps.

Skills are intended to be loaded by your agent/runtime when relevant to the user’s request (e.g. by name or description).

## Using skills

- **YC Company Analyzer**: Ask the agent to analyze a specific YC company, research AI/ML roles at YC startups, or prepare for applications on Work at a Startup. The skill walks through company intelligence, job analysis, and application strategy.

## Adding a new skill

1. Add a new folder under `Skills/` (e.g. `Skills/MySkill/`).
2. Create `SKILL.md` with frontmatter and clear instructions (see `Skills/YC_Company_Analysis/SKILL.md` and its references for the expected format and structure).
3. Optionally add `reference/`, `scripts/`, or other assets.
4. Register or configure the skill in your agent environment so it can be selected when relevant.

## License

Per-skill. See each skill’s folder for any `LICENSE` or terms.
