The command pattern encapsulates method invocation, requests or operations into a single object, and gives you the ability to both parameterize and pass method calls around that can be executed at your discretion.

It decouples the objects invoking the action from the objects which implement them, giving you a greater degree of overall flexibility in swapping out concrete classes (i.e. non-abstract classes).

Implementations of simple command objects bind an action with the object wishing to invoke the action. They consistently include an execution function, such as `run()` or `execute()`. All command objects with the same interface can easily be swapped as needed, and this is a benefit of the pattern.

## Implementation

```javascript
var CarManager = {
  requestInfo: function (model, id) {},
  buyVehicle: function (model, id) {},
  bookViewing: function (model, id) {}
};
```

If `CarManager`'s API changes, all references to its methods need to be changed. This dependency is a layer of coupling between the interface and the clients.

We can expand our `CarManager` to with a function that takes the name of an operation and data that that operation may or may not need to operate. We would like to be able to decouple the interface from its users, by allowing users to invoke operations with:

```javascript
CarManager.execute('buyVehicle', { model: 'Ford Escort', id: '4535' });
```

This decouples the users from the interface. The functions' names, required parameters, and ordering of parameters can all change without the client code being affected.

`CarManager.execute` can be implemented as follows.

```javascript
CarManager.execute = function (name, data) {
  return CarManager[name] && CarManager[name](data);
};
```

Note that this implementation requires the internal methods to only accept a single data object parameter.

## Commentary

It seems this pattern could be implemented simply by defining functions to take a single data object.

```javascript
var CarManager = {
  requestInfo: function (args) {},
  buyVehicle: function (args) {},
  arrangeViewing: function (args) {}
};
```

This decouples client code from the interface's parameter ordering changing, and aliases can easily be defined if required (i.e. for renaming functions). So, what's the benefit of implementing an `execute` function over this?
