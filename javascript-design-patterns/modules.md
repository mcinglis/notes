# Modules

Modules are an integral piece of any robust application's architecture. They help in keeping the code for a project organized and protected, and limiting namespace pollution.

## The module pattern

The module pattern protects variables from leaking into the global scope and colliding with other interfaces. Only an explicity exported interface is returned, keeping everything else within the module private.

```javascript
var counter = (function() {
    var counter = 0;
    return {
        value: function() {
            return counter;
        },
        increment: function() {
            // Makes use of an exported function
            return counter = this.value() + 1;
        },
        reset: function() {
            return counter = 0;
        }
    };
})();
```

### Disadvantages

Because private and public members are accessed differently, changing visibility of a member requires changing all references to that member.

Functions that are added to the module later can't access private members.

Automated unit tests can't be created for private variables.

Disables bug hot-fixing in a module (by patching its properties).

## The revealing module pattern

The revealing module pattern was born out of the frustration of having to repeat the name of the main object when you wanted to call one public method from another or access public variables.

```javascript
var counter = (function() {
    var counter = 0;
    var value = function() {
        return counter;
    };
    var increment = function() {
        return counter = value() + 1;
    };
    var reset = function() {
        return counter = 0;
    };
    return {
        value: value,
        increment: increment,
        reset: reset
    };
})();

counter.increment();
```

### Disadvantages

Patching exported properties will not fix private implementations.

Only objects can be exported due to pass-by-value rules.

### Advantages

A member's visibility doesn't affect internal code that refers to it.

Members can be exported with names different to their internal names.
