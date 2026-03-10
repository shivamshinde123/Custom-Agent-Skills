---
name: startup-analyzer
description: Comprehensive startup intelligence tool for job search strategy. Use this skill whenever the user wants to analyze a startup for job application purposes, understand a company's team, product, and opportunities. Trigger on queries like "analyze the company - [company name]", "research [company name]", "tell me about [startup]", or when the user needs complete company intelligence including team structure, product details, technical bottlenecks, and how their data science/AI expertise fits into the company's needs. Always use this skill for startup research during job search preparation.
---

# Startup Analyzer Skill

A comprehensive intelligence gathering and analysis tool designed to help you research startups strategically before applying for data science roles.

## What This Skill Does

When you provide a company name, this skill performs a multi-source web search to gather and synthesize information about:
- **Company Overview**: Mission, founding details, funding status, and growth metrics
- **Product & Features**: What they build, how it works, key differentiators
- **Team & Leadership**: Key people, their roles, backgrounds, and potential hiring contacts
- **Technical Stack & Bottlenecks**: Technologies they use, potential pain points, and gaps
- **Data Science Opportunities**: Where your specific expertise (LLMs, RAG, fine-tuning, bias mitigation, data platforms, etc.) could add value
- **Hiring Signals**: Whether they're actively hiring, job postings, and who to contact

## How to Use It

Trigger this skill by saying something like:
- "analyze the company - [company name]"
- "research [company name] for job opportunities"
- "I want a complete analysis of [startup name]"
- "give me intel on [company] - team, product, everything"

## Output Format

The skill generates a **detailed markdown report** with clearly organized sections, making it easy to:
- Review before submitting applications
- Identify key decision-makers to reach out to
- Understand where your skills align with company needs
- Prepare for interviews with company-specific insights

## How the Skill Works

1. **Multi-source Web Search**: Searches across LinkedIn, Crunchbase, TechCrunch, company websites, and other public sources
2. **Information Synthesis**: Gathers and organizes data about team, product, funding, and technology
3. **Opportunity Analysis**: Maps your resume skills (LLMs, RAG, fine-tuning, bias mitigation, data engineering, etc.) to company needs
4. **Gap Flagging**: Explicitly notes when information isn't publicly available rather than making assumptions

## Data Sources Used

- **Crunchbase**: Funding, investor info, company financials
- **LinkedIn**: Team members, company size, job postings
- **Company Website**: Official product info, mission, leadership
- **TechCrunch**: News, funding announcements, industry coverage
- **Other Public Sources**: GitHub repos, product reviews, technical blogs

## Important Notes

- The skill only compiles **publicly available information**
- If data gaps exist, the report will explicitly state "insufficient public information" rather than speculating
- Reports are designed specifically for job search strategy and data science role preparation
- Your background (LLMs, fine-tuning, RAG, bias mitigation, data platforms) is used to identify relevant opportunities