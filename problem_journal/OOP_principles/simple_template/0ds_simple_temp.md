# OOP DESIGN QUICK-START TEMPLATE (Python)
**Project:** [Project Name]
**Date:** [Date]

---

## 1. CORE DESIGN PRINCIPLES (Choose 3-5)
[ ] **Single Responsibility** - One reason to change per class
[ ] **Dependency Inversion** - Depend on abstractions (Protocols/ABCs)
[ ] **Composition Over Inheritance** - Favor HAS-A over IS-A
[ ] **Tell, Don't Ask** - Objects manage their own state
[ ] **Encapsulation** - Keep state private, expose behavior
[ ] **Open/Closed** - Extendable without modification

## 2. KEY OBJECTS & RESPONSIBILITIES
| Object | Responsibility | Type (Entity/Service/Value) |
|--------|----------------|------------------------------|
| [Object1] | [What it does] | [Entity/Service/ValueObject] |
| [Object2] | [What it does] | [Entity/Service/ValueObject] |
| [Object3] | [What it does] | [Entity/Service/ValueObject] |

## 3. CLASS SKELETONS
```python
# Value Object (immutable data container)
@dataclass(frozen=True)
class [ValueObjectName]:
    """One-line purpose"""
    attribute1: Type
    attribute2: Type = default_value
    
    def __post_init__(self):
        # Validation logic here
        pass

# Entity (has identity and lifecycle)
class [EntityName]:
    """One-line purpose"""
    
    def __init__(self, id: str, required_dep: Protocol):
        self._id = id  # private
        self._dependency = required_dep
        self._state = "initial"
    
    @property
    def id(self) -> str:
        return self._id
    
    def primary_action(self, param: Type) -> Result:
        """What this entity can do"""
        # Implementation
        pass

# Service (stateless coordinator)
class [ServiceName]:
    """One-line purpose"""
    
    def __init__(self, dep1: Protocol, dep2: Protocol):
        self._dep1 = dep1
        self._dep2 = dep2
    
    def orchestrate(self, entity: Entity) -> Result:
        """Coordinate between dependencies"""
        # Implementation
        pass

# Protocol (interface definition)
class [ProtocolName](Protocol):
    """What implementers must provide"""
    def required_method(self, param: Type) -> Result: ...
```

## 4. RELATIONSHIP DECISIONS
**Composition Pattern:**
```python
# Preferred approach
class MainObject:
    def __init__(self, dependency: Protocol):
        self._dependency = dependency  # HAS-A relationship
```

**Inheritance (only if true IS-A):**
```python
# Only when absolutely necessary
class SpecializedObject(BaseObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add specialized behavior
```

## 5. DEPENDENCY MANAGEMENT
```python
# Constructor injection (preferred)
class Service:
    def __init__(self, repo: RepositoryProtocol):
        self._repo = repo

# Factory function at composition root
def create_application() -> Application:
    return Application(
        service=Service(
            repo=DatabaseRepository()
        )
    )
```

## 6. TESTING APPROACH
```python
# Unit test template
def test_[object]_[behavior]_when_[condition]():
    # Arrange
    mock_dep = Mock(spec=Protocol)
    obj = ObjectUnderTest(mock_dep)
    
    # Act
    result = obj.method(param)
    
    # Assert
    assert result == expected
    mock_dep.method.assert_called_once_with(arg)
```

## 7. CODE QUALITY RULES
- [ ] Classes < 300 lines
- [ ] Methods < 30 lines
- [ ] Max 3 constructor parameters (use dataclass if more)
- [ ] No `isinstance()` checks (use Protocols)
- [ ] Private attributes start with `_`
- [ ] Public methods have type hints
- [ ] No God classes (doing too much)

---

## ONE-PAGE OOP DESIGN CHEATSHEET

### When to Use What:
| Scenario | Solution | Example |
|----------|----------|---------|
| **Data container** | `@dataclass` | `@dataclass UserData: name: str, email: str` |
| **Multiple behaviors** | **Composition** + Protocols | `Printer(renderer: RenderProtocol, formatter: FormatProtocol)` |
| **Family of objects** | **Factory function** | `create_notifier(type: str) -> NotifierProtocol` |
| **Optional features** | **Decorator pattern** | `notifier = LoggingDecorator(EmailNotifier())` |
| **Algorithm variations** | **Strategy pattern** | `Sorter(strategy: SortStrategy)` |
| **State changes** | **State pattern** | `Order().confirm()` → `Order().ship()` |

### Quick Design Checklist:
```python
# BEFORE IMPLEMENTING, ASK:
# 1. Is this class's responsibility single and clear?
# 2. Can I use composition instead of inheritance?
# 3. Are dependencies abstract (Protocols not concrete classes)?
# 4. Is state properly encapsulated (private attributes)?
# 5. Will this be easy to test (inject dependencies)?

# COMMON REFACTORINGS:
# - Large class → Split into multiple classes
# - Long method → Extract helper methods/classes
# - Type checking → Protocol/duck typing
# - Global state → Dependency injection
```

### Template Usage Example:
```python
"""
Simple E-commerce Example
"""

from dataclasses import dataclass
from typing import Protocol

# 1. Define Protocols (abstractions)
class PaymentProcessor(Protocol):
    def charge(self, amount: float) -> bool: ...

class InventoryChecker(Protocol):
    def is_available(self, product_id: str) -> bool: ...

# 2. Value Objects
@dataclass(frozen=True)
class Money:
    amount: float
    currency: str = "USD"

# 3. Entity
class Order:
    def __init__(self, order_id: str, items: list):
        self._id = order_id
        self._items = items
        self._status = "pending"
    
    def calculate_total(self) -> Money:
        total = sum(item.price for item in self._items)
        return Money(total)
    
    def confirm(self):
        self._status = "confirmed"

# 4. Service (coordinator)
class OrderService:
    def __init__(self, 
                 payment: PaymentProcessor,
                 inventory: InventoryChecker):
        self._payment = payment
        self._inventory = inventory
    
    def place_order(self, order: Order) -> bool:
        # Validate
        for item in order._items:
            if not self._inventory.is_available(item.id):
                return False
        
        # Process payment
        total = order.calculate_total()
        if not self._payment.charge(total.amount):
            return False
        
        # Update order
        order.confirm()
        return True

# 5. Composition root
def create_order_service() -> OrderService:
    return OrderService(
        payment=StripeProcessor(),
        inventory=DatabaseInventory()
    )
```

---

## WHEN TO DEVIATE FROM OOP PRINCIPLES

**It's OK to:**
1. **Use simple functions** for pure transformations
2. **Use modules** for related utility functions
3. **Keep simple data** in dicts/lists without classes
4. **Break encapsulation** for performance (document why)
5. **Use procedural code** for simple scripts

**Always document why you deviate:**
```python
# Performance optimization: direct attribute access
# Normally we'd use getters, but this is hot path code
result = obj._cache[key]  # Bypasses encapsulation for performance
```

---

## NEXT STEPS AFTER THIS TEMPLATE

1. **Start with 2-3 core classes**
2. **Add Protocols as you need abstraction**
3. **Refactor when classes grow > 300 lines**
4. **Add tests for each public method**
5. **Review design weekly as system evolves**

**Remember:** Good OOP emerges from refactoring, not upfront perfection. Start simple, make it work, then improve the design.