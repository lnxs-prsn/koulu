Quiz: Object-Oriented Programming - Pattern Recognition
Instructions: For each task, read the description and select the option that best describes the OOP principles and patterns most directly applied or illustrated in the proposed solution.

Question 1

Read the task:

"Design a simple system for a library. There is a base LibraryItem class with common properties like title, author, and id. We need specific types for Book (has numPages) and DVD (has durationMinutes). All item types must have a getDescription() method, but the format of the description differs per type."

Which combination of OOP principles is the primary foundation for this design?

A) Encapsulation + Abstraction → Data hiding is used, and complex reality is reduced to essential features.
B) Inheritance + Polymorphism → A hierarchy is established to share common code, while allowing subclasses to provide specific implementations.
C) Composition + Abstraction → Objects are built from others, and a simplified interface is presented.
D) Polymorphism + Encapsulation → Methods behave differently based on the object, and internal state is protected.
E) I don’t know.

Question 2

Read the task:

"You are modeling a BankAccount class. The internal balance must not be directly accessible. It can only be modified through methods like deposit(amount) and withdraw(amount), which include validation (e.g., no negative deposits, no overdrafts beyond a limit)."

Which principle is this most strongly enforcing, and what common pattern is used to achieve it?

A) Polymorphism → Strategy Pattern → Different accounts can have different withdrawal behaviors.
B) Abstraction → Facade Pattern → A simple interface hides the complex banking system.
C) Encapsulation → Accessors/Mutators with Validation → State is protected and changed only through controlled channels.
D) Inheritance → Template Method → A base class defines the skeleton of the transaction process.
E) I don’t know.

Question 3

Read the task:

"We have a Shape interface with a single method calculateArea(). We have the classes Circle, Square, and Triangle that implement this interface. A Drawing class has a method totalArea(shapes) that sums the area of all shapes in a list, calling calculateArea() on each one without knowing its concrete type."

This is a classic demonstration of which principle, enabling which powerful design benefit?

A) Inheritance → Code Reuse -> Circle and Square reuse code from a common ancestor.
B) Polymorphism → Extensibility -> New shapes (e.g., Pentagon) can be added without modifying Drawing.totalArea().
C) Encapsulation → Maintainability -> The area calculation logic is neatly contained within each shape.
D) Abstraction → Simplification -> The Shape interface reduces a shape to its area-calculating capability.
E) I don’t know.

Question 4

Read the task:

"A Car class is built. Instead of inheriting from a Engine class, it has a private engine property that is an instance of an Engine class. The Car delegates starting operations to engine.start(). Similarly, it has wheels (a list of Wheel objects)."

What principle is being prioritized over inheritance here, and what is the key relationship?

A) Polymorphism → "Is-a" relationship -> A Car is a type of Engine.
B) Abstraction → "Implements" relationship -> The Car provides a simplified interface to a complex system.
C) Encapsulation → "Has-a" relationship -> The Car's internal components are hidden and protected.
D) Composition → "Has-a" relationship -> The Car is composed of, or owns, other objects (Engine, Wheels).
E) I don’t know.

Answer Key (For you, not the quiz-taker):

B) Inheritance + Polymorphism -> This is the core of creating a hierarchy with shared interface but different implementations.

C) Encapsulation → Accessors/Mutators with Validation -> The task is a textbook definition of encapsulation.

B) Polymorphism → Extensibility -> The "Open/Closed Principle" (open for extension, closed for modification) is enabled by polymorphism.

D) Composition → "Has-a" relationship -> This describes favoring composition ("has-a") over inheritance ("is-a").

How does this align with your example's style?

Each question starts with a concrete task.

It asks for the principles/patterns used, not the code.

Options mix principles and patterns in plausible ways.

"I don't know" is an option.

Would you like me to adjust the difficulty, add more questions on specific concepts (like SOLID principles), or change the wording of the tasks?