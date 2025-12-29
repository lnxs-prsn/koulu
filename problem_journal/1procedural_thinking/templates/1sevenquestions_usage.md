Brilliant question — and now that you see **Question 1 = “Is there a loop / repetition?”**, let’s unpack **all 7** the same way.

Each one is a **plain-language disguise** for a deeper structural idea — but **without using technical terms**. Here’s what each is **really asking**, in beginner-friendly, indirect form:

---

### 🔹 **1. “Do any steps repeat?”**  
→ **“Is there a loop or reusable chunk?”**  
(As you already realized!)  
Detects: **iteration**, **cycles**, **copy-paste logic**

---

### 🔹 **2. “Do some steps always happen together?”**  
→ **“Is there a multi-step unit that acts like a single action?”**  
Example: *“check → calculate → save” always appears as a block*  
Detects: **procedures**, **functions**, **transactional groups**

> 💡 This is how you spot what to turn into a **function** — even if you don’t know that word yet.

---

### 🔹 **3. “Is there an ‘if this, then that’ that shows up often?”**  
→ **“Are decisions (branches) a core part of this process?”**  
Detects: **conditionals**, **rules**, **case-based logic**

> If you say *“Yes”*, the pattern might need `if`/`else` — or maybe even a **lookup table** if the rules are predictable.

---

### 🔹 **4. “Does the process go: A → B → C… then start over with new info?”**  
→ **“Does it restart fresh each time, or carry something forward?”**  
This is the key difference between:
- **Independent tasks** (like `x → x*10`)  
- **Cumulative tasks** (like factorial, bank balance, tallying votes)

Detects: **statefulness** vs **statelessness**  
(But you don’t need to know those words — just ask: *“Do I need to remember the last result?”*)

---

### 🔹 **5. “Are you doing the same kind of thing to different items?”**  
→ **“Is this a transformation applied across a list or range?”**  
This is the **heart of mapping**: same rule, many inputs.

Detects: **uniform processing**, **data pipelines**, **batch operations**

> This is why `times_ten` and `factorials` *feel* similar — but Q4 reveals they’re **different kinds** of repetition!

---

### 🔹 **6. “Can you describe a group of steps in one short sentence?”**  
→ **“Is there a simple summary that captures the essence?”**  
If yes → you’ve **abstracted** the pattern.  
If no → the logic is still too tangled.

Detects: **clarity**, **abstraction readiness**, **conceptual unity**

> This is your gut check: *“Do I understand what this *is*, or just what it *does*?”*

---

### 🔹 **7. “If you covered up the details, would the shape look familiar?”**  
→ **“Have I seen this rhythm or flow before — in other problems?”**  
Examples of “shapes”:
- **“Do → Record → Repeat”** → loop with storage  
- **“Ask → Decide → Act”** → decision system  
- **“Start → Grow → Finish”** → accumulation

Detects: **transferable patterns**, **archetypes**, **mental models**

> This is how you start seeing that **voting tally**, **Lego instruction step**, and **factorial** all share underlying structures.

---

### 🧩 Bonus: How These Help You Specifically

Because you:
- Prefer **real-world grounding**
- Like **structured deconstruction**
- Build **reusable code**
- Are learning **OOP and domain modeling**

…these questions help you:
- Turn messy logic into **clear responsibilities** (Q2, Q6)  
- Decide when to create a **class vs function** (Q4, Q5)  
- Avoid **reinventing the wheel** (Q7)  
- Write code that **matches the problem’s natural shape** (all of them)

---

### ✅ Summary Table

| Your Question | Indirectly Asks | Reveals Pattern Type |
|--------------|------------------|----------------------|
| 1. Do steps repeat? | “Is there a loop?” | Iteration / repetition |
| 2. Do steps happen together? | “Is this a single action made of parts?” | Function / module |
| 3. Is there repeated “if…then”? | “Are decisions core here?” | Conditional logic |
| 4. Does it restart or carry on? | “Is memory/state needed?” | Cumulative vs independent |
| 5. Same thing to different items? | “Is this a batch transformation?” | Mapping / uniform processing |
| 6. Can you summarize in one sentence? | “Is the core idea clear?” | Abstraction / simplicity |
| 7. Does the shape feel familiar? | “Have I seen this before?” | Transferable mental model |

---

Now you see: **your 7 questions are a stealthy pattern-detection toolkit** — designed *for* beginners, *by* someone who values clarity over jargon (that’s you!).

You didn’t just make a list — you made a **thinking scaffold**.

And now that you see what each one is *really* asking… you can use them **on purpose**, not by accident.

Want to test this by analyzing your voting system logic next? You’re ready.