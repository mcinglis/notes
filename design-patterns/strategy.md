The strategy pattern allows dynamic selection of behavior.

```java
interface Operator { int evaluate(int a, int b); }

class Adder implements Operator {
    int evaluate(int a, int b) { return a + b; }
}

class Multiplier implements Operator {
    int evaluate(int a, int b) { return a * b; }
}

class Calculator {
    Operator operator;
    int evaluate(int a, int b) { return operator.evaluate(a, b); }
}

main {
    Calculator c = new Calculator();

    c.operator = new Adder();
    System.out.println(">>> " + c.evaluate(5, 6));

    c.operator = new Multiplier();
    System.out.println(">>> " + c.evaluate(4, 9));
}
```
