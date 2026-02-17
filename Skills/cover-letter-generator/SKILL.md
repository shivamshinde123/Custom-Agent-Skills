---
name: cover-letter-generator
description: Generate personalized, compelling cover letters by analyzing job descriptions and candidate resumes. Use this skill when the user needs to create a cover letter for a job application. The skill follows a 4-step process: (1) Pain Point Analysis - identifying role challenges, (2) Hook Generation - crafting an attention-grabbing opening, (3) Full Cover Letter Composition - creating a complete 250-word letter, and (4) Grammatical Refinement - polishing the final output.
---

# Cover Letter Generator

## Overview

This skill creates personalized, compelling cover letters that address specific job challenges and highlight the candidate's unique qualifications through a systematic 4-step workflow.

## Input Requirements

Before starting, gather:
1. **Job Description** - Must include:
   - Target company name
   - Target role/position title
   - Job responsibilities and requirements
2. **Candidate's Resume** - Complete resume with experience, skills, and achievements

## Workflow

### Step 1: Pain Point Analysis

Analyze the job description to understand the role's challenges:

1. **Identify day-to-day challenges** - What obstacles will someone in this role face?
2. **Extract root causes** - Why do these challenges exist?
3. **Synthesize insights** - Create a concise summary of professional obstacles

**Output**: A brief analysis (2-3 sentences) of the most significant challenges for this role.

### Step 2: Attention-Grabbing Hook Generation

Craft a compelling opening paragraph that demonstrates empathy and capability:

**Consider:**
- Candidate's current role and industry experience
- Target role and company
- Relevant past challenge resolution examples

**Requirements:**
- Maximum 100 words
- Demonstrates empathy with role challenges
- Highlights candidate's relevant experience
- Shows enthusiasm and capability
- Uses creative narrative techniques
- Incorporates specific examples from resume

**Output**: A hook paragraph (≤100 words) that serves as the cover letter opening.

### Step 3: Full Cover Letter Composition

Expand the hook into a complete cover letter:

**Structure:**
1. Use the generated hook as the opening paragraph
2. Expand to maximum 250 words total
3. Integrate information from candidate's resume
4. Demonstrate alignment between:
   - Candidate's background
   - Role requirements
   - Company's potential challenges
5. Highlight unique value proposition
6. Maintain professional yet personal tone

**Critical Constraints:**
- Maximum 250 words
- No hallucinated information
- All content must derive from provided resume and job description
- Professional language throughout

**Output**: Complete cover letter (≤250 words).

### Step 4: Grammatical and Style Refinement

Conduct comprehensive review and correction:

**Review for:**
- Spelling errors
- Grammatical mistakes
- Punctuation issues
- Capitalization inconsistencies
- Overall readability improvements

**Output Format:**
1. Polished final cover letter
2. Change tracking table showing:
   - Original text
   - Corrected text
   - Type of correction (spelling/grammar/punctuation/style)

## Final Deliverables

Present all outputs in this order:

1. **Pain Point Analysis Summary** - Brief insight into role challenges
2. **Hook Paragraph** - Opening paragraph (≤100 words)
3. **Complete Cover Letter** - Full letter (≤250 words)
4. **Change Tracking Table** - All modifications made during refinement

## Best Practices

- **Be specific**: Use concrete examples from the resume
- **Show empathy**: Demonstrate understanding of role challenges
- **Maintain authenticity**: Never fabricate experiences or skills
- **Focus on value**: Emphasize what the candidate brings to the role
- **Keep it concise**: Respect word limits strictly
- **Professional tone**: Balance professionalism with personality

## Example Usage Pattern

```
USER: I need a cover letter for a Senior Data Scientist role at TechCorp. 
Here's the job description: [paste] and my resume: [paste]

ASSISTANT: I'll create your cover letter following the 4-step process.

Step 1: Pain Point Analysis
[Analysis of role challenges...]

Step 2: Hook Generation
[Compelling opening paragraph...]

Step 3: Complete Cover Letter
[Full 250-word letter...]

Step 4: Refinement
[Polished version + change tracking table...]
```
