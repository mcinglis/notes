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

If you use `observe` to watch changes to the database, be sure to call `this.flush` from inside your observe callbacks.

```javascript
// Server: publish the current size of a collection.
Meteor.publish( 'countsByRoom', function (roomId) {
  var self = this;
  var uuid = Meteor.uuid();
  var count = 0;

  var handle = Messages.find( { roomId: roomId } ).observe( {
    added: function (doc, previousId) {
      count++;
      self.set( 'counts', uuid, { roomId: roomId, count:  } );
      self.flush();
    },
    removed: function (doc, previousId) {
      count--;
      self.set( 'counts', uuid, { roomId: roomId } );
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
Counts = new Meteor.Collection('counts');

// Client: autosubscribe to the count for the current room.
Meteor.autosubscribe( function () {
  Meteor.subscribe( 'countsByRoom', Session.get( 'roomId' ) );
} );

// Client: use the new collection
console.log( 'Current room has ' + Counts.findOne().count + ' messages.' );
```
