# OBJECT-ORIENTED DESIGN PRINCIPLES TEMPLATE (Python Edition)
**System:** [System Name]
**Version:** [Version]
**Date:** [Date]

---

## 1. DESIGN PHILOSOPHY
**Core Philosophy:** [Guiding design approach, e.g., "Explicit over implicit, composition over inheritance"]
**Primary Goals:**
- [Goal 1: e.g., "Readability and maintainability through clear abstractions"]
- [Goal 2: e.g., "Duck typing with protocol-based interfaces"]
- [Goal 3: e.g., "Testability through dependency injection and mocking"]

**Python-Specific Principles:**
- **EAFP (Easier to Ask for Forgiveness than Permission):** Try first, handle exceptions
- **Duck Typing:** Focus on behavior, not type
- **Pythonic Design:** Follow PEP 8, use built-in protocols

## 2. CORE PRINCIPLES APPLIED
### SOLID Principles in Python
| Principle | Python Interpretation | Application Rules | Code Smells Violating It |
|-----------|----------------------|-------------------|---------------------------|
| **S - Single Responsibility** | "A class/module should have one reason to change" | • Use `@dataclass` for data-only classes<br>• Separate business logic from I/O<br>• Use composition to split responsibilities | • Classes with 500+ lines<br>• Mixing domain logic with database/API calls<br>• Classes with "Manager", "Handler", "Processor" in name doing everything |
| **O - Open/Closed** | "Open for extension via composition, closed for modification" | • Use ABCs (Abstract Base Classes) for interfaces<br>• Protocol classes for structural subtyping<br>• Function composition and decorators | • Large `if/elif` chains checking types<br>• Modifying core classes to add features<br>• Monkey patching instead of proper extension |
| **L - Liskov Substitution** | "Subtypes must be substitutable via duck typing" | • Follow protocol/interface contracts<br>• Don't change method signatures in incompatible ways<br>• Use `isinstance()` sparingly | • Subclass that raises `NotImplementedError`<br>• Override that changes return type significantly<br>• Violating method preconditions/postconditions |
| **I - Interface Segregation** | "Many specific protocols better than one large interface" | • Use `typing.Protocol` for role interfaces<br>• Keep ABCs small and focused<br>• Mixins for cross-cutting concerns | • ABC with 10+ abstract methods<br>• Classes implementing empty `pass` methods<br>• "God interface" that does everything |
| **D - Dependency Inversion** | "Depend on abstractions (Protocols/ABCs), not concretions" | • Type hints with Protocols/ABCs<br>• Dependency injection via constructor<br>• Use `__init__` for required dependencies | • Direct instantiation (`Class()`) in business logic<br>• Hard-coded imports of concrete implementations<br>• Global state/singletons as dependencies |

### Python-Specific Principles
**Composition Over Inheritance:**
```python
# Prefer this:
class Engine:
    def start(self): ...

class Car:
    def __init__(self):
        self.engine = Engine()
    
    def start(self):
        self.engine.start()

# Over this:
class Vehicle:
    def start(self): ...

class Car(Vehicle):  # What if Car needs multiple behaviors?
    pass
```

**Duck Typing with Protocols:**
```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class Flyable(Protocol):
    def fly(self) -> None: ...

def make_it_fly(obj: Flyable):
    obj.fly()  # Works with any object having .fly() method
```

**EAFP (Easier to Ask Forgiveness than Permission):**
```python
# Instead of:
if hasattr(obj, 'method'):
    obj.method()
# Prefer:
try:
    obj.method()
except AttributeError:
    handle_missing_method()
```

## 3. PYTHON OBJECT DESIGN PATTERNS
### Creational Patterns
| Pattern | Python Implementation | When to Use |
|---------|----------------------|-------------|
| **Factory Method** | Class method or module-level function | When subclass decides object creation |
| **Abstract Factory** | ABC with factory methods, dict of factories | Families of related objects |
| **Builder** | Fluent interface with `__call__` or separate Builder class | Complex object construction with many parameters |
| **Singleton** | Module-level instance, `__new__` method, or metaclass | True single instances (rarely needed in Python) |
| **Prototype** | `copy.deepcopy()` or custom `clone()` method | Creating objects by cloning existing ones |

### Pythonic Structural Patterns
```python
# Adapter using __getattr__
class LegacyAdapter:
    def __init__(self, legacy_obj):
        self._legacy = legacy_obj
    
    def __getattr__(self, name):
        # Forward unknown attributes to legacy object
        return getattr(self._legacy, name)

# Decorator using functools.wraps
from functools import wraps

def logger_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# Facade as a module
# facade.py simplifies complex subsystem
```

