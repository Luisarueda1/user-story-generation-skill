# Example: Task Management App — Meeting Transcript

This example demonstrates the full skill workflow: raw meeting transcript → pain point analysis → 9 sprint-ready user stories across 3 epics.

---

## User Input

```
"Generate user stories from this product meeting transcript:

Product Manager: Our users are really struggling with task visibility. People don't know what's
overdue until it's too late, and managers have no way to see what their team is actually working on.

Dev Lead: Yeah, and the notification system is basically broken — people either get spammed or
miss critical alerts entirely. There's no way to customize what you get notified about.

Designer: The other big pain I keep hearing is around collaboration. Right now you can't leave
comments on a task, so everything moves to Slack and context gets lost. People want to discuss
work inside the tool.

Product Manager: And reporting is a nightmare. Leadership keeps asking for weekly status summaries
and we're manually exporting CSVs and building pivot tables. We need a dashboard they can just
look at."
```

---

## Pain Points Identified

| # | Pain Point | Type |
|---|------------|------|
| 1 | Users don't see overdue tasks until it's too late | Explicit ("don't know what's overdue") |
| 2 | Managers lack visibility into team workload | Explicit ("no way to see what their team is working on") |
| 3 | Notification system sends too many or too few alerts | Explicit ("spammed or miss critical alerts") |
| 4 | No way to customize notification preferences | Explicit ("no way to customize") |
| 5 | No in-task commenting — context lost in Slack | Explicit ("can't leave comments on a task") |
| 6 | Reporting requires manual CSV exports and pivot tables | Explicit ("manually exporting CSVs") |

---

## Generated Stories

### Markdown Table Output

| Key | Summary | Description | Acceptance Criteria |
|-----|---------|-------------|---------------------|
| US-001 | Highlight overdue tasks on dashboard | As a team member, I want overdue tasks highlighted on my dashboard, so that I can immediately identify and prioritize work that is past its due date. | Given I have tasks past their due date / When I open my dashboard / Then overdue tasks are visually highlighted in red with the number of days overdue displayed |
| US-002 | Send overdue task email notifications | As a team member, I want to receive an email notification when one of my tasks becomes overdue, so that I am alerted even when I'm not actively using the app. | Given I have a task that reaches its due date without being completed / When the due date passes / Then I receive an email notification within 15 minutes |
| US-003 | View team workload as a manager | As a team manager, I want a view showing all tasks assigned to my team members, so that I can identify workload imbalances and who may need help. | Given I am logged in as a manager / When I open the Team Workload view / Then I see each team member's name, number of active tasks, and number of overdue tasks |
| US-004 | Filter team tasks by status and assignee | As a team manager, I want to filter team tasks by status and assignee, so that I can quickly focus on specific problem areas without scrolling through everything. | Given I am on the Team Workload view / When I apply a filter by status (e.g., "Overdue") / Then only tasks matching that status are displayed; filters can be combined |
| US-005 | Set notification preferences per event type | As a user, I want to choose which events trigger notifications, so that I only receive alerts for things that matter to me. | Given I am in my notification settings / When I toggle off a specific event type (e.g., "Task assigned to me") / Then I stop receiving notifications for that event type |
| US-006 | Choose notification delivery channel | As a user, I want to choose whether I receive notifications by email, in-app, or both, so that I get alerts in the format that fits my workflow. | Given I am in my notification settings / When I select "In-app only" for an event type / Then I receive in-app banners but no emails for that event |
| US-007 | Comment on a task | As a team member, I want to leave comments on a task, so that I can discuss the work in context without switching to a separate messaging tool. | Given I am viewing a task / When I type a comment and click Submit / Then my comment appears in the task thread with my name and timestamp |
| US-008 | Notify assignee of new task comment | As a task assignee, I want to be notified when someone comments on my task, so that I don't miss important feedback or questions. | Given someone posts a comment on a task assigned to me / When the comment is submitted / Then I receive an in-app notification; if my preferences allow, also an email |
| US-009 | View team status dashboard | As a project manager, I want a real-time dashboard showing task completion rates by person and project, so that I can generate status updates without manually compiling data. | Given I open the Reports dashboard / When the page loads / Then I see completion rate by team member and by project for the current week, with the ability to change the date range |

