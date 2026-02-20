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

| Category/Epic | Title | User Story | Acceptance Criteria | Requirement | Pain Point | Created Date |
|---------------|-------|------------|---------------------|-------------|------------|--------------|
| Task Visibility | Highlight overdue tasks on dashboard | As a team member, I want overdue tasks highlighted on my dashboard, given I have tasks past their due date, so that I can immediately identify and prioritize work that needs urgent attention. | - Given I have tasks past their due date, when I open my dashboard, then overdue tasks are visually highlighted in red<br>- Given an overdue task, when I hover over the highlight, then I see the number of days overdue | Users need to see overdue tasks at a glance | Users don't know tasks are overdue until it's too late | 2026-02-20 |
| Task Visibility | Send overdue task email alert | As a team member, I want to receive an email alert when one of my tasks becomes overdue, given I am not actively using the app, so that I am notified even when I'm away from the tool. | - Given a task reaches its due date without completion, when the due date passes, then I receive an email within 15 minutes<br>- Given I have email notifications disabled, when a task becomes overdue, then I do not receive an email | Alert users when tasks become overdue | Users miss overdue tasks when not logged in | 2026-02-20 |
| Task Visibility | View team workload as a manager | As a team manager, I want a view showing all tasks assigned to my team members, given I am responsible for team delivery, so that I can identify workload imbalances and who may need support. | - Given I am logged in as a manager, when I open the Team Workload view, then I see each team member with their active and overdue task counts<br>- Given a team member has overdue tasks, when I view their workload, then overdue items are visually distinct from active ones | Managers need visibility into team task status | Managers have no way to see what their team is working on | 2026-02-20 |
| Task Visibility | Filter team tasks by status | As a team manager, I want to filter team tasks by status and assignee, given I need to focus on specific problem areas, so that I can quickly drill down without scrolling through all tasks. | - Given I am on the Team Workload view, when I apply a status filter (e.g., "Overdue"), then only matching tasks are shown<br>- Given I apply multiple filters, when the view refreshes, then only tasks matching all selected filters are displayed | Allow managers to narrow team task views | Lack of filtering makes it hard to identify problem areas | 2026-02-20 |
| Notifications | Set notification preferences per event | As a user, I want to choose which events trigger my notifications, given I am being over-notified on low-priority events, so that I only receive alerts for things that are relevant to me. | - Given I am in notification settings, when I toggle off an event type, then I stop receiving notifications for that event<br>- Given I save my preferences, when a toggled-off event occurs, then no notification is sent | Allow users to control which events notify them | Notification system sends too many or too few alerts | 2026-02-20 |
| Notifications | Choose notification delivery channel | As a user, I want to choose whether notifications arrive by email, in-app, or both, given different channels suit different work contexts, so that I get alerts in the format that fits my workflow. | - Given I select "In-app only" for an event type, when that event occurs, then I receive an in-app banner but no email<br>- Given I select "Email only", when that event occurs, then I receive an email but no in-app notification | Let users pick notification delivery format | Users have no control over how they receive notifications | 2026-02-20 |
| Collaboration | Comment on a task | As a team member, I want to leave comments on a task, given that work discussions currently happen in Slack and context gets lost, so that I can keep all task-related conversation in one place. | - Given I am viewing a task, when I type a comment and click Submit, then my comment appears in the task thread with my name and timestamp<br>- Given a task has existing comments, when I open the task, then I see all previous comments in chronological order | Allow users to comment directly on tasks | Context is lost when task discussions move to Slack | 2026-02-20 |
| Collaboration | Notify assignee of new comment | As a task assignee, I want to be notified when someone comments on my task, given I may not be actively viewing the task, so that I don't miss important feedback or questions. | - Given someone posts a comment on a task assigned to me, when the comment is submitted, then I receive an in-app notification<br>- Given my preferences allow email, when a comment is posted on my task, then I also receive an email notification | Notify task owners of new comments | Team members miss questions and feedback on their tasks | 2026-02-20 |
| Reporting | View team status dashboard | As a project manager, I want a real-time dashboard showing task completion rates by person and project, given leadership requires weekly status summaries, so that I can generate updates without manually compiling data. | - Given I open the Reports dashboard, when the page loads, then I see completion rate by team member and by project for the current week<br>- Given I want to view a different period, when I change the date range, then the dashboard updates to reflect the selected timeframe | Provide a real-time team status dashboard | Reporting requires manual CSV exports and pivot tables | 2026-02-20 |

---

## JSON Output

