**revised, Python-native version** of the **Object-Oriented Design Principles Template**. It:

- Uses **Python idioms** (e.g., `@property`, `dataclasses`, duck typing),
- Drops **Java-specific constraints** (no interfaces, no `new` keyword),
- Embraces **Python’s “consenting adults” philosophy**,
- Keeps the **core OOP principles intact**, but applied *the Python way*.

---

# OBJECT-ORIENTED DESIGN PRINCIPLES TEMPLATE (Python Edition)  

**System:** [System Name]  
**Version:** [Version]  
**Date:** [Date]  

---

## 1. DESIGN PHILOSOPHY  

**Core Philosophy:**  
> *"Objects should encapsulate behavior and enforce invariants—not just hold data."*  

**Primary Goals:**  

- ✅ **Behavior-rich objects** (not data bags)  
- ✅ **Loose coupling** via dependency injection and duck typing  
- ✅ **Testability** through clear public interfaces  
- ✅ **Readability** over ceremony  

**Anti-Goals (What We Avoid):**  

- ❌ **Anemic models** (e.g., classes with only getters/setters)  
- ❌ **God classes** that do everything  
- ❌ **Procedural logic hidden inside methods** (e.g., `process_votes()` with 50 lines of ifs)  
- ❌ **Premature abstraction** (e.g., abstract base classes for two subclasses)  

---

## 2. CORE PRINCIPLES APPLIED (Python Style)

### SOLID — The Python Way

| Principle | Python Interpretation | Practical Guidelines | Code Smells |
|---------|-----------------------|----------------------|------------|
| **S – Single Responsibility** | “One class, one job” | • Class name should be a noun that describes its purpose<br>• If you need “and” in the job description → split it<br>• Keep public methods ≤ 5 | • `VotingSystem` that handles auth + votes + DB + UI<br>• 1,000-line classes<br>• Methods named `handle_*`, `manage_*`, `process_*` |
| **O – Open/Closed** | “Extend via composition or inheritance—but don’t break existing code” | • Use **strategy pattern with callables or protocols**<br>• Favor `@abstractmethod` only when needed<br>• New behavior via new classes, not modifying old ones | • Adding `elif vote_type == "special"` to core logic<br>• Monkey-patching core classes in tests |
| **L – Liskov Substitution** | “Subclasses should work anywhere the parent does” | • Don’t strengthen preconditions (`if not isinstance(x, int): raise` in subclass)<br>• Don’t weaken postconditions (returning `None` when parent returns object) | • Subclass that raises `NotImplementedError`<br>• `isinstance()` checks in client code |
| **I – Interface Segregation** | “Use duck typing or `Protocol`—don’t force clients to implement unused methods” | • Define **`typing.Protocol`** for roles (e.g., `Notifier`)<br>• Avoid “mega-interfaces”<br>• If a class implements 5+ methods but uses only 1 → split | • `class FakeDB` with 10 empty methods<br>• Passing objects that “quack like” the needed type but fail at runtime |
| **D – Dependency Inversion** | “Depend on abstractions (callables, protocols), not concrete classes” | • Inject dependencies via `__init__`<br>• Use **`Protocol` or `abc.ABC` only when needed for clarity/testability**<br>• Avoid global state or `from module import concrete_class` in core logic | • `VoteRecorder` doing `from db import SQLiteDB; self.db = SQLiteDB()`<br>• Hardcoded `print()` or `open()` in business logic |

---

### Supporting Principles (Python-Friendly)

- **Composition > Inheritance**  
  → Use **has-a**, not **is-a**, unless it’s a true specialization.  
  → Example: `Feed` has a `FilterStrategy`, not `class ChronologicalFeed(Feed)`.

- **Tell, Don’t Ask**  
  → **Bad**: `if voter.can_vote(): election.add_vote(voter, candidate)`  
  → **Good**: `voter.cast_vote(election, candidate)` → voter/election enforce rules internally.

