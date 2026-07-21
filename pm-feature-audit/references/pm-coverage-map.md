# Project-management coverage map

The coverage scaffold for the pm-feature-audit skill. Enumerate these jobs and mark each present, partial, or absent in the tool in front of you. It is a checklist to guarantee coverage rather than a script to recite, so report in the user's terms, with severity and the cost to them, the way SKILL.md describes.

Crucially, **not every job applies to every tool.** Each entry notes when it is load-bearing and when it is out of scope or outright bloat. Calibrate to the archetype first (who runs what kind of projects, at what scale), and then judge each job against *that*. Skip what's irrelevant and say why, rather than padding the report with gaps that the users will never feel.

## The core four, load-bearing in almost any PM tool

If any of these is absent, it's usually a blocker: you can't run a project without them.

1. **Work items / tasks.** The atomic unit of work. *Present:* create, name, and describe a unit of work; subtasks or checklists to break it down. *Gaps:* no way to break a big thing into small things; no description, so a task is a bare title with no context.

2. **Ownership / assignment.** Who is responsible. *Present:* a clear owner per task; ideally one accountable owner even where several people help. *Gaps:* no assignee at all, so no accountability; or only multi-assignee with no single owner, so everyone's job is no one's job.

3. **Status / progress.** Where each thing stands. *Present:* a set of states (to-do / doing / done, or finer) or % complete, visible at a glance. *Gaps:* a binary done/not-done where the work has real in-between stages; status you can't see without opening each item.

4. **Dates / deadlines.** When things are due. *Present:* due dates on work items, and a notion of "what's due soon." *Gaps:* no dates, so nothing has a deadline and nothing can be late; start dates with no due dates, or the reverse.

## Scheduling and sequencing, load-bearing when work has order and hard deadlines

5. **Dependencies / sequencing.** This must happen before that. *Present:* link a task as blocking or blocked-by another; ideally see the knock-on of a slip. *Gaps:* the most common serious hole in lightweight tools, where work that must be ordered is shown as a flat unordered list, so nobody can see the critical path or what a delay cascades into. *Out of scope:* a tool for genuinely independent, unordered tasks (a personal backlog, a content idea list) doesn't need it, so don't force it.

6. **Timeline / schedule view.** The work on a time axis. *Present:* a Gantt or calendar showing what lands when; milestones as fixed points. *Gaps:* every task exists but there's no way to *read the schedule*, and no answer to "what does the next month look like." The missing concept is usually time-on-an-axis; adding it tends to deliver milestones and "due this week" at once. *Out of scope:* a pure now/next board for a team that doesn't plan against dates.

7. **Milestones.** The fixed points that matter. *Present:* mark a date or deliverable as a milestone, distinct from ordinary tasks. *Gaps:* no way to distinguish "the show opens" from "email the printer", so everything is the same weight.

## Visibility and control, load-bearing once more than one person is involved

8. **Prioritisation.** What matters most. *Present:* order by importance, or a priority field that drives sorting and filtering. *Gaps:* no way to say one thing matters more than another, so a flat list gives no signal about where to start.

9. **Risk / issues / blocked flag.** What might go wrong, surfaced early. *Present:* flag a task as at-risk or blocked; filter to see everything in trouble. *Gaps:* a frequent serious hole, where the tool tracks done vs not-done but can't show *trouble before the deadline*, so problems are invisible until they bite. The whole point of tracking is to see slippage early.

10. **Progress roll-up / "are we on track".** The state of the whole, not just the parts. *Present:* a project-level read that shows % complete, items remaining, on or off track, or a burndown or a simple count. *Gaps:* you can see each task but not the project, and the manager has to add it up in their head.

11. **Reporting / stakeholder view.** The answer for someone who isn't in the tool daily. *Present:* a status summary, dashboard, or shareable view pitched at a sponsor or client, not the doer. *Gaps:* the only view is the working view, so there's nothing to show a funder or a board without a guided tour. Note the audiences, because the doer, the manager, and the sponsor read the same project differently, and one flat view rarely serves all three. *Out of scope (lightly):* a solo tool has no stakeholders to report to.

