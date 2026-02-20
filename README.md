# User Story Generation Skill

**Transform requirements, meeting transcripts, and feature requests into sprint-ready user stories with acceptance criteria.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Works with Claude](https://img.shields.io/badge/Works%20with-Claude-orange)](https://claude.ai)
[![Python 3.x](https://img.shields.io/badge/Python-3.x-green)](scripts/generate_excel.py)

---

## What It Does

This is a **portable Claude AI skill** that follows an 8-step Agile workflow to:

1. Analyze input for explicit and implicit pain points
2. Extract and deduplicate requirements
3. Apply INVEST criteria (Independent, Negotiable, Valuable, Estimable, Small, Testable)
4. Split large stories using vertical slicing
5. Generate stories in `As a... I want... So that...` format with `Given/When/Then` acceptance criteria
6. Deliver output in your preferred format

**Works anywhere Claude is available** — Claude Web, Claude Code, or any Claude interface.

---

## Quick Start

### Option A — Claude Settings › Skills (Recommended)

1. Download `user-story-generation-v2.skill` from [Releases](../../releases/latest)
2. Open [Claude.ai](https://claude.ai) → click your avatar → **Settings**
3. Go to **Capabilities** (or **Skills**)
4. Click **Add skill** and upload the `.skill` file
5. Start a conversation and say one of the trigger phrases below

### Option B — Claude Web Project Knowledge

1. Open [Claude.ai](https://claude.ai) and create or open a **Project**
2. Go to **Project Knowledge** → **Add content**
3. Upload or paste the contents of [`SKILL.md`](SKILL.md)

### Option C — Any Claude Interface

Paste the full contents of [`SKILL.md`](SKILL.md) into your system prompt or at the start of a conversation.

---

## Trigger Phrases

Once the skill is active, use any of these to start:

- `"Generate user stories"`
- `"I want to create user stories"`
- `"I need to create user stories"`
- `"Convert these requirements to user stories"`
- `"Transform this transcript into user stories"`

Then provide your input: a meeting transcript, feature list, stakeholder notes, or any text describing what needs to be built.

---

## Output

Each generated user story includes four fields:

| Column | Description |
|--------|-------------|
| **Key** | Unique identifier (e.g., `US-001`, `US-002`) |
| **Summary** | Brief one-line title (5–10 words) |
| **Description** | Full user story: *"As a [user], I want [goal], so that [benefit]"* |
| **Acceptance Criteria** | Testable conditions in `Given / When / Then` format (2–4 per story) |

### Output Formats

| Format | Best For |
|--------|----------|
| **CSV** | Direct import into Excel or Google Sheets |
| **Markdown Table** | GitHub, Notion, documentation sites |
| **JSON** | Programmatic use, piping into scripts |
| **Excel (.xlsx)** | Formatted spreadsheets via the included Python script |

---

## Excel Generator

A Python script is included to create professionally formatted `.xlsx` files from JSON output.

```bash
# Install dependency
pip install openpyxl

# Generate from a JSON file
python scripts/generate_excel.py --input stories.json --output user_stories.xlsx

# Generate from a JSON string
python scripts/generate_excel.py --output stories.xlsx --data '[{"key": "US-001", ...}]'
```

**Workflow:**
1. Ask Claude for output in JSON format
2. Save the JSON to `stories.json`
3. Run the script above
4. Open `user_stories.xlsx` — styled with frozen headers, wrapped text, and optimized column widths

See [`scripts/generate_excel.py`](scripts/generate_excel.py) for full usage.

---

## Examples

See the [`examples/`](examples/) folder for real input-to-output walkthroughs:

- [Task Management App](examples/task-management-app.md) — Meeting transcript → 9 sprint-ready user stories across 3 epics

---

## Methodology

This skill is based on established Agile practices:

- **INVEST criteria** — Bill Wake (2003)
- **Story splitting patterns** — Richard Lawrence (Humanizing Work)
- **User Stories Applied** — Mike Cohn (2004)
- **Scrum Guide** — Schwaber & Sutherland
- **Agile Alliance** — Industry standards

**Key principle — Vertical slicing:**
Each story delivers end-to-end user value (not a technical layer). A story is "done" when a user can complete a workflow, not when a database schema is built.

---

## Installing the Skill File

Download `user-story-generation-v2.skill` from [Releases](../../releases/latest) and import it via **Claude Settings → Capabilities → Add skill**.

---

## Contributing

Found a bug or have an idea for improvement? See [CONTRIBUTING.md](CONTRIBUTING.md).

- **Bug reports:** Open a [GitHub Issue](../../issues/new?template=bug_report.md)
- **Feature requests:** Open a [GitHub Issue](../../issues/new?template=feature_request.md)
- **Pull requests:** Fork the repo, make your change, and submit a PR

---

## License

[MIT](LICENSE) — Free to use, modify, and distribute.
