# Inheritance

## Writing final classes and methods

A `final` method cannot be overridden by subclasses. The `Object` class does this; a number of its methods are `final`. Methods called from constructors should generally be declared final. If a constructor calls a non-final method, surprising behavior would occur if a subclass redefines that method.

A `final` class cannot be subclassed. The `String` class does this.
