(for Multiple Authorities)
List all actions (not just one!)
→ “Lend”, “Return”, “Reserve”, “Notify overdue”, etc.
For each action, ask:
→ Who has full knowledge to perform this safely and completely?
→ Who enforces the rules for this action?
Assign that action to one authority
→ Even if others are consulted, only one object executes it
If two objects seem equally authoritative, ask:
→ Is this really two separate actions?
→ Or do I need a new coordinator object (e.g., LendingService, TransactionManager)?




In OO design, the authority (often a domain service or aggregate root) is the rightful holder of business logic,
while other participants (entities, value objects) primarily encapsulate state and enforce local invariants—not system-wide rules.