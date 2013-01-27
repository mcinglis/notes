# Event maps

Several functions take event maps. An event map is an object where the properties specify a set of events to handle, and the values are the handlers for those events. The property can be in one of several forms. For example:

```javascript
{
  // Triggers when any element is clicked.
  'click': function (event) { ... },

  // Triggers when any element with the 'accept' class is clicked.
  'click .accept': function (event) { ... },

  // Triggers when 'accept' is clicked, or a key is pressed.
  'keydown, click .accept': function (event) { ... }
}
```

## Event objects

The following properties and methods are available on the event object passed to handlers.

* `type` (string): the event's type (e.g. "click", "blur" or "keypress").
* `target` (DOM element): the element that originated the event.
* `currentTarget` (DOM element): the element currently handling the event, i.e. the element matching the selector. For events that bubble, it may be `target` or an ancestor of `target`, and its value changes as the event bubbles.
* `which` (number): for mouse events, the number of the mouse button (1=left, 2=middle, 3=right). For key events, a character or key code.
* `stopPropagation()`: prevent the event from bubbling up to other elements. Other event handlers matching the same element are still fired.
* `stopImmediatePropagation()`: prevent any further event handlers being called for this event, on all event maps.
* `preventDefault()`: prevents the action the browser would normally take in response to this event, such as following a link or submitting a form.

Returning `false` from a handler will call `stopImmediatePropagation` and `preventDefault` for the event.

## Event types

* `click`
* `dblclick`
* `focus`, `blur`: a form control field gains or loses focus. Does not bubble.
* `change`: a checkbox or radio button changes state.
* `mouseenter`, `mouseleave`: does not bubble.
* `mousedown`, `mouseup`
* `keydown`, `keypress`, `keyup`
