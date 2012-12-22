The mediator pattern is a behavioral design pattern that allows us to expose a unified interface through which the different parts of a system may communicate.

## Implementation

```javascript
var mediator = {};

(function (module) {
  var channels = {};

  module.subscribe = function (channel, callback) {
    channels[channel] = channels[channel] || [];
    channels[channel].push({
      context: this,
      callback: callback
    });
    return this;
  };

  module.publish = function (channel) {
    var subscribers = channels[channel];
    if (!subscribers) return false;
    var args = Array.prototype.slice.call(arguments, 1);
    for (var i = 0; i < subscribers.length; i++) {
      var subscriber = subscribers[i];
      subscriber.callback.apply(subscriber.context, args);
    }
    return this;
  };

  module.installTo = function (object) {
    object.subscribe = module.subscribe;
    object.publish = module.publish;
  };

}(mediator));
```

### Usage

```javascript
var person = 'Luke';

mediator.subscribe('nameChange', function (arg) {
  console.log(person);
  person = arg;
  console.log(person);
});

mediator.publish('nameChange', 'David');
```
