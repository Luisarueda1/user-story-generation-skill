---
name: user-story-generation
description: Transform raw requirements, meeting transcripts, feature requests, or stakeholder conversations into actionable Agile user stories. Use when the user asks to "generate user stories", "convert requirements to user stories", "create user stories from", "transform transcript into stories", or similar phrases. Also use when the user provides requirements documents or meeting notes and explicitly mentions user stories or backlog creation.
---

# User Story Generation Skill

Transform raw requirements into actionable, INVEST-compliant user stories ready for sprint planning.

## Core Process

### Step 1: Analyze Input

Read and understand the provided content:
- Meeting transcripts or notes
- Feature requests or requirements documents
- Stakeholder conversations
- Product vision statements

### Step 2: Identify Pain Points

Extract both explicit and implicit pain points:
- **Explicit**: Directly stated problems in the text
- **Implicit**: Inferred needs (e.g., request for automation implies manual process is tedious)

Consult `references/invest_and_splitting.md` for pain point analysis techniques.

### Step 3: Generate User Stories

Create stories using the format:
```
As a [type of user],
I want [goal/desire],
given [context/constraints],
so that [benefit/value].
```

**Requirements:**
- Each story must have a clear pain point it addresses
- Stories must be Independent, Negotiable, Valuable, Estimable, Small, and Testable (INVEST)
- Keep stories small enough to complete in 1-3 days
- Stories should be vertically sliced (not technical layers)

**Acceptance Criteria:**
For each story, generate 2-4 testable acceptance criteria using Given/When/Then format:
```
- Given [initial context], when [action occurs], then [expected outcome]
- Given [initial context], when [action occurs], then [expected outcome]
```

Acceptance criteria should:
- Be specific and testable
- Cover the main success scenarios
- Include edge cases where relevant
- Be clear enough for QA to validate

Consult `references/invest_and_splitting.md` for INVEST criteria details and story-splitting techniques when stories are too large.

### Step 4: Organize Stories

Group related stories into logical categories/epics:
- By feature area (e.g., "User Authentication", "Payment Processing")
- By user journey (e.g., "Onboarding", "Checkout Flow")
- By system component (e.g., "Admin Dashboard", "Mobile App")

### Step 5: Ask for Output Format

Always ask the user which output format they prefer:
- **CSV**: Best for importing to Excel/Google Sheets
- **Markdown Table**: Best for documentation, Notion, GitHub
- **JSON**: Best for programmatic processing or API integration
- **Excel (.xlsx)**: Best for formatted spreadsheets with styling

Do NOT assume a format - always ask first.

### Step 6: Generate Output

#### Required Columns

Every story must include these seven fields:
1. **category_epic**: High-level grouping for related stories
2. **title**: Brief summary (5-10 words)
3. **user_story**: Complete story in "As a... I want... given... so that..." format
4. **acceptance_criteria**: 2-4 testable criteria in Given/When/Then format (bullet points)
5. **requirement**: Original requirement or feature description from input
6. **pain_point**: The specific problem this story solves
7. **created_date**: Today's date in YYYY-MM-DD format

#### CSV Format
```csv
Category/Epic,Title,User Story,Acceptance Criteria,Requirement,Pain Point,Created Date
User Authentication,Login with Email,"As a returning user, I want to log in with my email and password, given I have an existing account, so that I can access my personalized content","- Given valid credentials, when I submit the login form, then I am redirected to my dashboard
- Given invalid credentials, when I submit the login form, then I see an error message
- Given I am already logged in, when I navigate to the login page, then I am redirected to my dashboard","Users need to access their accounts","Users cannot access their saved preferences",2026-01-29
```

#### Markdown Table Format
```markdown
| Category/Epic | Title | User Story | Acceptance Criteria | Requirement | Pain Point | Created Date |
|---------------|-------|------------|---------------------|-------------|------------|--------------|
| User Authentication | Login with Email | As a returning user... | - Given valid credentials, when I submit the login form, then I am redirected to my dashboard<br>- Given invalid credentials, when I submit the login form, then I see an error message | Users need to... | Users cannot... | 2026-01-29 |
```

#### JSON Format
```json
[
  {
    "category_epic": "User Authentication",
    "title": "Login with Email",
    "user_story": "As a returning user, I want to log in with my email and password, given I have an existing account, so that I can access my personalized content",
    "acceptance_criteria": "- Given valid credentials, when I submit the login form, then I am redirected to my dashboard\n- Given invalid credentials, when I submit the login form, then I see an error message\n- Given I am already logged in, when I navigate to the login page, then I am redirected to my dashboard",
    "requirement": "Users need to access their accounts",
    "pain_point": "Users cannot access their saved preferences",
    "created_date": "2026-01-29"
  }
]
```

#### Excel Format

For Excel output:
1. Generate the JSON format first
2. Save JSON to a temporary file (e.g., `/home/claude/stories.json`)
3. Run the Excel generation script with today's date in filename:
   ```bash
   cd /home/claude/user-story-generation/scripts
   python3 generate_excel.py --input /home/claude/stories.json --output /home/claude/$(date +%Y-%m-%d)_userstories.xlsx
   ```
4. Move the generated file to outputs:
   ```bash
   mv /home/claude/*_userstories.xlsx /mnt/user-data/outputs/
   ```
5. Present the Excel file to the user

The script automatically applies formatting:
- Colored header row (blue background, white text)
- Frozen header for scrolling
- Wrapped text for readability
- Optimized column widths
- Professional borders
- Seven columns: Category/Epic, Title, User Story, Acceptance Criteria, Requirement, Pain Point, Created Date

## Quality Guidelines

**Story Title:**
- Keep to 5-10 words
- Descriptive and actionable
- Avoid technical jargon

**User Story:**
- Always use full "As a... I want... given... so that..." format
- Be specific about user type (admin, customer, guest, etc.)
- Include meaningful context in "given" clause
- Articulate clear value in "so that" clause

**Acceptance Criteria:**
- Write 2-4 criteria per story in Given/When/Then format
- Each criterion should be independently testable
- Cover main success path and key edge cases
- Be specific about expected outcomes
- Use bullet points for readability
- Example format: "- Given [context], when [action], then [outcome]"

**Requirement:**
- Extract the original requirement from input text
- Keep concise but informative
- Preserve key details from original source

**Pain Point:**
- State the specific problem being solved
- Connect to user or business value
- One clear pain point per story

## Common Patterns

**Authentication Stories:**
- Category: "User Authentication" or "Security"
- Pain points: Access control, security concerns, user experience

**Data Management Stories:**
- Category: "Data Management" or "[Entity] Management"
- Pain points: Manual processes, data accuracy, efficiency

**Reporting/Analytics Stories:**
- Category: "Reporting" or "Analytics"
- Pain points: Lack of visibility, manual reporting, decision-making delays

**Integration Stories:**
- Category: "Integrations" or "Third-Party Services"
- Pain points: Manual data transfer, system disconnects, workflow inefficiency

## Resources

- **INVEST Criteria & Story Splitting**: `references/invest_and_splitting.md`
- **Excel Generation Script**: `scripts/generate_excel.py`

Load the INVEST reference when you need guidance on:
- Validating story quality
- Splitting large stories
- Understanding pain point analysis