### Behavioral Patterns in Python
```python
# Strategy Pattern with functions (first-class citizens)
def bubble_sort(data):
    # implementation
    return sorted_data

def quick_sort(data):
    # implementation
    return sorted_data

class Sorter:
    def __init__(self, strategy=bubble_sort):
        self.strategy = strategy
    
    def sort(self, data):
        return self.strategy(data)

# Observer with events
from typing import Callable, List

class Observable:
    def __init__(self):
        self._observers: List[Callable] = []
    
    def attach(self, observer: Callable):
        self._observers.append(observer)
    
    def notify(self, *args, **kwargs):
        for observer in self._observers:
            observer(*args, **kwargs)
```

## 4. CLASS DESIGN TEMPLATE
### For Each Major Class:
```python
"""
[ClassName]
Responsibility: [Single sentence]

Design Decisions:
- Encapsulation: [Private (_name) vs protected (__name) vs public]
- Immutability: [@dataclass(frozen=True) or read-only properties]
- Composition: [What objects this composes]
- Protocols: [What protocols/ABCs this implements]
"""

from typing import Protocol, Optional
from dataclasses import dataclass, field
from abc import ABC, abstractmethod

class DependencyProtocol(Protocol):
    """Protocol for dependencies"""
    def do_something(self) -> str: ...

@dataclass
class ClassName:
    """One-line docstring describing purpose."""
    
    # Required dependencies (injected)
    dependency: DependencyProtocol
    # Optional with default
    config: dict = field(default_factory=dict)
    # Private attribute
    _internal_state: int = field(default=0, init=False)
    
    @property
    def state(self) -> int:
        """Read-only property for external access."""
        return self._internal_state
    
    def primary_action(self, param: str) -> str:
        """Perform the class's main responsibility.
        
        Args:
            param: Description of parameter
            
        Returns:
            Description of return value
            
        Raises:
            ValueError: If param is invalid
        """
        if not param:
            raise ValueError("param cannot be empty")
        
        result = self.dependency.do_something()
        self._internal_state += 1
        return f"{result}: {param}"
    
    def __str__(self) -> str:
        """User-friendly string representation."""
        return f"ClassName(state={self._internal_state})"
```

## 5. RELATIONSHIP GUIDELINES
### Inheritance Decision Tree
```python
# Ask these questions:
# 1. Is it truly an "is-a" relationship?
# 2. Will you need multiple inheritance? (Python supports it)
# 3. Are you just reusing code? (Use composition instead)

# Good inheritance example:
class Animal(ABC):
    @abstractmethod
    def make_sound(self) -> str: ...

class Dog(Animal):
    def make_sound(self) -> str:
        return "Woof!"

# Bad inheritance example:
class LoggerMixin:  # Mixin for code reuse - often better as composition
    def log(self, message):
        print(f"{self.__class__.__name__}: {message}")
```

### Dependency Injection in Python
```python
# Constructor injection (preferred)
class Service:
    def __init__(self, repository: RepositoryProtocol, config: Config):
        self._repo = repository
        self._config = config
    
    def operation(self):
        return self._repo.get_data()

# Property injection (for optional dependencies)
class Service:
    def __init__(self):
        self._cache: Optional[CacheProtocol] = None
    
    @property
    def cache(self) -> CacheProtocol:
        if self._cache is None:
            self._cache = DefaultCache()
        return self._cache
    
    @cache.setter
    def cache(self, value: CacheProtocol):
        self._cache = value

# Using dependency injection frameworks
# pip install injector, django, fastapi, etc.
```

## 6. PYTHON CODE QUALITY METRICS
### Object-Oriented Metrics for Python
| Metric | Target | Tool | Purpose |
|--------|--------|------|---------|
| **Class Length** | < 300 lines | pylint, flake8 | Single Responsibility |
| **Method Length** | < 30 lines | radon | Method complexity |
| **Cyclomatic Complexity** | < 10 per method | mccabe | Control flow complexity |
| **LCOM (Lack of Cohesion)** | < 4 | radon | Class cohesion |
| **DIT (Depth of Inheritance)** | 1-3 | pylint | Inheritance depth control |

### Python-Specific Design Rules
```python
# Use these linter configurations:
# .pylintrc
[DESIGN]
max-args=5
max-locals=15
max-returns=6
max-branches=12
max-statements=50
max-parents=3  # Inheritance depth
max-attributes=10

# .flake8
max-complexity = 10
max-line-length = 88  # Black's default
```

