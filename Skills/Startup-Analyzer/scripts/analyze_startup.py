#!/usr/bin/env python3
"""
Startup Company Analyzer - Main Analysis Script
Performs comprehensive web-based research on startups and generates detailed reports
"""

import json
import sys
from datetime import datetime

# This script will be called with a company name and will:
# 1. Perform multi-source web searches (via Claude's web_search capability)
# 2. Gather information about team, product, funding, technical stack
# 3. Analyze where the user's skills fit
# 4. Generate a formatted markdown report

# The actual web searches will be performed by Claude using the web_search tool
# This script serves as a template and reminder of what queries to execute

SEARCH_QUERIES_TEMPLATE = {
    "company_overview": [
        "{company_name} company overview founding mission",
        "{company_name} funding rounds investors",
        "{company_name} company size headquarters"
    ],
    "product_and_features": [
        "{company_name} product features what does it do",
        "{company_name} technology stack how it works",
        "{company_name} competitors differentiation"
    ],
    "team_and_leadership": [
        "{company_name} founders team leadership LinkedIn",
        "{company_name} CEO CTO engineering leadership",
        "{company_name} data science team AI engineers"
    ],
    "hiring_and_roles": [
        "{company_name} hiring data science jobs",
        "{company_name} job openings careers",
        "{company_name} engineering team size growth"
    ],
    "technical_challenges": [
        "{company_name} technical challenges bottlenecks",
        "{company_name} machine learning data engineering",
        "{company_name} AI LLM implementation"
    ]
}

REPORT_TEMPLATE = """# {company_name} - Comprehensive Company Analysis

**Report Generated**: {date}

---

## 1. Company Overview

### Founding & Mission
{company_overview}

### Funding & Growth
{funding_info}

### Company Size & Structure
{company_size}

---

## 2. Product & Technology

### What They Build
{product_description}

### Key Features & Functionality
{product_features}

### Technical Architecture
{technical_stack}

### Competitive Positioning
{competitive_advantage}

---

## 3. Team & Leadership

### Founders & Leadership
{leadership_team}

### Key Personnel
{key_personnel}

### Organizational Structure
{team_structure}

### Potential Hiring Contacts
{hiring_contacts}

---

## 4. Technical Stack & Infrastructure

### Core Technologies Used
{tech_stack}

### Data & AI Infrastructure
{data_infrastructure}

### Development Tools & Practices
{dev_practices}

---

## 5. Identified Bottlenecks & Challenges

### Technical Pain Points
{technical_bottlenecks}

### Data & ML Challenges
{ml_challenges}

### Scaling Issues
{scaling_challenges}

---

## 6. Data Science Opportunities - Where You Can Help

### Your Relevant Skills
Based on your background in:
- Large Language Models (LLMs) and fine-tuning
- Retrieval Augmented Generation (RAG) systems
- Model bias mitigation and fairness
- Data platform architecture
- Multi-agent AI systems

### Opportunities for Impact
{opportunities}

### Specific Problem Areas
{problem_areas}

---

## 7. Key Takeaways & Action Items

### Hiring Status
{hiring_status}

### Next Steps for Your Application
{next_steps}

### Key People to Connect With
{key_contacts}

---

**Data Sources**: Crunchbase, LinkedIn, TechCrunch, Company Website, GitHub, Industry News

**Note on Information**: This report contains only publicly available information. Where data gaps exist, they are explicitly noted rather than assumed.
"""

def generate_report_template(company_name):
    """Generate a markdown report template with the company name"""
    report = REPORT_TEMPLATE.format(
        company_name=company_name,
        date=datetime.now().strftime("%B %d, %Y"),
        company_overview="[Information gathered from web search]",
        funding_info="[Information gathered from web search]",
        company_size="[Information gathered from web search]",
        product_description="[Information gathered from web search]",
        product_features="[Information gathered from web search]",
        technical_stack="[Information gathered from web search]",
        competitive_advantage="[Information gathered from web search]",
        leadership_team="[Information gathered from web search]",
        key_personnel="[Information gathered from web search]",
        team_structure="[Information gathered from web search]",
        hiring_contacts="[Information gathered from web search]",
        tech_stack="[Information gathered from web search]",
        data_infrastructure="[Information gathered from web search]",
        dev_practices="[Information gathered from web search]",
        technical_bottlenecks="[Information gathered from web search]",
        ml_challenges="[Information gathered from web search]",
        scaling_challenges="[Information gathered from web search]",
        opportunities="[Information gathered from web search]",
        problem_areas="[Information gathered from web search]",
        hiring_status="[Information gathered from web search]",
        next_steps="[Information gathered from web search]",
        key_contacts="[Information gathered from web search]"
    )
    return report

if __name__ == "__main__":
    if len(sys.argv) > 1:
        company_name = sys.argv[1]
        print(f"Generating analysis for {company_name}...")
        print(json.dumps(SEARCH_QUERIES_TEMPLATE, indent=2))
    else:
        print("Usage: python analyze_startup.py <company_name>")