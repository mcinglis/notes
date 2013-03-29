# Methods common to all objects

## Item 8: obey the general contract when overriding `equals`

The easiest way to avoid problems with overriding `equals` is to not do it, in which case, each instance of the class is equal only to itself.

Don't override `equals` if:

* each instance of the class is inherently unique
* you don't care whether the class provides a "logical equality" test
* a superclass has already overridden `equals`, and the superclass behavior is appropriate for this class

Arguably, if the class is private or package-private, and you are certain that its `equals` method will never be invoked, you should override it with something like:

``` java
@Override public boolean equals(Object o) {
    throw new AssertionError();         // Method is never called
}
```

It's appropriate to override `equals` when the class has a notion of *logical equality* that differs from mere object identity, and a superclass hasn't overriden `equals` to implement the desired behavior.

This is generally the case for **value classes**, like `Integer` and `Date`.

However, some value classes use *instance control* (Item 1) to ensure that at most one object exists with each value. In that case, logical equality is the same as object identity and so `equals` needn't be overridden. Enum types (Item 30) use this technique.

### The contract of `equals`

The `equals` method implements an *equivalence relation*. It is:

* **reflexive**: for any non-null `x`, `x.equals(x)` returns `true`
* **symmetric**: for any non-null `x` and `y`, `x.equals(y)` returns `true` if and only if `y.equals(x)` returns true
* **transitive**: for any non-null `x`, `y` and `z`, if `x.equals(y)` returns true and `y.equals(z)` returns true, then `x.equals(z)` returns true
* **consistent**: for any non-null `x` and `y`, `x.equals(y)` consistently returns `true` or `false`, provided no information used in `equals` comparisons on the objects is modified
* for any non-null `x`, `x.equals(null)` must return `false`

**If you violate the `equals` contract, you simply don't know how other objects will behave when confronted with your object.**

There is a fundamental problem of equivalence relations in object-oriented languages. **There is no way to extend an instantiable class and add a value component while preserving the `equals` contract.**

**Don't write an `equals` method that depends on unreliable resources.**

### The recipe for a high-quality `equals`

#### 1. Use `==` to check if the argument is a reference to this object, and if so, return `true`

This is just a performance optimization.

#### 2. Use `instanceof` to check that the argument has the correct type, and if not, return `false`

Typically, the correct type is the class that the `equals` method is being written for, but it could also be an interface implemented by the class.

#### 3. Cast the argument to the correct type

Because the cast was preceded by an `instanceof` test, it's guaranteed to succeed.

#### 4. Check the equality of "significant" properties

For primitive fields that aren't a `float` or `double`, use `==`; for objects, invoke their `equals` method; for `float` fields, use `Float.compare`; for `double` fields, use `Double.compare`. If every element of an array field is significant, use `Arrays.equals`.

To avoid `NullPointerException`s when comparing objects:

``` java
(field == null ? o.field == null : field.equals(o.field))
# Or, this might be faster if the fields are often identical
(field == o.field || (field != null && field.equals(o.field))
```

#### 5. Write tests for the symmetricity, transitivity and consistency properties

### Final caveats

* **always override `hashCode` when you override `equals` (Item 9)**
* **don't be tricky when defining equivalence**
* **don't substitute another type for `Object` in the `equals` signature

## Item 9: always override `hashCode` when you override `equals`


