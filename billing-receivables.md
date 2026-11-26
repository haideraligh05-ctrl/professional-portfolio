# Billing and receivables prototype

**Aligh Nexus Solutions project · Browser prototype**

The prototype brings client records, service and product catalogs, invoice preparation, and payment entry together for a diagnostics business.

**Demonstration scenario.** Set up a sample client and service, create an itemized invoice, log a payment, then review the remaining balance in the receivables view. The interface also exposes an invoice register and an outstanding-client list for follow-up.

## Worked example: partial payment

A fictional diagnostics provider invoices a client for two screening services at 120 units each and one reporting service at 60 units. The invoice total is 300 units.

| Event | Invoice total | Payments received | Outstanding | Status |
| --- | ---: | ---: | ---: | --- |
| Invoice issued | 300 | 0 | 300 | Open |
| First payment allocated | 300 | 120 | 180 | Partially paid |
| Final payment allocated | 300 | 300 | 0 | Paid |

At the second step, the invoice register retains the original 300-unit charge and the receivables view shows the remaining 180 units. The acceptance check is that the outstanding balance equals the invoice total minus posted payments and disappears from the open queue when it reaches zero. All amounts are synthetic.
