# Creating and destroying objects

## Item 1: consider static factory methods instead of constructors

A *static factory method* is a static method that returns an instance of the class.

``` java
public static Boolean valueOf(boolean b) {
  return b ? Boolean.TRUE : Boolean.FALSE;
}
```

Advantages of static factory methods, in comparison to constructors:

1. **They have names**, so they're more descriptive, and there can be more than one static factory method with the same signature.
2. **They aren't required to return a new object**, enabling *instance control*.
3. **They can return an object of any subtype of their return type,** offering better flexibility in the API design.

The main disadvantage of providing only static factory methods is that classes without public or protected constructors cannot be subclassed. Also, static factory methods aren't distinguishable from other static methods in documentation.

Below is an example **service provider framework** that uses static factory methods.

``` java
// Service interface
public interface Service {}

// Service provider interface: optional, otherwise, implementations are
// registered by their class name and are then instantiated reflectively.
public interface Provider {
    Service newService();
}

public class Services {
    private Services() {} // Prevents instantiation (item 4)

    private static final Map<String, Provider> providers =
            new ConcurrentHashMap<>();
    public static final String DEFAULT_PROVIDER_NAME = "<default>";

    // Provider registration API
    public static void registerDefaultProvider(Provider p) {
        registerProvider(DEFAULT_PROVIDER_NAME, p);
    }
    public static void registerProvider(String name, Provider p) {
        providers.put(name, p);
    }

    // Service access API
    public static Service newInstance() {
        return newInstance(DEFAULT_PROVIDER_NAME);
    }
    public static Service newInstance(String name) {
        Provider p = providers.get(name);
        if (p == null) {
            throw new IllegalArgumentException(
                    "No provider registered with name: " + name
            );
        }
        return p.newService();
    }
}
```

## Item 2: consider a builder when faced with many constructor parameters

The telescoping constructor pattern works, but it is hard to write client code when there are many parameters, and harder still to read it.

With the JavaBeans pattern, an object may be in an inconsistent state partway through its construction. Also, it precludes making the class immutable.

**The builder pattern combines the safety of telescoping constructors with the readability of JavaBeans constructors.** The builder is a static member class (item 22) of the class it builds.

``` java
public class NutritionFacts {
    private final int servingSize;
    private final int servings;
    private final int calories;
    private final int fat;
    private final int sodium;
    private final int carbohydrate;

    public static class Builder implements Builder<NutritionFacts> {
        // Required parameters
        private final int servingSize;
        private final int servings;

        // Optional parameters, initialized to default values
        private int calories     = 0;
        private int fat          = 0;
        private int sodium       = 0;
        private int carbohydrate = 0;

        public Builder(int servingSize, int servings) {
            this.servingSize = servingSize;
            this.servings = servings;
        }

        public Builder calories(int val) {
            calories = val;
            return this;
        }

        public Builder fat(int val) {
            fat = val;
            return this;
        }

        public Builder sodium(int val) {
            sodium = val;
            return this;
        }

        public Builder carbohydrate(int val) {
            carbohydrate = val;
            return this;
        }

        public NutritionFacts build() {
            return new NutritionFacts(this);
        }
    }

    private NutritionFacts(Builder builder) {
        servingSize  = builder.servingSize;
        servings     = builder.servings;
        calories     = builder.calories;
        fat          = builder.fat;
        sodium       = builder.sodium;
        carbohydrate = builder.carbohydrate;
    }
}
```

The Builder pattern simulates named optional parameters as found in Ada and Python.

The builder's `build` method can check invariants of the parameters. It is critical that they be checked *after* copying the parameters from the builder to the object, and that they be checked on the object fields rather than the builder fields (Item 39). If any invariants are violated, the `build` method should throw an `IllegalStateException` (Item 60). The exception's detail method should indicate which invariant is violated (Item 63).

Builders can have multiple varargs parameters, up to one per setter method.

A single builder can be used to build multiple objects. The builder can be modified between object creations to vary the objects. The builder can fill in some fields automatically, such as a serial number that automatically increases each time an object is created.

Builders that implement the `Builder` generic interface type make excellent abstract factories. Don't use `Class` and `newInstance` for abstract factories, as they break compile-time exception checking.

**The Builder pattern is a good choice when designing classes whose constructors or static factories could have more than a handful of parameters, especially if most of those parameters are optional.**

## Item 3: enforce the singleton property with enums

A *singleton* is a class that is instantiated exactly once. **Making a class a singleton can make it difficult to test its clients,** as it's impossible to substitute a mock implementation for a singleton unless it implements an interface that serves as its type.

As of Java 1.5, a single-element enum type is the best way to implement a singleton.

``` java
public enum Elvis {
  INSTANCE;

  // Methods and state
  public void leaveTheBuilding() {}
}
```

Enums provide the serialization machinery for free, and an ironclad guarantee against multiple instantiation, even in the face of sophisticated serialization or reflection attacks.

## Item 4: enforce noninstantiability with a private constructor