## 7. PYTHON REFACTORING CATALOG
### Common Python OOP Refactorings
**Large Class → Extract Class:**
```python
# Before:
class UserManager:
    def __init__(self):
        self.users = []
    
    def add_user(self, user): ...
    def remove_user(self, user): ...
    def validate_email(self, email): ...  # Should be in Validator
    def send_welcome_email(self, user): ...  # Should be in Notifier
    def save_to_db(self, user): ...  # Should be in Repository

# After:
class UserValidator:
    def validate_email(self, email): ...

class UserNotifier:
    def send_welcome_email(self, user): ...

class UserRepository:
    def save(self, user): ...

class UserService:  # Coordinating class
    def __init__(self, validator, notifier, repository):
        self.validator = validator
        self.notifier = notifier
        self.repository = repository
```

**Long Parameter List → Parameter Object:**
```python
# Before:
def create_user(name, email, password, age, address, phone, role):
    ...

# After:
@dataclass
class UserData:
    name: str
    email: str
    password: str
    age: int
    address: str
    phone: str
    role: str

def create_user(data: UserData):
    ...
```

**Conditional Logic → Strategy Pattern:**
```python
# Before:
def calculate_shipping(order, customer_type):
    if customer_type == "premium":
        return 0
    elif customer_type == "regular":
        return 5
    elif customer_type == "international":
        return 20
    else:
        return 10

# After:
from typing import Protocol

class ShippingStrategy(Protocol):
    def calculate(self, order) -> float: ...

class PremiumShipping:
    def calculate(self, order) -> float:
        return 0

class RegularShipping:
    def calculate(self, order) -> float:
        return 5

class ShippingCalculator:
    def __init__(self, strategy: ShippingStrategy):
        self.strategy = strategy
    
    def calculate(self, order):
        return self.strategy.calculate(order)
```

## 8. PYTHON TESTING STRATEGY
### OOP-Specific Testing in Python
```python
import pytest
from unittest.mock import Mock, MagicMock, patch
from typing import Protocol

# Test using protocols/interfaces
class DatabaseProtocol(Protocol):
    def save(self, data) -> bool: ...

def test_service_saves_data():
    # Arrange
    mock_db = Mock(spec=DatabaseProtocol)
    service = Service(mock_db)
    
    # Act
    result = service.process("test")
    
    # Assert
    mock_db.save.assert_called_once_with("processed: test")
    assert result is True

# Property-based testing with hypothesis
from hypothesis import given, strategies as st

@given(st.text(min_size=1))
def test_user_creation(name):
    user = User(name=name)
    assert user.name == name
    assert user.id is not None

# Testing with dependency injection
def test_with_real_dependencies():
    # Use real implementations for integration tests
    repo = RealRepository()
    service = Service(repo)
    # ...

def test_with_mocked_dependencies():
    # Use mocks for unit tests
    repo = Mock()
    service = Service(repo)
    # ...
```

## 9. PYTHON-SPECIFIC BEST PRACTICES
### Magic Methods Usage
```python
class Vector:
    """Example of proper magic method usage."""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Required for collections
    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    # For arithmetic operations
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    # For string representation
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __str__(self):
        return f"({self.x}, {self.y})"
```

### Context Managers for Resource Management
```python
from contextlib import contextmanager
from typing import Iterator

class DatabaseConnection:
    def __enter__(self):
        self.connect()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()
    
    def connect(self): ...
    def disconnect(self): ...

# Usage
with DatabaseConnection() as db:
    db.query("SELECT ...")

# Or as a decorator
@contextmanager
def temporary_config(config: dict) -> Iterator[None]:
    old_config = get_config()
    set_config(config)
    try:
        yield
    finally:
        set_config(old_config)
```

## 10. DESIGN REVIEW CHECKLIST (Python)
### Pre-Implementation Review
- [ ] Does the class have a single, clear responsibility?
- [ ] Are dependencies injected and typed with Protocols/ABCs?
- [ ] Is inheritance truly necessary, or would composition work better?
- [ ] Are there Pythonic alternatives (functions, decorators, generators)?
- [ ] Are magic methods implemented correctly and consistently?
- [ ] Is state properly encapsulated (prefix with `_` for private)?
- [ ] Are objects immutable where possible (`frozen=True`)?

### Python-Specific Code Review
- [ ] EAFP used instead of LBYL where appropriate?
- [ ] Duck typing with Protocols instead of `isinstance()` checks?
- [ ] Proper use of `@property`, `@classmethod`, `@staticmethod`?
- [ ] Context managers for resource management?
- [ ] Type hints for public interfaces?
- [ ] Follows PEP 8 and project-specific conventions?

