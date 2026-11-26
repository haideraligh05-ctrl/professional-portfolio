# Portfolio reporting and AUM validation

**Problem.** Operations needed a consistent view of changes in assets under management (AUM), with a clear link between reported movement and validation decisions.

**My contribution.** I worked on business requirements for classifying portfolio movement, defining period baselines, and presenting targets and shortfalls across consultant and management levels. I translated retention and eligibility scenarios into rules for exception review.

**Design.** Capture opening and closing balances, calculate movement, classify the result, and record the source period and validation status. Route exceptions to an accountable reviewer with the underlying evidence and resolution.

**Illustrative acceptance checks**

- A portfolio whose closing balance equals its opening balance is classified as maintained.
- The headline movement reconciles to the underlying records for the selected scope and period.
- An exception retains the original outcome, the resolution, and the approval history.

**Project stage represented.** Business requirements, controls, and reporting design.