Occasionally you'll want to write a class that is just a grouping of static methods and static fields. Such classes have acquired a bad reputation because some people abuse them to avoid thinking in terms of objects, but they do have valid uses. They can be used to group related methods on primitive values or arrays, in the manner of `java.lang.Math` and `java.util.Arrays`. They can also be used to group static methods, including factory methods, for objects that implement a particular interface, as `java.util.Collections` does. Lastly, they can be used to group methods on a final class, instead of extending the class.

Such *utility classes* were not designed to be instantiated.

In the absence of explicit constructors, however, the compiler provides a public, parameterless *default constructor*. It is not uncommon to see unintentionally instantiable classes in published APIs.

**A class should be made noninstantiable by including a single private constructor**:

``` java
// Noninstantiable utility class
public class UtilityClass {
    // Suppress default constructor for noninstantiability
    private UtilityClass() { throw new AssertionError(); }
}
```

## Item 5: avoid creating unnecessary objects

It often suffices to reuse an object rather than create a new one. Reuse can be faster and more readable. An object can always be reused if it is *immutable* (Item 15).

``` java
// Don't do this! It creates a new String instance every time.
String s = new String("stringette");

// This string will be reused by any other code running in the same VM that
// happens to contain the same string literal.
String s = "stringette";
```

Constructors will always create a new object each time they're called. Thus, `Boolean.valueOf(String)` is almost always preferable to `Boolean(String)`, for example.

In addition to reusing immutable objects, you can also reuse mutable objects.

Here is a more subtle example of what not to do.

``` java
class Person {
    private final Date birthDate;
    // other stuff omitted

    // DON'T DO THIS
    boolean isBabyBoomer() {
        // Unnecessary allocation of expensive objects
        Calendar gmtCal = Calendar.getInstance(TimeZone.getTimeZone("GMT"));
        gmtCal.set(1946, Calendar.JANUARY, 1, 0, 0, 0);
        Date boomStart = gmtCal.getTime();
        gmtCal.set(1965, Calendar.JANUARY, 1, 0, 0, 0);
        Date boomEnd = gmtCal.getTime();
        return birthDate.after(boomStart) && birthDate.before(boomEnd);
    }
}
```

`isBabyBoomer` unnecessarily creates new `Calendar`, `TimeZone` and `Date` instances every time it's invoked.

This version avoids this inefficiency with a static initializer:

``` java
class Person {
    private final Date birthDate;
    // other stuff omitted

    // Starting and ending dates of the baby boom.
    private static final Date BOOM_START;
    private static final Date BOOM_END;

    static {
        Calendar gmtCal = Calendar.getInstance(TimeZone.getTimeZone("GMT"))
        gmtCal.set(1946, Calendar.JANUARY, 1, 0, 0, 0, 0);
        BOOM_START = gmtCal.getTime();
        gmtCal.set(1965, Calendar.JANUARY, 1, 0, 0, 0, 0);
        BOOM_END = gmtCal.getTime();
    }

    public boolean isBabyBoomer() {
        return birthDate.after(BOOM_START) && birthDate.before(BOOM_END);
    }
}
```

### Adapters

An *adapter* (aka *view*) is an object that delegates to a backing object, providing an alternative interface to the backing object. Because an adapter has no state beyond that of its backing object, there's no need to create more than one instance of a given adapter to a given object.

For example, the `keySet` method of the `Map` interface returns a `Set` view of the `Map` object, consisting of all the keys in the map. Calls to `keySet` on a given `Map` object may return the same `Set` object. While it would be harmless to create multiple instances of the `keySet` view object, it is also unnecessary.

### Autoboxing

*Autoboxing* allows the programmer to mix primitive and boxed primitive types, boxing and unboxing automatically as needed. It's a new way to create unnecessary objects.

Consider the following program which calculates the sum of all the positive int values. To do this, the program has to use `long` arithmetic, because an `int` is not big enough to hold the sum of all the positive `int` values.

``` java
// Hideously slow - can you spot the object creation?
public static void main(String[] args) {
    Long sum = 0L;
    for (long i = 0; i < Integer.MAX_VALUE; i++) {
        sum += i;
    }
    System.out.println(sum);
}
```

This program is correct, but it is *much* slower than it needs to be, due to a one-character typographical error. The variable `sum` is declared as a `Long` instead of a `long`, which means the program constructs about 2^31 unnecessary `Long` instances (roughly one for each time the `long i` is added to the the `Long sum`).

**Prefer primitives to boxed primitives, and watch out for unintentional autoboxing.**

### Summary

Creating objects is cheap on modern JVMs. In general, you should always create additional objects if it would enhance the clarity, simplicity or maintainability of a program.

However, avoiding object creation by maintaining your own *object pool* is a bad idea unless the objects in the pool take non-deterministic time to construct.

The counterpoint to this item is Item 39 on *defensive copying*, which says: "Don't reuse an existing object when you should create a new one." The penalty for reusing an object when defensive copying is called for is far greater than the penalty for needlessly creating a duplicate object.

## Item 6: eliminate obsolete object references

Having garbage collection can fool you into not thinking about memory management.