## Collaboration and record, load-bearing for teams, optional for solo

12. **Comments / discussion on work.** Conversation attached to the thing it's about. *Present:* comment on a task; @mention to pull someone in. *Gaps:* discussion happens in chat or email, detached from the work, so the *why* behind a task is lost.

13. **Notifications / reminders.** The tool nudges, so work doesn't fall through silently. *Present:* deadline reminders, assignment alerts, due-soon nudges. *Gaps:* a serious hole in practice, because without reminders every deadline depends on someone remembering to look, and things slip not from disagreement but from silence.

14. **Documentation / attachments.** The artefacts the work needs. *Present:* attach files, links, briefs, and notes to a task or project. *Gaps:* nowhere to put the brief or the asset, so reference material lives elsewhere and goes stale.

15. **Activity / change history.** What changed, when, and by whom. *Present:* an audit trail on a task or project; ideally who moved a date or reassigned an owner. *Gaps:* scope and dates change with no record, so nobody can reconstruct what happened or when a deadline moved. Load-bearing wherever accountability or change-tracking matters, notably in grant-funded or client work.

## Scale and structure, load-bearing only above a certain size

16. **Multiple projects / portfolio.** More than one project, and how they relate. *Present:* separate projects; a cross-project view; shared people across them. *Gaps:* everything is one undifferentiated pile when it should be several projects; or projects exist but there's no roll-up across them. *Out of scope:* a single-project tool by design should be judged as one project, so don't invent a portfolio it doesn't need.

17. **Permissions / roles.** Who can see and change what. *Present:* roles (admin vs member), or per-project access. *Gaps:* relevant once there are people who shouldn't edit everything, or external collaborators; irrelevant for a trusted small team where everyone is an admin by design, so don't manufacture a need.

18. **Templates / recurrence.** Repeatable structure for work that repeats. *Present:* save a project or task structure and reuse it; recurring tasks. *Gaps:* a real time-sink for teams that run the *same shape* of project over and over (events, sprints, client onboarding) and rebuild it by hand each time. *Out of scope:* one-off or never-repeating work.

19. **Search / findability.** Finding a thing across the data. *Present:* search by name; filter by owner, status, date, tag. *Gaps:* fine to skip while the data is tiny; a real gap once there's enough that scrolling stops working.

20. **Integrations.** Connection to where the work actually happens. *Present:* links to calendar, email, chat, or file storage, wherever the team already lives. *Gaps:* the tool is an island the team has to remember to visit, and the value of a reminder or a due date drops sharply if it doesn't reach where people already look.

## The frequently-not-needed: bloat in the wrong tool, essential in the right one

Scrutinise these hardest for *fit*. Each is load-bearing for a specific kind of project and pure weight everywhere else. A gap here is only a gap if the archetype actually calls for it, and more often the finding is "cut this" rather than "add this."

- **Time tracking / logged effort.** Essential for anyone who bills by the hour or measures effort against estimate; dead weight for a team that doesn't. A "log hours" field nobody fills in is worse than nothing.
- **Budget / cost tracking.** Essential for agencies and grant-funded projects with reportable spend; out of scope for most internal task management. Where it *is* needed (funded projects with a budget line per work package), its absence is a real gap, not bloat.
- **Estimation / story points / velocity.** Load-bearing for engineering teams running sprints; meaningless overhead for a team that doesn't plan in points.
- **Sprints / iterations / agile ceremonies.** Right for software teams who work that way; imposing them on a team that doesn't is process for its own sake.
- **Workflow automation / custom rules.** Powerful at scale; a maintenance and comprehension cost for a small team that could do the thing by hand in less time than it takes to configure the rule.
- **Resource levelling / capacity planning.** Load-bearing when many people are shared across many projects and over-allocation is a real risk; overkill for a handful of people on one project.
- **Unlimited custom fields.** A little is useful; unlimited custom fields is how a tool rots into an unscannable form that nobody completes.

## Reminders

When several gaps share a root concept, name the concept, because one fix retires the cluster. When a feature is bloat, say *cut*, and say why it doesn't fit *these* users. And every finding carries the cost to the user: a gap without a "so they can't..." is an observation, not a finding.