- **Law of Demeter**  
  → **Bad**: `user.profile.address.city`  
  → **Good**: `user.get_city()` or `user.profile.get_city()` (only one dot for behavior)

- **DRY**  
  → But distinguish **duplication** from **coincidental similarity**.  
  → Don’t extract a function just because two lines look alike.

---

## 3. PYTHONIC DESIGN PATTERNS

| Pattern | When to Use | Python Implementation |
|--------|-------------|------------------------|
| **Strategy** | Multiple algorithms (e.g., vote tallying: simple vs. ranked) | Pass a **callable** or object with `__call__`<br>`election.set_tally_strategy(rank_choice_tally)` |
| **Factory** | Creating objects with complex setup | **Factory function** > factory class<br>`def create_voter(voter_id, registry) -> Voter:` |
| **Builder** | Objects with many optional params | Use `@dataclass` + `replace`, or class with `.set_x().build()` |
| **Observer** | Event-driven updates (e.g., notify when election closes) | Use `weakref.WeakSet` or simple list of callbacks<br>`election.on_close.append(email_admin)` |
| **Context Manager** | Resource management (e.g., election session) | `class ElectionSession:` with `__enter__`, `__exit__` |
| **Protocol (Structural Subtyping)** | Define “roles” without inheritance | ```python<br>from typing import Protocol<br>class Notifier(Protocol):<br>    def notify(self, msg: str) -> None: ...<br>``` |

> 💡 **Python Note**: You often **don’t need full Gang-of-Four patterns**.  
> A **function** or **closure** can replace a Strategy. A **dict** can replace a Flyweight.

---

## 4. CLASS DESIGN TEMPLATE (Python)

```python
## Voter
"""Encapsulates voter identity and voting behavior."""

# Responsibility: Represent an eligible voter who can cast exactly one vote per election.

class Voter:
    def __init__(self, voter_id: str, registry: "VoterRegistry"):
        self._voter_id = voter_id
        self._registry = registry
        self._elections_voted_in = set()  # private state

    @property
    def voter_id(self) -> str:
        return self._voter_id

    def cast_vote(self, election: "Election", candidate: str) -> None:
        """Cast a vote if eligible. Enforces: one vote per election."""
        if election.id in self._elections_voted_in:
            raise ValueError("Already voted in this election")
        if not self._registry.is_eligible(self._voter_id):
            raise ValueError("Voter not eligible")
        election._record_vote(self._voter_id, candidate)  # protected method
        self._elections_voted_in.add(election.id)

    # No public setters for internal state
    # No `get_voted_elections()` — that would violate encapsulation
```

**Design Notes:**  

- **Immutability**: `voter_id` is read-only (via `@property`).  
- **Encapsulation**: Internal state (`_elections_voted_in`) is private.  
- **Dependencies**: Injected (`registry`), not hardcoded.  
- **Behavior**: Rules enforced in `cast_vote`, not in a service.

---

## 5. PYTHON-SPECIFIC GUIDELINES

### Inheritance vs. Composition

| Use Inheritance When | Use Composition When |
|----------------------|----------------------|
| True “is-a” relationship (`AdminVoter` is a `Voter`) | Adding behavior (`Election` has a `TallyStrategy`) |
| Sharing implementation that won’t change | Need multiple behaviors or runtime switching |
| Using `super()` to extend, not replace | Avoiding deep hierarchies |

> 🐍 **Python Tip**: Favor **composition + delegation**. Inheritance is powerful but easy to overuse.

### Dependency Injection (Python Style)

```python
# Good: Constructor injection
class ElectionService:
    def __init__(self, voter_registry: VoterRegistry, notifier: Notifier):
        self._registry = voter_registry
        self._notifier = notifier

# Even simpler: Callable injection
class Election:
    def __init__(self, id: str, on_close: Callable[[str], None] = lambda x: None):
        self._on_close = on_close
```

> ✅ **No need for frameworks** like `dependency-injector` unless you have complex wiring.

---

## 6. PYTHON CODE QUALITY (Practical Metrics)

Forget Java-style metrics. Focus on:

