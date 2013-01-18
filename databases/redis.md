# Redis

Redis is a networked, in-memory, key-value data store. 

## Data model

The Redis data model is a dictionary wherein keys are mapped to values. A value can be:

* a string
* a list of strings
* a set of strings
* a sorted set of strings
* a hash of strings to strings

The type of value determines what commands are available for the value.

## Commands

> `SET server:name "fido"`
> `GET server:name` => `"fido"`
> `SET connections 10`
> `INCR connections` => `11`
> `INCR connections` => `12`
> `DEL connections`
> `INCR connections` => `1`

