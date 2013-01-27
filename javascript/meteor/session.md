# Session

`Session` provides a global object on the **client** that you can use to store an arbitrary set of key-value pairs. Use it to store things like the currently-selected item in a list.

`Session` is reactive. If you call `Session.get('currentList')` from inside a template, the template will automatically be rendered whenever `Session.set('currentList', x)` is called.

## `Session.set(key, value)`

Set a variable in the session. Notify any listeners that the value has changed (e.g. redraw templates, and rerun any `Meteor.autosubscribe` blocks that called `Session.get` on this `key`).

```javascript
Meteor.autosubscribe(function () {
  Meteor.subscribe('chatHistory', { room: Session.get('currentRoomId') });
});

// Causes the function passed to Meteor.autosubscribe to be re-run, so
// that the chat-history subscription is moved to the room 'home'.
Session.set('currentRoomId', 'home');
```

## `Session.get(key)`

Get the value of a session variable. If inside a `Meteor.deps` context, invalidates the context the next time the value of the variable is changed by `Session.set`. This returns a clone of the session value, so mutating the returned value has no effect on the value stored in the session.

```javascript
Session.set('enemy', 'Eastasia');
var fragment = Meteor.render(function () {
  return '<p>We\'ve always been at war with ' +
         Session.get('enemy') + '</p>';
});

// Page will say "We've always been at war with Eastasia".
document.body.append(fragment);

// Page will change to say "We've always been at war with Eurasia".
Session.set('enemy', 'Eurasia');
```

## `Session.equals(key, value)`

Test if a session variable is equal to a value. If inside a `Meteor.deps` context, invalidates the context the next time the variable changes to or from the value.

For object and array session values, you cannot use `Session.equals`; instead, you need to use something like `underscore` and write `_.isEqual(Session.get(key), value)`.

These two expressions do the same thing:

```javascript
Session.get('key') === value;
Session.equals('key', value);
```

But the second one is always better, because it triggers fewer invalidations (template redraws).

### Example

```handlebars
<template name="postsView">
  {{#each posts}}
    {{> postItem}}
  {{/each}}
</template>

<template name="postItem">
  <div class="{{postClass}}">
    {{title}}
  </div>
</template>
```

```javascript
Template.postsView.posts = function () {
  return Posts.find();
};

Template.postItem.postClass = function () {
  if (Session.equals('selectedPost', this._id)) {
    return 'selected';
  } else {
    return '';
  }
}

Template.postItem.events({
  'click': function () {
    Session.set('selectedPost', this._id);
  }
});

// Using `Session.equals` here means that when the user clicks on an
// item and changes the selection, only the newly selected and the
// newly unselected items are re-rendered.
// If `Session.get` had been used instead, then whenever the
// selection changed, all the items would be re-rendered.
```
