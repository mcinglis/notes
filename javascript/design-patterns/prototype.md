The prototype pattern creates objects based on a template of an existing object through cloning.

Real prototypal inheritance requires the use of `Object.create`, which is defined in the ECMAScript 5 standard.

```javascript
var car = {
  drive: function () {},
  name: 'Mazda 3'
};

var anotherCar = Object.create(car);
console.log(anotherCar.name);
```

`Object.create` allows you to easily implement advanced concepts such as differential inheritance where objects are able to directly inherit from other objects.

Properties can be initialized on the second argument of `Object.create` using an object literal syntax similar to that used by the `Object.defineProperty` method.

```javascript
var vehicle = {
  logModel: function () {
    console.log('The model of this vehicle is...' + this.model);
  }
};

var car = Object.create(vehicle, {
  'model': {
    value: 'Ford',
    enumerable: true,
    // By default:
    // writable: false,
    // configurable: false
  }
});
```

## Without using `Object.create`

This does not allow the user to define read-only properties in the same manner (as `vehiclePrototype` may be altered if not careful).

```javascript
var beget = (function () {
  function constructor() {]
  return function (prototype) {
    F.prototype = prototype;
    return new F();
  };
})();

var vehiclePrototype = {
  init: function (model) {
    this.model = model;
  },
  logModel: function () {
    console.log('The model of this vehicle is...' + this.model);
  }
};

var makeVehicle = function (model) {
  var vehicle = beget(vehiclePrototype);
  vehicle.init(model);
  return vehicle;
}

var car = makeVehicle('Ford Escort');
car.logModel();
```