---

## JSON Output

```json
[
  {
    "key": "US-001",
    "summary": "Highlight overdue tasks on dashboard",
    "description": "As a team member, I want overdue tasks highlighted on my dashboard, so that I can immediately identify and prioritize work that is past its due date.",
    "acceptance_criteria": "Given I have tasks past their due date\nWhen I open my dashboard\nThen overdue tasks are visually highlighted in red with the number of days overdue displayed"
  },
  {
    "key": "US-002",
    "summary": "Send overdue task email notifications",
    "description": "As a team member, I want to receive an email notification when one of my tasks becomes overdue, so that I am alerted even when I'm not actively using the app.",
    "acceptance_criteria": "Given I have a task that reaches its due date without being completed\nWhen the due date passes\nThen I receive an email notification within 15 minutes"
  },
  {
    "key": "US-003",
    "summary": "View team workload as a manager",
    "description": "As a team manager, I want a view showing all tasks assigned to my team members, so that I can identify workload imbalances and who may need help.",
    "acceptance_criteria": "Given I am logged in as a manager\nWhen I open the Team Workload view\nThen I see each team member's name, number of active tasks, and number of overdue tasks"
  },
  {
    "key": "US-004",
    "summary": "Filter team tasks by status and assignee",
    "description": "As a team manager, I want to filter team tasks by status and assignee, so that I can quickly focus on specific problem areas without scrolling through everything.",
    "acceptance_criteria": "Given I am on the Team Workload view\nWhen I apply a filter by status (e.g., \"Overdue\")\nThen only tasks matching that status are displayed; filters can be combined"
  },
  {
    "key": "US-005",
    "summary": "Set notification preferences per event type",
    "description": "As a user, I want to choose which events trigger notifications, so that I only receive alerts for things that matter to me.",
    "acceptance_criteria": "Given I am in my notification settings\nWhen I toggle off a specific event type (e.g., \"Task assigned to me\")\nThen I stop receiving notifications for that event type"
  },
  {
    "key": "US-006",
    "summary": "Choose notification delivery channel",
    "description": "As a user, I want to choose whether I receive notifications by email, in-app, or both, so that I get alerts in the format that fits my workflow.",
    "acceptance_criteria": "Given I am in my notification settings\nWhen I select \"In-app only\" for an event type\nThen I receive in-app banners but no emails for that event"
  },
  {
    "key": "US-007",
    "summary": "Comment on a task",
    "description": "As a team member, I want to leave comments on a task, so that I can discuss the work in context without switching to a separate messaging tool.",
    "acceptance_criteria": "Given I am viewing a task\nWhen I type a comment and click Submit\nThen my comment appears in the task thread with my name and timestamp"
  },
  {
    "key": "US-008",
    "summary": "Notify assignee of new task comment",
    "description": "As a task assignee, I want to be notified when someone comments on my task, so that I don't miss important feedback or questions.",
    "acceptance_criteria": "Given someone posts a comment on a task assigned to me\nWhen the comment is submitted\nThen I receive an in-app notification; if my preferences allow, also an email"
  },
  {
    "key": "US-009",
    "summary": "View team status dashboard",
    "description": "As a project manager, I want a real-time dashboard showing task completion rates by person and project, so that I can generate status updates without manually compiling data.",
    "acceptance_criteria": "Given I open the Reports dashboard\nWhen the page loads\nThen I see completion rate by team member and by project for the current week, with the ability to change the date range"
  }
]
```

---

## How to Generate the Excel File

1. Save the JSON above to `stories.json`
2. Run:
   ```bash
   pip install openpyxl
   python ../scripts/generate_excel.py --input stories.json --output task_management_stories.xlsx
   ```
3. Open `task_management_stories.xlsx` — 9 formatted rows with frozen headers, wrapped text, and styled columns.
