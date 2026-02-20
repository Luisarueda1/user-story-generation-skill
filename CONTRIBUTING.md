# Contributing

Thank you for your interest in improving this skill!

## Reporting Bugs

If the skill produces incorrect or unexpected output:

1. Open a [bug report issue](../../issues/new?template=bug_report.md)
2. Include:
   - The input you provided to Claude
   - What output you expected
   - What output you actually received
   - Which Claude interface you used (Claude Web, Claude Code, API, etc.)

## Suggesting Features

Have an idea for a new capability or improvement?

1. Open a [feature request issue](../../issues/new?template=feature_request.md)
2. Describe the use case, not just the solution
3. Include a sample input and the output you'd want to see

## Submitting a Pull Request

1. Fork the repository
2. Create a branch: `git checkout -b my-improvement`
3. Make your changes
4. **Test the skill** by adding the updated `SKILL.md` to Claude and running at least one end-to-end test with real input
5. Submit a pull request with a clear description of what changed and why

## What's in Scope

- Improvements to the skill workflow or instructions (`SKILL.md`)
- New or improved examples (`examples/`)
- Bug fixes or enhancements to the Excel generator (`scripts/generate_excel.py`)
- Documentation improvements (`README.md`)

## Code Style

For the Python script, follow PEP 8. No external dependencies beyond `openpyxl`.
