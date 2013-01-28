# Collections

Meteor stores data in *collections*.

## `new Meteor.Collection(name, [options])`

* **name**: the name of the collection. If null, creates an unmanaged (unsynchronized) local collection.
* options[**manager**]: the Meteor connection that will manage this collection, defaults to `Meteor` if null. Unmanaged collections cannot specify a manager.

Calling this function is analogous to declaring a model in a traditional ORM-centric framework. It sets up a *collection* of *documents* to store information. Each document is a JSON object, and has a `_id` property whose value is unique in the collection.

```javascript
Chatrooms = new Meteor.Collection('chatrooms');
Messages = new Meteor.Collection('messages');
```

The constructor returns an object with methods to `insert`, `update`, `remove` and `find` documents in the collection.

```javascript
// Return an array of my messages.
var myMessages = Messages.find({ userId: Session.get('currentUserId') }).fetch();

// Create a new message.
Messages.insert({ text: 'Hello, world!' });

// Mark my first message as "important".
Messages.update(myMessages[0].id, { $set: { important: true }});
```

When you pass a non-null `name` value:

* On the server, a collection with that name is created on a backend MongoDB server. When you call methods on that collection on that server, they translate directly into normal MongoDB operations (given that they match your access control rules).
* On the client, a Minimongo instance is created. Minimongo is essentially an in-memory, non-persistent implementation of MongoDB in pure JavaScript. It serves as a local cache that stores just the subset of the database that this client is working with. Queries on the client (`find`) are served directly out of the cache, without talking to the server.
* When you write to the database on the client (`insert`, `update` or `remove`), the command is executed immediately on the client, and simultaneously, it's shipped up to the server and executed there too. The `livedata` package is responsible for this.

If you pass `null` as the `name` value, then you're creating a local collection. It's not synchronized anywhere; it's just a local scratchpad that supports MongoDB-style `find`, `insert`, `update` and `remove` operations (implemented using Minimongo).

By default, Meteor automatically publishes every document in your collection to each connected client. To turn this behaviour off, remove the `autopublish` package:

```bash
$ meteor remove autopublish
```

...and instead call `Meteor.publish` to specify which parts of your collection should be published to which users.

## *collection*`.find(selector, [options])`

Find the documents in a collection that match the selector.

* **selector** (Mongo selector or String): the query
* options[**sort**] (Object: sort specifier): sort order (default: natural order)
* options[**skip**] (Number): number of results to skip at the beginning
* options[**limit**] (Number): maximum number of results to return
* options[**fields**] (Object: field specifier): (Server only) fields to return or exclude.
* options[**reactive**] (Boolean): (Client only) Default `true`; pass `false` to disable reactivity.

`find` does not immediately access the database or return documents. Instead, it returns a cursor object with the following methods:

* `fetch` returns the matching documents.
* `map` and `forEach` allow iteration over the matching documents.
* `observe` registers callbacks for when the set of matching documents changes.

## *collection*`.findOne(selector, [options])`

Finds the first document that matches the selector, as ordered by sort and skip options.

Equivalent to `find(selector, options).fetch()[0]`.

## *collection*`.insert(doc, [callback])`

Inserts a document in the collection and returns its unique `_id`.

* **doc** (Object): the document to insert; should not yet have an `_id` attribute.
* **callback** (Function): If present, called with an error object as the first argument and, if no error, the `_id` as the second.

A document is just an object, and its fields can contain any combination of JSON-compatible datatypes (arrays, objects, numbers, strings, `null`, `true` and `false`).

On the server, if you don't provide a callback, `insert` will block until the database acknowledges the write, or throws an exception if something went wrong. If you do provide a callback, `insert` returns the ID immediately. 

On the client, `insert` never blocks. If you do not provide a callback and the insert fails on the server, then Meteor will log a warning to the console.

```javascript
var groceriesId = Lists.insert({ name: 'Groceries' });
Items.insert({ list: groceriesId, name: 'Watercress' });
Items.insert({ list: groceriesId, name: 'Persimmons' });
```

## *collection*`.update(selector, modifier, [options], [callback])

Modifies one or more documents in the collection.

* **modifier** (Object: Mongo modifier): specifies how to modify the documents.
* options **multi** (Boolean): `true` to modify all matching documents, `false` to only modify one of the matching documents (the default).

```javascript
// Give the 'Superlative' badge to every user with a score greater than 10.
// If the user is logged in and their badge list is visible on the screen, it
// will update automatically as they watch.
Users.update({ score: { $gt: 10 } },
             { $addToSet: { badges: 'Superlative' } },
             { multi: true });
```

## *collection*`.remove(selector, [callback])`

Removes documents from the collection.

```javascript
// Delete all users with karma less than -2.
Users.remove({ karma: { $lt: -2 } });

// Delete all the log entries
Logs.remove({});
```

## *collection*`.allow(options)`

Allows users to write directly to this collection from client code, subject to limitations you define.

* options **insert**, **update**, **remove** (Function): functions that look at the proposed modification and return true if it should be allowed, or false if not.
* options **fetch** (Array of Strings): optional performance enhancement. Limits the fields that will be fetched from the database for inspection by your `update` and `remove` callbacks.

## *collection*`.deny(options)`

Overrides `allow` rules. Same options as `allow`, except the callbacks return `true` if the operation should be denied.

```javascript
Posts = new Meteor.Collection('posts');

Posts.allow({
  insert: function (userId, doc) {
    // Users must be logged in, and can only create posts belonging to them
    return (userId && doc.owner === userId);
  },
  update: function (userId, docs, fields, modifier) {
    // Users can only change their own posts.
    return _.all(docs, function (doc) {
      return doc.owner === userId;
    });
  },
  remove: function (userId, docs) {
    // Users can only remove their own posts.
    return _.all(docs, function (doc) {
      return doc.owner === userId;
    });
  },
  fetch: ['owner']
});

Posts.deny({
  update: function (userId, docs, fields, modifier) {
    // Users can't change the owner of a post.
    return _.contains(fields, 'owner');
  },
  remove: function (userId, docs) {
    // Users can't remove locked posts.
    return _.any(docs, function (doc) {
      return doc.locked;
    });
  },
  // No need to fetch the 'owner' field of posts
  fetch: ['locked']
});
```
