# Startup Analyzer Skill - Documentation

## Overview

The **Startup Analyzer** skill is a comprehensive intelligence-gathering tool designed specifically for your data science job search. It performs multi-source web research on startups and generates detailed markdown reports analyzing their team, product, technical stack, and where your specific skills (LLMs, RAG, bias mitigation, data platforms, etc.) can add value.

## Skill Structure

```
startup-analyzer/
├── SKILL.md                      # Main skill definition (triggers, capabilities)
├── scripts/
│   └── analyze_startup.py       # Analysis script template
├── test_cases.json              # Test prompts for skill triggering
└── SAMPLE_REPORT_Anthropic.md   # Example output report
```

## How to Use the Skill

### Trigger Phrases
The skill triggers on queries like:
- "analyze the company - [company name]"
- "research [company name] for job opportunities"
- "I want a complete analysis of [startup name]"
- "give me intel on [company] - team, product, everything"

### Example Usage
```
User: "analyze the company - Databricks"
Claude: [Activates skill, performs web searches, generates comprehensive report]
```

## What the Skill Does

1. **Multi-Source Web Search**
   - Searches LinkedIn, Crunchbase, TechCrunch, company websites
   - Gathers public information about funding, team, product

2. **Information Organization**
   - Company overview & founding story
   - Funding rounds and investors
   - Product features and technical architecture
   - Team structure and leadership
   - Technical stack and infrastructure

3. **Opportunity Analysis**
   - Maps your resume skills to company needs
   - Identifies bottlenecks where you can add value
   - Suggests where your LLM, RAG, and bias mitigation expertise fits

4. **Actionable Intelligence**
   - Hiring status and signals
   - Key contacts and decision-makers
   - Next steps for application
   - Specific problem areas you could tackle

5. **Explicit Gap Flagging**
   - Notes where public information is insufficient
   - Avoids speculation and unfounded assumptions
   - Marks incomplete sections clearly

## Report Structure

Each report includes:

### 1. Company Overview
- Founding & mission
- Funding & growth metrics
- Company size & structure

### 2. Product & Technology
- What they build
- Key features & functionality
- Technical architecture
- Competitive positioning

### 3. Team & Leadership
- Founders & CEO/CTO
- Key personnel
- Organizational structure
- Potential hiring contacts

### 4. Technical Stack & Infrastructure
- Core technologies
- Data & AI infrastructure
- Development practices

### 5. Bottlenecks & Challenges
- Technical pain points
- Data & ML challenges
- Scaling issues

### 6. **YOUR OPPORTUNITIES** (Custom to Your Skills)
- Your relevant background
- Specific ways you can help
- Problem areas where your expertise applies
- Based on your:
  - LLM fine-tuning & prompt engineering
  - RAG system design
  - Bias mitigation & fairness
  - Data platform architecture
  - Multi-agent AI systems
  - Data visualization & dashboarding

### 7. Action Items
- Hiring status
- Next steps for application
- Key people to connect with
- How to approach them

## Your Resume Context

The skill uses your background from your resume:

**Key Technical Skills**:
- Large Language Models (fine-tuning, prompt engineering)
- Retrieval Augmented Generation (RAG) with MongoDB
- Bias mitigation (SEAT, self-debiasing techniques)
- Multi-agent AI systems (LangChain, GPT-4)
- Data platforms & optimization
- Python, PyTorch, TensorFlow
- Data visualization (Tableau, Power BI)

**Relevant Project Experience**:
- Built LLM-based recommendation system for SWAP platform
- Reduced BERT model bias by quantifying with SEAT
- Implemented RAG with MongoDB for improved context
- Automated research workflows with LLMs
- Created comprehensive dashboards and analytics systems

## Example Output

See `SAMPLE_REPORT_Anthropic.md` for a complete example analysis showing:
- How the skill identifies company details
- How opportunities are customized to your skills
- How specific problem areas are mapped to your experience
- Professional formatting ready for reference during job search

## Test Cases

The skill has been validated against the following test prompts:

| Query | Should Trigger | Status |
|-------|----------------|--------|
| "analyze the company - Anthropic" | Yes | ✓ Explicit trigger phrase |
| "research Hugging Face for job opportunities" | Yes | ✓ Job search context |
| "I want a complete analysis of OpenAI - team, product, everything" | Yes | ✓ Explicit comprehensive request |
| "Tell me about Retool - their team structure, product features, and where I could help with my data science background" | Yes | ✓ Fit analysis request |
| "What is Python?" | No | ✓ Not company research |
| "How do I write a cover letter?" | No | ✓ General career advice |

## How the Skill Performs Research

When you trigger the skill, Claude:

1. **Performs Web Searches** on:
   - Company overview and mission
   - Funding rounds and investors
   - Product features and technology
   - Team members and leadership
   - Job openings and hiring signals
   - Technical architecture and challenges

2. **Synthesizes Information** from:
   - Official company websites
   - LinkedIn company pages
   - Crunchbase funding data
   - TechCrunch news coverage
   - Industry publications
   - GitHub repositories (if applicable)

3. **Generates a Markdown Report** with:
   - Well-organized sections
   - Cited information sources
   - Explicit data gaps noted
   - Your personalized opportunity analysis

4. **Returns Output** as a formatted markdown document you can:
   - Save for future reference
   - Print or PDF for interview prep
   - Share with mentors or advisors
   - Use to prepare tailored applications

## Important Notes

- **Public Data Only**: The skill only uses publicly available information
- **No Speculation**: Information gaps are noted explicitly, not filled with assumptions
- **Your Background**: Analysis is customized using your resume and experience
- **Job Search Focused**: All insights are framed for job application strategy
- **Personalized**: Highlights opportunities specific to your technical skills

## Next Steps

Once the skill is finalized, you can:

1. **Analyze Target Companies** by saying: "analyze the company - [name]"
2. **Build a Company Database** - Run analyses on your target companies
3. **Prepare for Applications** - Use insights to customize your resume and cover letter
4. **Identify Contacts** - Know who to reach out to and how to approach them
5. **Understand Fit** - Clearly articulate your value based on company's real challenges

## Example Use Cases

- **Researching Crunchbase-funded AI startups** before applying for data science roles
- **Understanding technical bottlenecks** at potential employers to tailor your pitch
- **Identifying decision-makers** to reach out to for informational interviews
- **Preparing company-specific answers** for interviews
- **Building your target company list** with detailed intelligence
- **Understanding market positioning** of startups in your field

---

**Skill Version**: 1.0  
**Created**: February 25, 2026  
**Last Updated**: February 25, 2026