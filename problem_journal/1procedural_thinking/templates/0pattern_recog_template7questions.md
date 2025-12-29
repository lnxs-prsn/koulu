
### 1. **Decomposition & Granularity**
- _What are the smallest indivisible steps in this process?_
- _Can any steps be grouped into higher-level actions or phases?_
- _Are there repeated sequences or loops? If so, what triggers them?_

### 2. **Flow & Control**
- _What determines the order of operations? (e.g., conditions, inputs, state changes)_
- _Where do branches (if/else decisions) occur, and what are their conditions?_
- _Is the flow strictly linear, or are there feedback loops, parallel paths, or recursion?_

### 3. **State & Data**
- _What data or state is being read, modified, or passed between steps?_
- _Does the output of one operation consistently become the input of another?_
- _Are there variables or objects that persist across multiple operations?_

### 4. **Roles & Relationships**
- _Which entities (objects, actors, components) perform or are affected by each operation?_
- _Who or what is the active agent in each step? Who or what is passive?_
- _Are there clear responsibilities or boundaries emerging between components?_

### 5. **Patterns & Abstractions**
- _Do certain combinations of operations repeat with only minor variations?_
- _Can any set of operations be abstracted into a function, method, or class?_
- _Does this resemble any known algorithmic or architectural pattern (e.g., state machine, pipeline, observer)?_

### 6. **Constraints & Invariants**
- _What must always be true before or after a given operation?_
- _Are there assumptions or preconditions that, if violated, break the process?_
- _What stays constant throughout the process (invariants)?_

### 7. **Purpose & Outcome**
- _What is the ultimate goal of this process?_
- _If I remove or reorder a step, does the outcome change in a predictable way?_
- _What minimal set of operations still achieves the core purpose?