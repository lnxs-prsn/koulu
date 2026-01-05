I want you to provide me quizes like below are you able to do it ?

🔧 **SOLID Quiz: Task-Centered Design Challenges (Round 2)**

---

**Question 1**  
You’re building a file processor for a data pipeline. The `DataExporter` class currently supports only CSV:

```python
class DataExporter:
    def export(self, data, filename):
        with open(f"{filename}.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerows(data)
```

Later, your team needs JSON and XML exports. Instead of modifying `DataExporter`, you’re told:  
> “Don’t touch existing code—just make it work with new formats.”

You refactor by defining:

```python
class Exporter(ABC):
    @abstractmethod
    def export(self, data, filename): ...

class CsvExporter(Exporter): ...
class JsonExporter(Exporter): ...
class XmlExporter(Exporter): ...

class DataPipeline:
    def __init__(self, exporter: Exporter):
        self.exporter = exporter
```

Which **two** SOLID principles does this design best embody?

A) Single Responsibility + Liskov Substitution  
B) Open/Closed + Dependency Inversion  
C) Interface Segregation + Single Responsibility  
D) Liskov Substitution + Open/Closed  
E) I don’t know.

💡 **Think**: Can you add new formats without changing `DataPipeline`? And what does `DataPipeline` depend on?

---

**Question 2**  
You create a `Bird` class with a `fly()` method. Then you implement `Eagle` and `Penguin` as subclasses:

```python
class Bird:
    def fly(self):
        print("Flying high!")

class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("Penguins can't fly!")
```

Later, this code breaks:

```python
def migrate_birds(birds: list[Bird]):
    for bird in birds:
        bird.fly()  # ← Raises error for Penguin!
```

Which SOLID principle is violated?

A) Single Responsibility – `Bird` mixes flying with identity.  
B) Open/Closed – You had to override behavior.  
C) Liskov Substitution – `Penguin` isn’t a valid substitute for `Bird`.  
D) Interface Segregation – `Bird` forces unnecessary methods.  
E) I don’t know.

💡 **Think**: If a subclass can’t fulfill the contract of its parent, what’s at risk?

---

**Question 3**  
You design a `PaymentService` that handles credit cards, PayPal, and bank transfers. To avoid code duplication, you create one giant `process_payment()` method with a chain of `if/elif` checks:

```python
def process_payment(self, method, amount):
    if method == "credit_card":
        # 20 lines of CC logic
    elif method == "paypal":
        # 18 lines of PayPal logic
    elif method == "bank_transfer":
        # 22 lines of bank logic
```

Every time finance adds a new method (e.g., “crypto”), you edit this method.  
Which principle is most clearly ignored?

A) Dependency Inversion – it uses concrete logic, not abstractions.  
B) Single Responsibility – this method has many reasons to change.  
C) Open/Closed – it’s not open for extension.  
D) Liskov Substitution – payment types aren’t substitutable.  
E) I don’t know.

💡 **Think**: How many different payment providers might ask you to change this one method?

---

**Question 4**  
You define a `Worker` interface for a task queue:

```python
class Worker(ABC):
    @abstractmethod
    def work(self): ...
    @abstractmethod
    def take_lunch_break(self): ...
    @abstractmethod
    def attend_meeting(self): ...
```

But your `AutomatedBot` class—meant to run 24/7—must implement `take_lunch_break()` and `attend_meeting()`, even though it never does those things. You fill them with `pass` or dummy logs.

Which principle is violated?

A) Single Responsibility – `Worker` is doing too much.  
B) Interface Segregation – clients depend on methods they don’t use.  
C) Dependency Inversion – `AutomatedBot` depends on human-centric abstractions.  
D) Liskov Substitution – bots aren’t “real” workers.  
E) I don’t know.

💡 **Think**: Should a non-human worker be forced to pretend it takes coffee breaks?

---

**Question 5**  
You’re told:  
> “Our logging system must support file, console, and cloud logging. But the core app shouldn’t care which one is used—and we shouldn’t rewrite it when adding new log targets.”

You design:

```python
class Logger(ABC):
    @abstractmethod
    def log(self, message): ...

class FileLogger(Logger): ...
class ConsoleLogger(Logger): ...
class CloudLogger(Logger): ...

class Application:
    def __init__(self, logger: Logger):
        self.logger = logger
```

Now, switching loggers only requires changing the injection point—not `Application`.

Which principle is **most directly** satisfied?

A) Single Responsibility  
B) Open/Closed  
C) Liskov Substitution  
D) Dependency Inversion  
E) I don’t know.

💡 **Think**: Is `Application` depending on a concrete logger or an abstraction?