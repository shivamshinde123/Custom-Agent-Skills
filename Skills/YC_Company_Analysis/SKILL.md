---
name: yc-company-analyzer
description: Researches Y Combinator companies for job applications—company intelligence (funding, founders, product, bottlenecks), AI/ML job analysis (roles, skills, tech stack), and application strategy. Use when the user wants to analyze a YC company, research YC jobs, prepare for applications at workatastartup.com, or gather founder/funding/product/job details for a specific YC-backed startup.
---

# Y Combinator Company Analyzer

Systematic research workflow for YC companies when applying to jobs (especially AI/ML). Produces company intelligence, job analysis, and an application plan.

## When to Use

- User names a YC company and wants a full analysis before applying
- User asks about YC jobs in AI/ML, job details, or how to apply
- User wants founder backgrounds, funding, backers, product, or bottlenecks
- User is preparing applications on YC Work at a Startup

## Step-by-Step Research Workflow

### 1. Identify the Company

**Sources:**
- YC Work at a Startup: https://www.workatastartup.com/companies
- YC Directory: https://www.ycombinator.com/companies
- YC Demo Day: https://www.ycombinator.com/demo-day

**Capture:** Company name, website, YC batch (e.g. W24, S23), one-liner/mission.

### 2. Company Intelligence

**Company overview**
- Mission, vision, problem solved, target market
- Competitive landscape, unique value proposition

**Founders and team**
- Full names, education, previous companies, exits, notable roles
- Key technical hires, advisors/board
- Team size, structure, remote/hybrid/on-site

**Funding and backers**
- Total raised, rounds (Seed, Series A/B/C), dates
- Lead investors and notable backers (especially AI/ML VCs)
- Valuation if disclosed; revenue/ARR if available
- Runway or burn indicators if visible

**Product and how it works**
- Core product and main features
- Technical overview: architecture, integrations, user flow
- AI/ML components: models, frameworks (PyTorch/TensorFlow/etc.), infra
- Tech stack: languages, frontend, backend, DB, cloud, MLOps

**Product issues and bottlenecks**
- Known limitations, scaling or reliability challenges
- Technical debt or legacy systems mentioned in blogs/job posts
- Customer complaints or support themes (reviews, G2, Product Hunt)
- Regulatory or compliance constraints (e.g. for AI)

**Traction and metrics**
- Users, growth, revenue metrics
- Key customers/partners, press, awards
- Product status (beta, GA, scaling)

### 3. AI/ML Job Analysis

For each relevant AI/ML role:

**Job details**
- Title, level (Junior/Mid/Senior/Staff), team
- Location (remote/hybrid/on-site + city)
- Salary range and equity if stated
- Posting date and source (Work at a Startup, company site, etc.)

**Skills and requirements**
- Required: languages (Python, etc.), ML frameworks, domain (NLP/CV/LLMs/RL), cloud, tools
- Preferred: degree, industry experience, publications, domain knowledge
- Tech stack for the role: training/serving, data pipelines, MLOps, dev workflow

**Responsibilities**
- List primary responsibilities from the job description
- Note overlap with product bottlenecks or roadmap (for tailoring)

### 4. Best Way to Apply

**Choose primary channel:**
- **Direct:** Company careers page or YC Work at a Startup
- **Warm intro:** Mutual connection, alumni, YC network
- **Cold outreach:** Personalized email to founder/CTO/hiring manager
- **Recruiter:** YC talent partners, AI-focused recruiters

**Preparation**
- Tailor resume to job keywords and company tech stack
- Prepare 1–2 portfolio projects or papers relevant to their domain
- Draft company-specific cover letter / cold email (see [reference/application-templates.md](reference/application-templates.md))
- Update LinkedIn; ensure GitHub reflects relevant work

**Follow-up**
- Follow up once after 1–2 weeks with a short, value-add note
- Use multiple touchpoints only if appropriate (e.g. email + LinkedIn)

### 5. Risk and Fit (Red / Green Flags)

**Green flags:** Strong backers, clear traction, founder domain fit, technical leadership, recent funding or growth, positive reviews, public eng/blog culture.

**Red flags:** Short runway (<12 months), leadership churn, poor reviews, hype without metrics, high turnover, vague job description, regulatory risk for AI.

Summarize risk level (Low / Medium / High) and a brief verdict: Apply / Monitor / Skip.

### 6. Interview Preparation

- Company-specific ML/AI challenges and how the role might address them
- System design relevant to their product
- STAR stories: collaboration, ambiguity, technical leadership, learning
- Questions to ask: ML challenges, team structure, infra, success metrics, career path

## Output Format

Present analysis in this order:

1. **Company snapshot** — One-paragraph overview (what they do, stage, traction).
2. **Key metrics** — Funding, team size, batch, headquarters.
3. **Founders and backers** — Backgrounds, lead investors.
4. **Product analysis** — What they build, how it works, tech stack, **issues/bottlenecks**.
5. **AI/ML jobs** — Role(s), requirements, skills, tech stack, responsibilities.
6. **Application strategy** — Recommended channel, key talking points, materials to prepare.
7. **Red/green flags** — Short risk assessment and verdict.

Use the structured template for consistency: [reference/job-analysis-template.md](reference/job-analysis-template.md).

## Key Data Sources (Quick Reference)

| Source | Use for |
|--------|--------|
| workatastartup.com | Open roles, company snapshot |
| ycombinator.com/companies | Batch, one-liner, links |
| Crunchbase | Funding, investors, timeline |
| LinkedIn | Founders, team, backgrounds |
| Company site + blog | Product, tech, culture |
| GitHub | Tech stack, open source |
| Product Hunt | Launches, feedback |
| Glassdoor / Blind | Culture, reviews |

Full source list and workflow: [reference/yc-data-sources.md](reference/yc-data-sources.md).

## Research Tips

- Cross-check facts across at least 2–3 sources.
- Prefer recent data (blog, LinkedIn, news) for product and bottlenecks.
- Map job requirements to their stated challenges to tailor application.
- Note specific product features or posts to reference in cover letter or outreach.
