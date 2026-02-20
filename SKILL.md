---
name: User Story Generator
description: Transform requirements, meeting transcripts, or feature requests into structured user stories with acceptance criteria following INVEST principles.
---

# User Story Generator

> **Portable Prompt** - Works in Claude Web (claude.ai), Claude Code, or any Claude interface.
> Add this file as Project Knowledge in Claude Web, or use as custom instructions.

---

## How to Use

**Trigger phrases:**
- "Generate user stories"
- "I want to create user stories"
- "I need to create user stories"
- "Convert these requirements to user stories"

**Provide input via:**
- Conversation (describe features, problems, or paste text)
- Paste content from files (.txt, .doc, .vtt transcripts)
- Paste data from Excel/spreadsheets

**Choose output format:**
- **CSV** - Copy-paste into Excel or Google Sheets
- **Markdown table** - For documentation, Notion, GitHub
- **JSON** - Use with the Python script below to generate `.xlsx` files

---

## Purpose

Transform raw requirements, meeting transcripts, feature requests, or stakeholder conversations into actionable user stories that:
- Follow the standard "As a [user], I want [goal], so that [benefit]" format
- Include clear acceptance criteria using Given/When/Then patterns
- Meet INVEST criteria (Independent, Negotiable, Valuable, Estimable, Small, Testable)
- Are granular enough to complete in 1-3 days of development work

---

## Workflow

### Step 1: Gather Input

Collect requirements from:
- User conversation describing features or problems
- Pasted text from documents, transcripts, or meeting notes
- Pasted data from spreadsheets

Ask clarifying questions if:
- The input source is unclear
- A project key prefix is needed (e.g., "US-", "PROJ-")
- The user type or persona is ambiguous

### Step 2: Analyze for Pain Points

Examine input to identify pain points - problems, frustrations, inefficiencies, or unmet needs.

**Look for explicit indicators:**
| Signal Phrase | Example |
|---------------|---------|
| "It's frustrating when..." | "It's frustrating when I have to re-enter my information" |
| "I wish I could..." | "I wish I could export reports to PDF" |
| "It takes too long to..." | "It takes too long to find customer records" |
| "I can't..." | "I can't see my order history" |
| "There's no way to..." | "There's no way to bulk update items" |
| "I have to manually..." | "I have to manually calculate totals" |

**Look for implicit indicators:**
- Workarounds ("We use spreadsheets to track this")
- Multiple steps for simple tasks ("First I export, then...")
- Repeated tasks ("Every Monday I have to...")
- Error-prone processes ("Sometimes the data doesn't match")
- Missing information ("We don't know when...")

**Business pain indicators:**
- Revenue loss, time waste, compliance risk, customer complaints

Document each pain point before proceeding.

### Step 3: Extract Requirements

For each pain point, determine:
- What capability would solve this pain point?
- Who is the user experiencing this pain?
- What value does addressing this provide?

Transform pain points into requirement statements.

### Step 4: Deduplicate and Consolidate

Before generating stories, consolidate overlapping requirements:

**Identify duplicates:**
- Same feature, different wording ("export data" = "download feature")
- Subset relationships ("filter by date" is subset of "advanced filtering")
- Complementary requirements ("sort ascending" + "sort descending" = "sorting")

**Consolidation rules:**
1. Merge same-feature duplicates (keep most specific wording)
2. Combine subsets into broader story
3. Group related items under epics
4. Preserve distinctions when users or contexts differ

**Goal:** One user story per distinct user need.

### Step 5: Apply INVEST Criteria

Evaluate each story against INVEST (Bill Wake, 2003):

| Criterion | Check |
|-----------|-------|
| **I**ndependent | Can be developed and delivered separately |
| **N**egotiable | Details open to discussion; not a contract |
| **V**aluable | Delivers value to user or business |
| **E**stimable | Team can estimate the effort required |
| **S**mall | Completable in 1-3 days (fits in a sprint) |
| **T**estable | Has clear pass/fail acceptance criteria |

### Step 6: Split Large Stories

Stories too large (epics) must be split using **vertical slicing** - each slice delivers end-to-end functionality.

**Splitting patterns:**

