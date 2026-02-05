Question
Strong Answer                                   Weak Answer (Avoid)
Q1  "Compare birth year to current minimum"     "Loop through tuples"
Q2  "Yes — state = person with earliest year seen so far"   "Variable gets updated in loop"
Q3  "Many inputs → one output (N:1 = reduction)"    "Returns a name"
Q4  "Find item with minimum value in a field" (works for servers/products/etc.) "Find oldest person" (domain-locked)
Q5  min(..., key=) or reduction/fold algorithm      "For loop with if statement"
Q6"Find extreme value via linear scan"      "Iterate and compare"