---

## QUICK REFERENCE CARD (Python)
### Python OOP Design Rules
```python
1. Classes < 300 lines, Methods < 30 lines
2. Use @dataclass for data containers
3. Depend on Protocols, not concrete classes
4. Composition over inheritance (especially multiple inheritance)
5. Make objects immutable with frozen=True where possible
6. Use dependency injection (constructor args)
7. Protocol-based duck typing over isinstance()
8. EAFP over LBYL for expected failures
9. Context managers for cleanup
10. Type hints for public APIs
```

### Python Code Smells → Refactoring
```python
# Large Class → Extract Class, use composition
# Long Method → Extract Method, use helper functions
# Primitive Obsession → Create Value Objects (@dataclass)
# Switch Statements → Strategy Pattern with dict of functions
# Feature Envy → Move Method to appropriate class
# Message Chains → Law of Demeter, create Facade/Adapter
# Temporary Field → Introduce Parameter Object
```

---

## EXAMPLE: ORDER PROCESSING SYSTEM (Python)
```python
"""
OOP Principles applied in Python
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Protocol, List
from datetime import datetime

# Protocols for dependency inversion
class RepositoryProtocol(Protocol):
    def save(self, entity) -> None: ...
    def find_by_id(self, id) -> object: ...

class ValidatorProtocol(Protocol):
    def validate(self, data) -> bool: ...

# Value Objects (immutable data)
@dataclass(frozen=True)
class Money:
    amount: float
    currency: str = "USD"
    
    def __post_init__(self):
        if self.amount < 0:
            raise ValueError("Amount cannot be negative")

# Entity with identity
class Order:
    def __init__(self, order_id: str, customer_id: str):
        self._id = order_id
        self._customer_id = customer_id
        self._items: List[OrderItem] = []
        self._status = "PENDING"
    
    @property
    def id(self) -> str:
        return self._id
    
    @property
    def status(self) -> str:
        return self._status
    
    def add_item(self, product_id: str, quantity: int, price: Money):
        """Tell, don't ask: Order manages its own items."""
        item = OrderItem(product_id, quantity, price)
        self._items.append(item)
    
    def calculate_total(self) -> Money:
        """SRP: Order calculates its own total."""
        total = sum(item.price.amount * item.quantity for item in self._items)
        return Money(total)
    
    def confirm(self):
        """State transition managed by Order."""
        if self._status != "PENDING":
            raise ValueError(f"Cannot confirm from {self._status}")
        self._status = "CONFIRMED"

# Service with injected dependencies
class OrderService:
    def __init__(
        self,
        repository: RepositoryProtocol,
        validator: ValidatorProtocol,
        notifier: "NotificationProtocol"
    ):
        self._repo = repository
        self._validator = validator
        self._notifier = notifier
    
    def place_order(self, order: Order) -> bool:
        """Coordinator that delegates to specialists."""
        if not self._validator.validate(order):
            return False
        
        # Order manages its own state transition
        order.confirm()
        
        # Repository handles persistence
        self._repo.save(order)
        
        # Notifier handles communication
        self._notifier.send_confirmation(order)
        
        return True

# Using Protocols for flexible design
class NotificationProtocol(Protocol):
    def send_confirmation(self, order: Order) -> None: ...

class EmailNotifier:
    def send_confirmation(self, order: Order) -> None:
        print(f"Email sent for order {order.id}")

# Factory function (not method)
def create_order_service() -> OrderService:
    """Dependency injection at composition root."""
    return OrderService(
        repository=SqlRepository(),
        validator=OrderValidator(),
        notifier=EmailNotifier()
    )
```

---

## TEMPLATE USAGE NOTES (Python-Specific)

1. **Start Simple:** Python allows progressive complexity - start with functions, then classes if needed
2. **Use Python Features:** Decorators, context managers, generators can often replace complex OOP patterns
3. **Protocols over ABCs:** `typing.Protocol` is often more flexible than ABC for duck typing
4. **Type Hints:** Use them for public APIs and complex interfaces
5. **Testability:** Python's dynamic nature makes testing easier - use it to your advantage
6. **Batteries Included:** Check standard library (`collections.abc`, `contextlib`, `dataclasses`) before building custom solutions

**Remember:** Python is multi-paradigm. Use OOP when it makes the code clearer and more maintainable, not because "it's OOP." Sometimes a simple function or module is the right solution.