1. **By workflow steps** - Break complex process into individual steps
2. **By business rules** - Separate different rules (discount types, etc.)
3. **By data variations** - Different input types (CSV, API, manual)
4. **By user type** - Different users need different views
5. **By CRUD** - Create, Read, Update, Delete as separate stories
6. **Simple/Complex** - Happy path first, then edge cases

**Vertical (correct):**
```
1. User can log in with email/password
2. User can log in with Google SSO
3. User can reset forgotten password
```

**Horizontal (avoid):**
```
1. Build login database schema
2. Create login API
3. Build login UI
```

### Step 7: Generate User Stories

Format each story:

**Summary:** Brief, action-oriented (5-10 words)

**Description:**
```
As a [type of user],
I want [goal/desire],
So that [benefit/value].
```

**Acceptance Criteria:** (2-4 per story)
```
Given [precondition]
When [action]
Then [expected result]
```

### Step 8: Output

Ask user for preferred format, then output:

**Option A - CSV (for Excel/Google Sheets):**
```csv
Key,Summary,Description,Acceptance Criteria
US-001,"Search customers by phone","As a support agent, I want to search customers by phone number, so that I can quickly find accounts during calls.","Given I am logged in as a support agent
When I enter a valid phone number
Then I see matching customer records"
```

**Option B - Markdown Table:**
| Key | Summary | Description | Acceptance Criteria |
|-----|---------|-------------|---------------------|
| US-001 | Search customers by phone | As a support agent... | Given... When... Then... |

**Option C - JSON (for Excel script):**
```json
[
  {
    "key": "US-001",
    "summary": "Search customers by phone",
    "description": "As a support agent, I want to search customers by phone number, so that I can quickly find accounts during calls.",
    "acceptance_criteria": "Given I am logged in as a support agent\nWhen I enter a valid phone number\nThen I see matching customer records"
  }
]
```

---

## Output Columns

| Column | Description |
|--------|-------------|
| Key | Unique identifier (e.g., US-001, US-002) |
| Summary | Brief one-line description (5-10 words) |
| Description | Full user story: "As a... I want... So that..." |
| Acceptance Criteria | Testable conditions in Given/When/Then format |

---

## Quality Checklist

Before delivering output, verify:
- [ ] Each story follows "As a... I want... So that..." format
- [ ] Acceptance criteria use Given/When/Then structure
- [ ] Stories are independent and can be developed in any order
- [ ] Stories are small enough for 1-3 days of work
- [ ] No duplicate or overlapping stories
- [ ] All identified pain points are addressed
- [ ] Keys are unique and follow consistent naming

---

## User Story Examples

**Example 1: Search Functionality**
```
Key: US-001
Summary: Search customers by phone number

As a customer support agent,
I want to search customer records by phone number,
So that I can quickly pull up account details during calls.

Acceptance Criteria:
1. Given I am logged in as a support agent
   When I enter a valid 10-digit phone number
   Then I see all customer records matching that phone number

2. Given I am logged in as a support agent
   When I enter a phone number with no matches
   Then I see "No customers found" with suggestions

3. Given I am logged in as a support agent
   When I enter a partial phone number (4+ digits)
   Then I see all records containing those digits
```

**Example 2: Notification**
```
Key: US-002
Summary: Email alerts for overdue tasks

As a project manager,
I want to receive email alerts when tasks become overdue,
So that I can take immediate action to keep projects on track.

Acceptance Criteria:
1. Given I have notifications enabled
   When a task I own becomes overdue
   Then I receive an email within 15 minutes

2. Given I have notifications disabled
   When a task becomes overdue
   Then I do not receive an email

3. Given a task is already overdue
   When 24 hours pass without completion
   Then I receive a follow-up reminder
```

---

## Pain Point to User Story Transformation

**Pain Point:** "Our sales team wastes 2 hours daily searching through emails to find customer information."

**Analysis:**
- Pain: Difficulty finding customer information
- User: Sales team members
- Goal: Centralized, searchable customer database
- Value: Save time, faster response to customers

**User Story:**
```
As a sales team member,
I want to search all customer interactions from a single dashboard,
So that I can quickly find relevant information without digging through emails.
```

---

## Common Mistakes to Avoid

**In User Stories:**
- Technical implementation ("I want a REST API endpoint...") instead of user goal
- Vague benefit ("so that things are better") instead of specific value
- Multiple features in one story - split them