``` java
// Can you spot the memory leak?
class Stack {
    private Object[] elements;
    private int size;
    private static final int INITIAL_CAPACITY = 16;

    public Stack() {
        elements = new Object[INITIAL_CAPACITY];
    }

    public void push(Object e) {
        ensureCapacity();
        elements[size++] = e;
    }

    public Object pop() {
        if (size == 0) {
            throw new EmptyStackException();
        }
        return elements[--size];
    }

    /**
     * Ensure space for at least more element, roughly doubling the capacity
     * each time the array needs to grow.
     */
    private void ensureCapacity() {
        if (elements.length == size) {
            elements = Array.copyOf(elements, 2 * size + 1);
        }
    }
}
```

If this stack grows and then shrinks, the objects that were popped off the stack will not be garbage collected, even if the program using the stack has no more references to them. This is because the stack itself contains obsolete references to these objects.

Memory leaks in GCd languages are insidious. If an object reference is unintentionally retained, then that object and all objects it holds references to (and so on) are also retained. This can have a significant impact on performance.

Memory leaks can remain in a sytem for years. They are typically discovered only as a result of careful code inspection or with the aid of a *heap profiler*. Therefore, it is very desirable to learn to anticipate problems like this before they occur and prevent them from happening.

The fix here is simple: null out references once they become obsolete.

``` java
public Object pop() {
    if (size == 0) {
        throw new EmptyStackException();
    }
    size -= 1;
    Object result = elements[size];
    elements[size] = null;              // Eliminate obsolete reference
    return result;
}
```

An added benefit of nulling out obsolete references is that, if they are subsequently dereferenced by mistake, the program will immediately fail with a `NullPointerException`, rather than quietly doing the wrong thing.

It is always beneficial to detect programming errors as soon as possible.

However, **nulling out object references should be the exception rather than the norm**. The best way to eliminate an obsolete reference is to let the reference fall out of scope. This occurs naturally if you define each variable in the narrowest possible scope.

### Common sources of memory leaks

**Whenever a class manages its own memory, the programmer should be alaert for memory leaks.**

**Caches are a common source of memory leaks**.

Use a `WeakHashMap` to implement a cache if the entries are relevant only so long as there are external references to them.

Otherwise, the cache should occasionally be cleansed of entries that have fallen into disuse. This can be done by a background thread or as a side effect of adding new entries to the cache.

**Listeners and callbacks are another common source of memory leaks.** If you implement an API where clients register callbacks but don't deregister them, they will accumulate unless you take some action. The best way to ensure that callbacks are garbage collected promptly is to store only *weak references* to them, for instance, by storing them only as keys in a *WeakHashMap*.

## Item 7: avoid finalizers

Every class inherits the `finalize()` method from `Object`. The method is called when the JVM determines no more references to the object exist.

**Finalizers are unpredictable, often dangerous, and generally unnecessary.**

**Never do anything time-critical in a finalizer**; there is no guarantee they'll be executed promptly.

**Never depend on a finalizer to update critical persistent state**; there is no guarantee they'll be executed at all.

If an uncaught exception is thrown during finalization, the exception is ignored and finalization of that object terminates.

**There are *severe* performance penalties for using finalizers.**

### What to do instead?

**Provide an *explicit termination method*,** and require clients of the class to invoke the mehtod on each instance when it's no longer needed.

**Explicit termination methods are typically used in combination with the `try-finally` construct to ensure termination.**

``` java
// try-finally block guarantees execution of termination method
Foo foo = new Foo(...);
try {
    // Do what must be done with foo
    ...
} finally {
    foo.terminate();    // Explicit termination method
}
```

### So what are finalizers good for?

Finalizers can act as a "safety net" in case the owner of an object forgets to call its explicit termination method. While there's no guarantee that the finalizer will be invoked prompty, it may be better to free the resource late than never. **The finalizer should log a warning if it finds that the resource has not been terminated**. If you are writing such a safety-net finalizer, think long and hard about whether the extra protection is worth the extra cost.

Finalizers can also be used to reclaim *native peers*, assuming the native peers hold no critical resources.

## Finalizer chaining

If a class has a finalizer and a sublcass overrides it, the subclass finalizer must invoke the superclass' finalizer manually.

``` java
// Manual finalizer chaining
@Override protected void finalize() throws Throwable {
    try {
        ... // Finalize subclass state
    } finally {
        super.finalize();
    }
}
```

It is possible to defend against subclasses forgetting to invoke their superclasses' finalizers with a *finalizer guardian*.

``` java
// Finalizer guardian idiom
public class Foo {
    // Sole purpose of this object is to finalize outer Foo object
    private final Object finalizerGuardian = new Object() {
        @Override protected foo finalize() throws Throwable {
            ... // finalize outer Foo object
        }
    }
    ...  // remainder omitted
}
```

The finalizer guardian will become eligible for finalization at the same time as the enclosing instance.

`Foo` has no finalizer, so it doesn't matter whether a subclass finalizer calls `super.finalize` or not.

This technique should be considered for every nonfinal public class that has a finalizer.
