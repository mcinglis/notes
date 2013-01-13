# SOLID

SOLID is an acronym that represents the five basic principles of object-oriented programming and design. They encourage maintainability and extensibility.

## Single responsibility principle

Every class should have a single responsibility, and that responsibility should be entirely encapsulated by the class. All its services should be narrowly aligned with that responsibility.

## Open/closed principle

Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification. Abstracted interfaces should be used, allowing multiple implementations to be polymorphically substituted for one another.

## Liskov substitution principle

All properties provable of objects of a type T should also be provable for objects of subtypes of T.

## Interface segregation principle

Provide small interfaces suited to a specific role.

## Dependency inversion principle

1. High-level modules should not depend on low-level modules. Both should depend on abstractions.
2. Abstractions should not depend on details. Details should depend on abstractions.

If A depends on B, then an indirection interface should be created for A that B implements.
