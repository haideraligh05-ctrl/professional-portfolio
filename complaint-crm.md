# Complaint CRM and SLA tracking

**Problem.** Staff needed consistent classification, clear ownership, and visibility into complaints awaiting action.

**My contribution.** I worked on classification and escalation requirements and supported pilot UAT. My testing identified gaps in acknowledgement and escalation actions, reopened-case behavior, and the separation of queues for initiators and handlers.

**Design.** Record each complaint with a unique reference and category. Assign a handler, capture acknowledgement, monitor the response deadline, and retain status and ownership history through resolution and any reopening.

**Illustrative acceptance checks**

- The handler can acknowledge the complaint and route it for escalation.
- Reopening a resolved case preserves prior activity and returns the case to the handler queue.
- A complaint completed exactly at its deadline is recorded as within SLA.

**Project stage represented.** Pilot UAT and defect reporting.
