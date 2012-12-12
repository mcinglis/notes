Decorators dynamically add behavior to an object, without affecting other instances of the object's class. They provide a flexible alternative to subclassing for extending functionality.

```java
interface Drink { double cost(); String name(); }

class Coffee implements Drink {
    double cost() { return 1; }
    String name() { return "coffee"; }
}

abstract class IngredientDecorator implements Drink {
    Drink drink;
    IngredientDecorator(Drink d) { drink = d; }
    abstract void 
    double cost() { return drink.cost() + cost() }
}

class Milk {
    Drink drink;
    Milk(Drink d) { drink = d; }
    double cost() { return drink.cost() + 0.5; }
    String name() { return drink.ingredients() + ", milk"; }
}

```
