# Publish and subscribe

These functions control how Meteor servers publish sets of records and how clients can subscribe to those sets.

## `Meteor.publish(name, onSubscribe)`

Publishes a record set to clients.

* **name**: the name of the attribute set. If `null`, the set has no name, and the record set is automatically sent to all connected clients.
* **onSubscribe**: function called on the server each time a client subscribes. In the function, `this` is the publish handler object. If a client passed arguments to `subscribe`, the function is called with the same arguments.

Publish functions can return a `Collection.Cursor` object, in which case that cursor's documents will be published.

```javascript
// Server-side

// Publish the `Rooms` collection, minus secret info.
Meteor.publish( 'rooms', function () {
  return Rooms.find( {}, { fields: { secretInfo: 0 } } );
} );

// But, publish secret information for rooms where the logged-in user is an
// admin. If the client subscribes to both streams, the records are merged
// together into the same documents.
Meteor.publish( 'adminSecretInfo', function () {
  return Rooms.find( { admin: this.userId }, { fields: { secretInfo: 1 } } );
} );
```

Otherwise, the publish function can `set` and `unset` individual record attributes on a client. These methods are provided by `this` in your publish function.

If you use `observe` to watch changes to the database, be sure to call `this.flush` from inside your observe callbacks. Methods that update the database are considered finished when the `observe` callbacks return.

```javascript
// Server: publish the current size of a collection.
Meteor.publish( 'roomMessageCounts', function (roomId) {
  var self = this;
  var uuid = Meteor.uuid();
  var count = 0;

  var handle = Messages.find( { roomId: roomId } ).observe( {
    added: function ( message, beforeIndex ) {
      count++;
      self.set( 'counts', uuid, { roomId: roomId, count: count } );
      self.flush();
    },
    removed: function ( message, atIndex ) {
      count--;
      self.set( 'counts', uuid, { roomId: roomId, count: count } );
      self.flush();
    }
  } );

  // Observe only returns after the initial added callbacks have run. Now mark
  // the subscription as ready.
  self.complete();
  self.flush();

  // Stop observing the cursor when the client unsubscribes.
  self.onStop( function () {
    handle.stop();
  } );
} );

// Client: declare collection to hold count of objects.
Counts = new Meteor.Collection( 'counts' );

// Client: autosubscribe to the count for the current room.
Meteor.autosubscribe( function () {
  Meteor.subscribe( 'roomMessageCounts', Session.get( 'roomId' ) );
} );

// Client: use the new collection
console.log( 'Current room has ' + Counts.findOne().count + ' messages.' );
```

### Publish handler methods

#### `this.set(collection, id, attributes)`

Queues a command to set attributes.

#### `this.unset( collection, id, keys )`

Queues a command to unset attributes.

#### `this.complete()`

Queues a command to mark this subscription as complete (as in, initial attributes are set).

#### `this.flush()`

Sends all pending `set`, `unset`, and `complete` commands to the client.

#### `this.onStop( callback )`

Registers a callback to run when the subscription is stopped.

#### `this.stop()`

Stops the client's subscription.

## `Meteor.subscribe( name [, arg1, arg2, ... ] [, onComplete] )`

Subscribes to a record set, and returns a handle that provides a `stop()` method, which will stop the subscription.

* **name**: name of the subscription, matching the name of the server's `publish` call.
* **arg1**, **arg2**, ...: optional arguments passed to the publisher function on the server.
* **onComplete**: called without arguments when the server marks the subscription as complete.

When you subscribe to a record set, it tells the server to send records to the client. The client stores these records in local Minimongo collections, with the same name as the `collection` argument to `set`. Meteor will queue incoming attributes until you declare the `Meteor.Collection` on the client with the matching collection name.

## `Meteor.autosubscribe( func )`

Automatically set up and tear down subscriptions.

* **func**: a reactive function that sets up some subscriptions by calling `Meteor.subscribe`. It will automatically be re-run when its dependencies change.

```javascript
// Subscribe to the chat messages in the current room. Automatically update
// the subscription whenever the current room changes.
Meteor.autosubscribe( function () {
  Meteor.subscribe( 'chat', { room: Session.get( 'currentRoom' ) } );
} );
```
