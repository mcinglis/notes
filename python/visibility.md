Prefixing variables with `_` is a widely-used convention in Python to denote that the variable is private. By default, `from module import *` will ignore `_`-prefixed variables.

I consider `_`-prefixing to be an antipattern because it makes the variable name dependent on its visibility. For example, if the `_Request` class is made public and thus renamed `Request`, all references to `_Request` (in your own code or others) need to be changed.

However, `_`-prefixing does allow for external recognition of visibility. If you `import module`, private variables will be indistinguishable from exported variables in `dir(module)`. Furthermore, some tools (e.g., documentation generators) treat `_`-prefixed variables as private.

You can define `__all__` in modules to control what variables are exported.

```python
__all__ = ['these', 'Variables', 'are_exported']

# And this isn't:
class Request:
    ...
```

However, this pattern requires variable names to be repeated in the `__all__`
assignment.

A solution would be to write a `@public` decorator that exports the decorated class or function, and a module that, when imported, will modify non-public variables to be externally visible with `_`. However, I don't know if this is even possible.

Another solution would be to establish a visibility documentation standard and expect fellow developers to read documentation.

## `private` decorator implementation in *Learning Python, 4th Edition*

```python
def class_private(*privates):
    def decorator(WrappedClass):
        class Wrapper:
            def __init__(self, *args, **kwargs):
                self.__wrapped = WrappedClass(*args, **kwargs)

            def __getattr__(self, attr):
                if attr in privates:
                    raise TypeError('private attribute access: ' + attr)
                else:
                    return getattr(self.wrapped, attr)

            def __setattr__(self, attr, value):
                if attr == '__wrapped':
                    self.__dict__[attr] = value
                elif attr in privates:
                    raise TypeError('private attribute change: ' + attr)
                else:
                    setattr(self.wrapped, attr, value)

        return Wrapper
    return decorator

@class_private('name')
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

marge = Person('Margaret', 64)
print(marge.name)

# Raises TypeErrors
print(marge.age)
marge.age -= 10
```

## Name mangling with `__`

Any class member variable that starts with two underscores is textually replaced to be prefixed with the name of the class. For example, a variable called `__spam` in the `Example` class will be visible outside of that class definition as `_Example__spam`.

Name mangling is helpful for letting subclasses override methods without breaking method calls.

```python
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    # private copy of original update() method
    __update = update

class MappingSubclass(Mapping):
    # overrides update() without breaking __init__()
    def update(self, keys, values):
        for item in zip(keys, values):
            self.items_list.append(item)
```