**In Acceptance Criteria:**
- Not testable ("page loads quickly") - use specific metrics
- Technical details ("stored in PostgreSQL") - describe behavior
- Too vague ("search works correctly") - be specific

---

## Python Script for Excel Generation

Copy this script to generate formatted `.xlsx` files from JSON output:

```python
#!/usr/bin/env python3
"""
Generate Excel file from user story JSON data.

Usage:
    python generate_excel.py --output stories.xlsx --input stories.json
    python generate_excel.py --output stories.xlsx --data '[{"key": "US-001", ...}]'

Dependencies:
    pip install openpyxl
"""

import argparse
import json
import sys

try:
    from openpyxl import Workbook
    from openpyxl.styles import Font, Alignment, Border, Side, PatternFill
    from openpyxl.utils import get_column_letter
except ImportError:
    print("Error: openpyxl is required. Install with: pip install openpyxl")
    sys.exit(1)


def create_user_stories_excel(stories: list, output_path: str) -> str:
    """Create a formatted Excel file from user story data."""
    wb = Workbook()
    ws = wb.active
    ws.title = "User Stories"

    headers = ["Key", "Summary", "Description", "Acceptance Criteria"]

    # Styles
    header_font = Font(bold=True, size=12, color="FFFFFF")
    header_fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    header_alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    cell_alignment = Alignment(vertical="top", wrap_text=True)
    thin_border = Border(
        left=Side(style="thin"), right=Side(style="thin"),
        top=Side(style="thin"), bottom=Side(style="thin")
    )

    # Write headers
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col, value=header)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = header_alignment
        cell.border = thin_border

    # Write data
    for row_idx, story in enumerate(stories, 2):
        for col, key in enumerate(["key", "summary", "description", "acceptance_criteria"], 1):
            cell = ws.cell(row=row_idx, column=col, value=story.get(key, ""))
            cell.alignment = cell_alignment
            cell.border = thin_border

    # Column widths
    for col, width in {1: 12, 2: 40, 3: 50, 4: 60}.items():
        ws.column_dimensions[get_column_letter(col)].width = width

    ws.freeze_panes = "A2"
    wb.save(output_path)
    return output_path


def main():
    parser = argparse.ArgumentParser(description="Generate Excel from user story JSON")
    parser.add_argument("--output", "-o", required=True, help="Output Excel file path")
    parser.add_argument("--data", "-d", help="JSON string of user stories")
    parser.add_argument("--input", "-i", help="Path to JSON file")

    args = parser.parse_args()

    if args.input:
        with open(args.input, "r") as f:
            stories = json.load(f)
    elif args.data:
        stories = json.loads(args.data)
    else:
        stories = json.load(sys.stdin)

    if not isinstance(stories, list):
        print("Error: Data must be a JSON array")
        sys.exit(1)

    output_path = create_user_stories_excel(stories, args.output)
    print(f"Created: {output_path} ({len(stories)} stories)")


if __name__ == "__main__":
    main()
```

**To use:**
1. Save the JSON output from Claude to `stories.json`
2. Run: `pip install openpyxl`
3. Run: `python generate_excel.py --input stories.json --output user_stories.xlsx`

---

## Agile Best Practices Sources

This workflow is based on established Agile methodologies:

- **Bill Wake** - INVEST criteria (2003)
- **Mike Cohn** - "User Stories Applied" (2004)
- **Richard Lawrence** - Story splitting patterns (Humanizing Work)
- **Scrum Guide** - Schwaber & Sutherland
- **Agile Alliance** - Industry standards

---

## Quick Reference

**Story Template:**
```
As a [specific user type],
I want [one specific goal],
So that [clear business benefit].

Acceptance Criteria:
1. Given [context] When [action] Then [outcome]
2. Given [context] When [action] Then [outcome]
3. (edge case scenario)
```

**INVEST Checklist:**
- [ ] Independent - Can be delivered alone
- [ ] Negotiable - Open to discussion
- [ ] Valuable - Delivers user/business value
- [ ] Estimable - Team can size it
- [ ] Small - 1-3 days of work
- [ ] Testable - Has acceptance criteria

**Splitting Decision:**
1. Too big? → Split by workflow steps
2. Multiple rules? → Split by business rule variations
3. Multiple inputs? → Split by data variations
4. Multiple users? → Split by user type
5. CRUD operations? → Split by interface
6. Performance critical? → Split simple/complex
