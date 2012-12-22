The singleton pattern restricts instantiation of a class to a single object.

In Javascript, singletons serve as a namespace that protects the global namespace from implemented variables, and provides a single point of access for functions.

The simplest form of a singleton in Javascript is an object literal.

```javascript
var singleton = {
  property1: 'some value',

  method1: function () {
    console.log('hello world');
  }
};
```

If you wished to extend this further, you could add your own private members and methods to the singleton by encapsulating variable and function delcarations inside a closure.

```javascript
var singleton = (function () {
  var privateVariable = 'something private';

  var showPrivate = function () {
    console.log(privateVariable);
  };

  return {
    publicMethod: function() {
      showPrivate();
    },

    publicVariable: 'the public can see this!'
  };
})();
```

To only instantiate the singleton when it's needed.

```javascript
var singleton = (function () {
  var instance;

  var init = function () {
    return {
      publicMethod: function () {
        console.log('hello world');
      },
      publicProperty: 'public'
    };
  };

  return {
    getInstance: function () {
      if (!instance) {
        instance = init();
      }
      return instance;
    }
  };
})();
```

The singleton pattern is useful when exactly one object is needed to coordinate actions and data across the system.
