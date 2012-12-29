A facade is an object that provides a simplified interface to a more complex one. A facade can:

* make a software library easier to use, understand and test, since the facade has convenient methods for common tasks
* make the library more readable, for the same reason
* reduce dependencies of outside code on the inner workings of a library, since most code uses the facade, thus allowing more flexibility in developing the system
* wrap a poorly-designed collection of interfaces with a single well-designed interface, according to the task's needs

## Example facade

```javascript
var addEvent = function (element, event, handler) {
  if (element.addEventListener)
    element.addEventListener(event, handler, false);
  else if (element.attachEvent)
    element.attachEvent('on' + event, handler);
  else
    element['on' + event] = handler;
};
```

## `$(document).ready(...)` facade

In jQuery, this is actually being powered by a method called `bindReady()`, which is implemented as such:

```javascript
bindReady: function () {
  ...
  if (document.addEventListener) {
    document.addEventListener('DOMContentLoaded', DOMContentLoaded, false);
    window.addEventListener('load', jQuery.ready, false);

  // If IE event model is used
  } else if (document.attachEvent) {
    document.attachEvent('onreadystatechange', DOMContentLoaded);
    window.attachEvent('onload', jQuery.ready);
  }
  ...
}
```

## Integration with module pattern

```javascript
var module = (function () {
  var _private = {
    i: 5,
    get: function () {
      console.log('current value:' + this.i);
    },
    set: function (val) {
      this.i = val;
    },
    run: function () {
      console.log('running');
    },
    jump: function () {
      console.log('jumping');
    }
  };

  return {
    facade: function (args) {
      _private.set(args.val)
      _private.get();
      if (args.run)
        _private.run();
    }
  };
}());
```

With this, clients of the module can interact with it with expressions like:

```javascript
// Outputs: 'current value: 10' and 'running'
module.facade({ run: true, val: 10 });
```

## Disadvantages