- **Cyclomatic complexity** < 10 per function (`mccabe` or `radon`)
- **Public methods per class** ≤ 5
- **No `*args, **kwargs` hiding real interfaces**
- **No `isinstance()` checks in core logic** (breaks polymorphism)
- **Use `typing.Protocol` for duck typing clarity**

> 🛠️ Tools: `mypy`, `ruff`, `pylint`, `radon`

---

## 7. COMMON PYTHON OOP SMELLS → REFACTORINGS

| Smell | Refactoring |
|------|-------------|
| `if type(obj) == Voter:` | → Use polymorphism or `isinstance(obj, Voter)` only if unavoidable |
| `obj.get_data()['votes']` | → `obj.get_vote_count()` (Tell, Don’t Ask) |
| 10+ constructor args | → Use `@dataclass` or Builder |
| `utils.py` with 20 functions | → Move behavior into relevant classes |
| `class X: pass` with attributes set externally | → Define `__init__` and encapsulate |

---

## 8. TESTING STRATEGY (Pythonic)

```python
def test_voter_cannot_vote_twice():
    # Given
    registry = FakeRegistry(eligible_voters=["V1"])
    election = Election("E1")
    voter = Voter("V1", registry)

    # When
    voter.cast_vote(election, "C1")

    # Then
    with pytest.raises(ValueError, match="Already voted"):
        voter.cast_vote(election, "C2")
```

**Guidelines:**  

- **Test behavior, not state**: Don’t check `voter._elections_voted_in`  
- **Use real objects when possible**: Only mock I/O (DB, email)  
- **No mocking of collaborators** (e.g., don’t mock `Election` when testing `Voter`) unless slow or non-deterministic

---

## 9. QUICK PYTHON OOP RULES OF THUMB

1. **Classes < 300 lines**, **methods < 20 lines**  
2. **0–3 constructor args** (use `dataclass` or Builder if more)  
3. **3–5 public methods max per class**  
4. **Use `_private` for internal state/methods**  
5. **Prefer `@property` over getters**  
6. **Inject dependencies, don’t import them in `__init__`**  
7. **Raise meaningful exceptions (`ValueError`, `PermissionError`)**  
8. **Use `Protocol` to define roles, not abstract base classes (unless needed)**  

---

## 10. EXAMPLE: VOTING SYSTEM (Python)

```python
from typing import Protocol, Set

class VoterRegistry(Protocol):
    def is_eligible(self, voter_id: str) -> bool: ...

class Election:
    def __init__(self, eid: str):
        self.id = eid
        self._votes: dict[str, str] = {}  # voter_id → candidate (but not exposed!)
        self._is_open = True

    def close(self) -> None:
        self._is_open = False

    def results(self) -> dict[str, int]:
        from collections import Counter
        return Counter(self._votes.values())  # only expose aggregated data

    def _record_vote(self, voter_id: str, candidate: str) -> None:
        if not self._is_open:
            raise ValueError("Election closed")
        self._votes[voter_id] = candidate  # internal only

class Voter:
    def __init__(self, voter_id: str, registry: VoterRegistry):
        self._id = voter_id
        self._registry = registry
        self._voted_in: Set[str] = set()

    def cast_vote(self, election: Election, candidate: str) -> None:
        if election.id in self._voted_in:
            raise ValueError("Already voted")
        if not self._registry.is_eligible(self._id):
            raise ValueError("Not eligible")
        election._record_vote(self._id, candidate)  # protected method
        self._voted_in.add(election.id)
```

✅ **This is Pythonic OOP**:  

- Behavior in objects, not services  
- State encapsulated  
- Dependencies injected  
- No Java-style ceremony

---

### Final Note

This template **respects Python’s culture**:  
> **“Simple is better than complex. Flat is better than nested. Readability counts.”**  
> — *The Zen of Python*

Use principles to **solve real problems**—not to make your code look like Java.

Want to adapt this to your actual voting system? Share a class, and I’ll help you “Pythonify” it using these ideas.