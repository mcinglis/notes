An object is a set of key-value pairs known as properties.

There should be no comma after the final property. Object literals don't require instantiation using the `new` operator.

New properties can be added to an object after its assignment.

```javascript
var person = {
    name: 'Brendan',
    introduce: function() {
        return "Hello";
    }
};

person.address = {
    zipcode: '12345',
    state: 'CA'
};
```
