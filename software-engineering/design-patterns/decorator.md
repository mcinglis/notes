Decorators dynamically add behavior to an object, without affecting other instances of the object's class. They provide a flexible alternative to subclassing for extending functionality.

```java
interface Drawable { void draw(); }

class Window implements Drawable { ... }

class ScrollbarsWindowDecorator implements Drawable {
    ...
    void draw() {
        window.draw();
        /* draw scrollbars */
    }
}

class BordersWindowDecorator implements Drawable {
    ...
    void draw() {
        window.draw();
        /* draw borders */
    }
}
```

Consider implementing the above with subclasses. `ScrollbarsBordersWindow`, anyone?
