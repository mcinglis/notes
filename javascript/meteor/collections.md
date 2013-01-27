# Collections

Meteor stores data in *collections*.

## `new Meteor.Collection(name, [options])`

* **name**: the name of the collection. If null, creates an unmanaged (unsynchronized) local collection.
* **manager**: the Meteor connection that will manage this collection, defaults to `Meteor` if null. Unmanaged collections cannot specify a manager.

Calling this function is analogous to declaring a model in a traditional ORM-centric framework. It sets up a *collection* of *documents* to store information. Each document is a JSON object, and has a `_id` property whose value is unique in the collection.

```javascript
Chatrooms = new Meteor.Collection('chatrooms');
Messages = new Meteor.Collection('messages');
```

The constructor returns an object with methods to `insert`, `update`, `remove` and `find` documents in the collection.

```javascript
// Return an array of my messages.
var myMessages = Messages.find({ userId: Session.get('currentUserId') }).fetch();
```


