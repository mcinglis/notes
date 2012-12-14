Some content is from [Better Python APIs](http://ozkatz.github.com/better-python-apis.html).

See [A Guide to Python's Magic Methods](http://www.rafekettler.com/magicmethods.html) for complete descriptions of magic methods, which help in designing better APIs.

TODO: write notes on language-agnostic API design.

## Write clients and tests before designing the API

Start out writing what you want (with respect to the API's desired generality) and what it should do, *then* implement to those requirements.

## Default to private access

Only expose what is needed. All implementation details should be hidden. Convenience functions are a matter of taste.

See the [visibility](visibility.md) notes.

## Use attributes and properties liberally

Getter and setter functions should almost always be replaced with attributes, or, if special logic is required, [properties](http://docs.python.org/library/functions.html#property).

Setters are permissable if a return value from assignment is semantically reasonable. For instance, an `equip` method on a Character should probably return a truthy value if equipping succeeded, or a falsy value if it failed.

## Operator overloading

### If in doubt, don't overload operators

If the functionality of operator overloading for your class could be considered by *anyone* to be unintuitive, then don't overload.

Ideally, write client code using your imagined operator overloaders and show it to a friend or three. If any of them guess the functionality incorrectly, then don't overload.

The functionality of overloaded operators should be extremely obvious and intuitive. Anything less and it becomes harmful to the readability of your API, even if the operator functionality will be documented.

### Make your objects REPL friendly

Make `__repr__` return an `eval`uable string representation of the object.

```python
>>> from mymodule import Container
>>> Container(1, 2, 'Hello', False)
Container(1, 2, 'Hello', False)
```

### Provide iteration for sequences where natural

Implement `__iter__` to expose an iterator to users. This hides the underlying complexity, as users can then use `for` to iterate through your data.

```python
>>> for video in youtube.Search('DjangoCon 2012'):
...     print(video)
```

### Overload arithmetic operators where natural

Overload arithmetic operators to make the semantics of your API seem more natural. For example, `__add__(self, other)` can be overloaded to enable `self + other`. Likewise for `__sub__`, `__mul__`, and `__div__`.

```python
>>> hero.health -= enemy.damage
>>> hero.position += 5 * hero.velocity
```

### Provide boolean meaning where natural

Empty data structures, queries with no results, and null objects could be considered falsy. This is defined with `__bool__` in Python 3, and `__nonzero__` in earlier Python versions.

`has` methods should be replaced with truthiness checking on the attribute or property.

```python
>>> if not opponent.ammo:
...     self.say('Muahaha. No hope for you now.')
```

### Provide length semantics where natural

Sets (actual or conceptual) of anything should probably have a length. This can be provided by overriding `__len__`.

```python
>>> if len(target.team) < len(self.team):
...     self.message(target, 'Join my team')
```

### Provide support for `x in collection` where natural

Collections and data structures should provide natural membership checking with the `in` keyword. This can be done by overriding `__contains__`.

```python
>>> if Terminator in self.vision:
...     if not self.equip(self.weapons.rocket_launcher):
...         self.message(self.team, 'Run!')
```

### Provide dynamic attributes where natural

Dynamic attributes can provide very readable and human-friendly APIs.  However, they aren't REPL friendly due to not being autocompleteable. Also, dynamic attributes can cause confusion if access is supported but assignment isn't, or vice versa.

Dynamic access can be provided by overriding `__getattr__`, and dynamic assignment can be provided by overriding `__setattr__`.

### Provide ordering semantics where natural

Ordering semantics can be implemented by overriding `__cmp__`. Not only does it provide all the ordering and equality operators such as `=`, `!=`, `<`, `>` and so on, but also supports the `sorted` function operating on lists of the object.
