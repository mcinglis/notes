Observers register their interest in a certain type of event by listening to that event on a subject. When that event is triggered on the subject, the subject notifies all its listeners of the event.

The observer pattern is also known as the publish/subscribe pattern.

## Advantages

* promotes loose coupling
* encourages consideration about the relationships between objects in the system

## Disadvantages

* Subjects can't safely assume that the appropriate observers are listening to them
* Observers are ignorant of the existence of each other, making update dependencies difficult

## Libraries

The observer pattern fits in very well with Javascript ecosystems. Popular Javascript libraries already have utilities that can assist in easily implementing the observer pattern.

```javascript
// Publish

// Dojo
dojo.publish('channel', [arg1, arg2]);

// jQuery
$(el).trigger('channel', [arg1, arg2]);

// YUI
el.publish('channel', [arg1, arg2]);

// Subscribe

// Dojo
var handle = dojo.subscribe('channel', function (data) { ... });

// jQuery
$(el).on('channel', function (event) { ... });

// YUI
el.on('channel', function (data) { ... });

// Unsubscribe

// Dojo
dojo.unsubscribe(handle);

// jQuery
$(el).off('channel');

// YUI
el.detach('channel');
```

## Implementation

```javascript
var pubsub = {};

(function (q) {
  var topics = {},
      counter = 0;

  q.publish = function (topics, args) {
    var subscribers = topics[topic];

    if (!subscribers)
      return false;

    var len = subscribers.length;
    while (len--)
      subscribers[len].func(topic, args);

    return true;
  };

  q.subscribe = function (topic, func) {
    topics[topic] = topics[topic] || [];
    var token = counter++;
    topics[topic].push({
      token: token,
      func: func
    });
    return token;
  };

  q.unsubscribe = function (token) {
    for (var m in topics)
      if (topics[m])
        for (var i = 0; i < topics[m].length; i++)
          if (topics[m][i].token === token) {
            topics[m].splice(i, 1);
            return token;
          }
  }
}(pubsub));
```

### Basic usage

```javascript
var handler = function (topics, data) {
  console.log(topics + ': ' + data);
};

var subscription = pubsub.subscribe('example1', handler);

pubsub.publish('example1', 'hello world');
pubsub.publish('example1', ['a', 'b', 'c']);
pubsub.publish('example2', [{ color: 'blue' }, { text: 'hello' }]);

pubsub.unsubscribe(subscription);

pubsub.publish('example1', 'hello again?');
```
