Mixins are a common pattern in Javascript that automate the assignment of properties of one object to another.

Mixins need to be handled differently in ES3 and ES5.

More information: http://www.nczonline.net/blog/2012/12/11/are-your-mixins-ecmascript-5-compatible/

A mixin function written only for ES5 compatibility would be:

```javascript
function mixin(receiver, supplier) {
  Object.keys(supplier).forEach(function(property) {
    Object.defineProperty(receiver, property,
                          Object.getOwnPropertyDescriptor(supplier, property));
  });
}
```

Whereas a mixin function written for ES3 and ES5 compatibility would be:

```javascript
function mixin(receiver, supplier) {
  if (Object.keys)
    Object.keys(supplier).forEach(function(property) {
      Object.defineProperty(
          receiver,
          property,
          Object.getOwnPropertyDescriptor(supplier, property)
      );
    });
  else
    for (var property in supplier)
      if (supplier.hasOwnProperty(property))
        receiver[property] = supplier[property];
}
```