```json
[
  {
    "category_epic": "Task Visibility",
    "title": "Highlight overdue tasks on dashboard",
    "user_story": "As a team member, I want overdue tasks highlighted on my dashboard, given I have tasks past their due date, so that I can immediately identify and prioritize work that needs urgent attention.",
    "acceptance_criteria": "- Given I have tasks past their due date, when I open my dashboard, then overdue tasks are visually highlighted in red\n- Given an overdue task, when I hover over the highlight, then I see the number of days overdue",
    "requirement": "Users need to see overdue tasks at a glance",
    "pain_point": "Users don't know tasks are overdue until it's too late",
    "created_date": "2026-02-20"
  },
  {
    "category_epic": "Task Visibility",
    "title": "Send overdue task email alert",
    "user_story": "As a team member, I want to receive an email alert when one of my tasks becomes overdue, given I am not actively using the app, so that I am notified even when I'm away from the tool.",
    "acceptance_criteria": "- Given a task reaches its due date without completion, when the due date passes, then I receive an email within 15 minutes\n- Given I have email notifications disabled, when a task becomes overdue, then I do not receive an email",
    "requirement": "Alert users when tasks become overdue",
    "pain_point": "Users miss overdue tasks when not logged in",
    "created_date": "2026-02-20"
  },
  {
    "category_epic": "Task Visibility",
    "title": "View team workload as a manager",
    "user_story": "As a team manager, I want a view showing all tasks assigned to my team members, given I am responsible for team delivery, so that I can identify workload imbalances and who may need support.",
    "acceptance_criteria": "- Given I am logged in as a manager, when I open the Team Workload view, then I see each team member with their active and overdue task counts\n- Given a team member has overdue tasks, when I view their workload, then overdue items are visually distinct from active ones",
    "requirement": "Managers need visibility into team task status",
    "pain_point": "Managers have no way to see what their team is working on",
    "created_date": "2026-02-20"
  },
  {
    "category_epic": "Task Visibility",
    "title": "Filter team tasks by status",
    "user_story": "As a team manager, I want to filter team tasks by status and assignee, given I need to focus on specific problem areas, so that I can quickly drill down without scrolling through all tasks.",
    "acceptance_criteria": "- Given I am on the Team Workload view, when I apply a status filter (e.g., \"Overdue\"), then only matching tasks are shown\n- Given I apply multiple filters, when the view refreshes, then only tasks matching all selected filters are displayed",
    "requirement": "Allow managers to narrow team task views",
    "pain_point": "Lack of filtering makes it hard to identify problem areas",
    "created_date": "2026-02-20"
  },
  {
    "category_epic": "Notifications",
    "title": "Set notification preferences per event",
    "user_story": "As a user, I want to choose which events trigger my notifications, given I am being over-notified on low-priority events, so that I only receive alerts for things that are relevant to me.",
    "acceptance_criteria": "- Given I am in notification settings, when I toggle off an event type, then I stop receiving notifications for that event\n- Given I save my preferences, when a toggled-off event occurs, then no notification is sent",
    "requirement": "Allow users to control which events notify them",
    "pain_point": "Notification system sends too many or too few alerts",
    "created_date": "2026-02-20"
  },
  {
    "category_epic": "Notifications",
    "title": "Choose notification delivery channel",
    "user_story": "As a user, I want to choose whether notifications arrive by email, in-app, or both, given different channels suit different work contexts, so that I get alerts in the format that fits my workflow.",
    "acceptance_criteria": "- Given I select \"In-app only\" for an event type, when that event occurs, then I receive an in-app banner but no email\n- Given I select \"Email only\", when that event occurs, then I receive an email but no in-app notification",
    "requirement": "Let users pick notification delivery format",
    "pain_point": "Users have no control over how they receive notifications",
    "created_date": "2026-02-20"
  },
  {
    "category_epic": "Collaboration",
    "title": "Comment on a task",
    "user_story": "As a team member, I want to leave comments on a task, given that work discussions currently happen in Slack and context gets lost, so that I can keep all task-related conversation in one place.",
    "acceptance_criteria": "- Given I am viewing a task, when I type a comment and click Submit, then my comment appears in the task thread with my name and timestamp\n- Given a task has existing comments, when I open the task, then I see all previous comments in chronological order",
    "requirement": "Allow users to comment directly on tasks",
    "pain_point": "Context is lost when task discussions move to Slack",
    "created_date": "2026-02-20"
  },
  {
    "category_epic": "Collaboration",
    "title": "Notify assignee of new comment",
    "user_story": "As a task assignee, I want to be notified when someone comments on my task, given I may not be actively viewing the task, so that I don't miss important feedback or questions.",
    "acceptance_criteria": "- Given someone posts a comment on a task assigned to me, when the comment is submitted, then I receive an in-app notification\n- Given my preferences allow email, when a comment is posted on my task, then I also receive an email notification",
    "requirement": "Notify task owners of new comments",
    "pain_point": "Team members miss questions and feedback on their tasks",
    "created_date": "2026-02-20"
  },
  {
    "category_epic": "Reporting",
    "title": "View team status dashboard",
    "user_story": "As a project manager, I want a real-time dashboard showing task completion rates by person and project, given leadership requires weekly status summaries, so that I can generate updates without manually compiling data.",
    "acceptance_criteria": "- Given I open the Reports dashboard, when the page loads, then I see completion rate by team member and by project for the current week\n- Given I want to view a different period, when I change the date range, then the dashboard updates to reflect the selected timeframe",
    "requirement": "Provide a real-time team status dashboard",
    "pain_point": "Reporting requires manual CSV exports and pivot tables",
    "created_date": "2026-02-20"
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
3. Open `task_management_stories.xlsx` — 9 rows across 7 columns (Category/Epic, Title, User Story, Acceptance Criteria, Requirement, Pain Point, Created Date) with blue headers, frozen first row, and wrapped text.
