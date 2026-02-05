1. What is the single logical operation being applied repeatedly?
(Not "are there loops?" but: "What decision or transformation happens identically for each item?")
→ Forces distinction between homogeneous repetition (filter/reduce) vs. heterogeneous steps (composition).
2. Does the operation maintain state across iterations? If so, what does that state represent?
(Examples: "best-so-far", "running total", "collection of matches". No state = filter/transform; state = reduce/aggregate.)
→ Separates filter (no state beyond output list) from reduction (state = accumulator).
3. What is the relationship between input items and output items?
One input item → zero/one output item? (filter)
Many input items → one output item? (reduction)
One input item → one transformed output item? (map/transform)
One input item → many output items? (expand/flatten)
→ Names the structural shape independent of domain.
4. Could you replace the domain nouns (movies/people) with placeholders and still describe the solution?
(If yes: "Keep items where [field] matches [condition]" → reusable pattern. If no: domain-specific logic.)
→ Tests whether you've abstracted beyond surface details.
5. What built-in language construct or algorithmic idiom directly expresses this pattern?
(Examples: filter(), min(..., key=), list comprehension with if, reduce(). If none exists → novel composition.)
→ Connects your mental model to established patterns/tooling.
6. If you removed all loops/conditionals from your description, what purpose would remain?
(Example: "Find items matching a condition" survives loop removal; "iterate with index" does not.)
→ Strips away implementation noise to reveal core intent.