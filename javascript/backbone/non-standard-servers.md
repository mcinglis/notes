# Dealing with non-standard servers

For an example, suppose that another team has messed up the JSON returned for Appointment data. Instead of returning JSON like:

``` json
{
  "id": 1,
  "title": "Ms. Kitty Hairball Treatment",
  "cancelled": false
}
```

The server is actually returning JSON like:

``` json
{
  "appointment": {
    "identifier": 1,
    "title": "Ms. Kitty Hairball Treatment",
    "cankelled": false
  }
}
```

How do we fix this?

``` javascript
var Appointment = Backbone.Model.extend({

  // The attribute name that represents the model's ID
  idAttribute: 'identifier',

  // Override parse to work with non-standard server responses
  parse: function ( response ) {
    var a = response.appointment;
    a.cancelled = a.cankelled;
    delete a.cankelled;
    return a;
  }

  // Override toJSON to control how the data is structured to be sent
  // back to the server
  toJSON: function () {
    var attrs = _.clone( this.attributes );
    attrs.cankelled = attrs.cancelled;
    delete attrs.cankelled;
    return { appointment: attrs };
  }
});

var data = {
  "appointment": {
    "title": "Ms. Kitty Hairball Treatment",
    "cankelled": false,
    "identifier": 1
  }
};

// We make sure the attributes are run through the parse method like so:
var appointment = new Appointment( data, { parse: true } );

// All views should be using model.attributes for templating, not toJSON
var AppointmentView = Backbone.View.extend({
  template: _.template( '<p><%= title %></p>' ),

  render: function () {
    this.$el.html( this.template( this.model.attributes ) );
  }
});
```

## Small `idAttribute` example

``` javascript
var Meal = Backbone.Model.extend({
  idAttribute: '_id'
});

var cake = new Meal({ _id: 1, name: 'Cake' });
console.log( 'Cake's ID is ' + cake.id );
// => Cake's ID is 1
```
