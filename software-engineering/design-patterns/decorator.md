Decorators dynamically add behavior to an object, without affecting other instances of the object's class. They provide a flexible alternative to subclassing for extending functionality.

```java
interface Drawable { void draw(); }

class Window implements Drawable { ... }

class ScrollbarsDecorator implements Drawable {
    Drawable drawable;

    ScrollbarsDecorator(Drawable drawable) {
        this.drawable = drawable;
    }

    void draw() {
        drawable.draw();
        // draw scrollbars
    }
}

class BordersDecorator implements Drawable {
    Drawable drawable;

    BordersDecorator(Drawable drawable) {
        this.drawable = drawable;
    }

    void draw() {
        drawable.draw();
        // draw borders
    }
}

public class Example {
  public static void main(String[] args) {
    Drawable window = new Window();
    Drawable withBorders = new BordersDecorator(new Window());
    Drawable withScrollbars = new ScrollbarsDecorator(new Window());
    Drawable withBoth = new BordersDecorator(
                        new ScrollbarsDecorator(new Window()));
  }
}
```

Consider implementing the above with subclasses. `ScrollbarsBordersWindow`, anyone?
