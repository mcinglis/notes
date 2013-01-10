# Modern conveniences and conventions

## Explicit return from `main`

If you don't write `return 0;` as the last line in `main`, then it will be assumed.

## Declare variables only where they're needed

Variables no longer need to be declared at the top of the block.

## Set array size at runtime

Arrays can now be allocated to have a length determined at runtime.

So, this:

```c
int thread_count = atoi(argv[1]);
pthread_t* threads = malloc(thread_count * sizeof(pthread_t));
...
free(threads);
```

Can be written as just:

```c
pthread_t threads[atoi(argv[1])];
```

## Automatic type casts

If it's valid to assign an item of one type to an item of another type, then C will do it for you without your having to tell it to with an explicit cast.

Thus, there remain three reasons to use C's type-casting syntax:

* performing true division (not integer division) of two `int` variables
* making an array index an `int`
* using compound literals of arrays and structs

## Favor strings over `enum`s

Enums are often used for error codes and operation codes, as in `open`.

In these situations, characters and strings are easier to memorize, don't pollute the namespace, and are easier to use and extend in external systems.

## Use `goto` for common clean-ups, and little else

`goto` can be used for cleaning up resources used in a function in case of different kinds of errors.

Otherwise, it's generally considered less-than-ideal.

## Don't use `switch`

Don't use `switch`, as it's error-prone and verbose. Rather, use a series of `if`s and `else`s.

## Always use `double` over `float`

Numeric drift with `float`s is harmful. Computer resources are cheaper, and we should use `double`s everywhere.

## Don't hesitate to use `long`s


