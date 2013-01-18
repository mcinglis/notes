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

`SET key value` sets the key to the string value.

`GET key` gets the key's value, which must be a string.

`INCR key` and `DECR key` increment or decrement the integer value of the key by one.

`INCRBY key increment` and `DECRBY key increment` increment or decrement the integer value of the key by the given increment.

`SETNX key value` sets the key to the given string value, but only if the key does not exist.

`DEL key` deletes the key.

`EXPIRE key seconds` sets a key's time to live in seconds.

`TTL key` gets the key's time to live.

### Lists

`RPUSH key value [value ...]` appends the values to the list.

`LPUSH key value [value ...]` prepends the values to the list.

`LRANGE key start stop` returns a subset of the list from start to stop inclusive. `-1` can be given for `stop` to retrieve all elements up to the end of the list. Other out-of-range indices will not produce an error.

`LLEN key` gets the length of the list.

`LPOP key` removes and returns the first element of the list.

`RPOP key` removes and returns the last element of the list.

### Sets

`SADD key member [member ...]` adds the members to the set.

`SREM key member [member ...]` removes the members from the set.

`SISMEMBER key member` determines if the given value is a member of the set.

`SMEMBERS key` gets all the members in a set.

`SUNION key [key ...]` combines the given sets and returns a list.

`SINTER key [key ...]` intersects the given sets and returns a list.

### Sorted sets

`ZADD key score member [score member ...]` adds the members to the sorted set, overwriting the score if the member is already in the set.

`ZRANGE key start stop [WITHSCORES]` returns a range of members in the sorted set, by their index.

### Hashes

`HSET key field value` sets the value of the hash's field. The value must be a string.

`HGET key field` gets the value of the hash's field.

`HDEL key field [field ...]` deletes the given fields from the hash.

`HEXISTS key field` determines the hash contains the given field.

`HLEN key` gets the number of fields in the hash.

`HINCRBY key field increment` increments the integer value of the hash's field by the given number.

`HKEYS key` gets all the fields in the hash.

`HVALS key` gets all the values in the hash.

`HGETALL key` gets all the fields and values in the hash.
