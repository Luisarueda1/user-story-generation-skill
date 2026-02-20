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
