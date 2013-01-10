# Memory in C

## Memory management models

### Automatic

### Static

#### Declaring static variables

Static variables are initialized when the program starts, before `main` is executed. Therefore, they can't be initialized with a nonconstant value.

The code below won't compile, as `Point_new()` can't be called before `main()`.

```c
static Query query = Query_new();
```

This can be solved by allocating the variable on first use.

```c
static Query query;
if (!query) query = Query_new();
```

### Manual

## Structures are copied, arrays are aliased

Structures are copied on assignment and return from functions.

```c
typedef struct {
  double base, square, cube;
} Powers;

Powers Powers_new( double in ) {
  return (Powers){
    .base = in,
    .square = in * in,
    .cube = in * in * in
  };
}

int main() {
  // Powers_new returns a copy of the struct constructed internally
  Powers threes = Powers_new( 3 );
  // Makes a copy of threes' values
  Powers copy = threes;

  threes.base = 10;
  threes.square = 100;

  // copy hasn't changed (or vice versa had we changed copy)
  assert( copy.base == 3 );
  assert( copy.square == 9 );
  assert( copy.cube == 27 );
}
```

Arrays are not copied on assignment or return from functions; their references are. This is a nasty trap; the pointer returned from a function may be pointing to automatically allocated data which was destroyed on the function exiting.

Copying an array requires `memcpy`.

```c
#include <string.h> // memcpy

int main() {
  int abc [] = { 'a', 'b', 'c' };
  int * reference = abc;
  int copy [3];

  memcpy(copy, abc, sizeof int * 3)

  abc[1] = 'x';

  assert( reference[1] == 'x' );
  assert( copy[1] == 'b' );
}
```
