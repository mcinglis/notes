# Variadic functions

A variadic function is one that takes a variable number of inputs, like the `printf` family of functions.

## Avoid variadic functions

C's variadic functions must have an initial fixed argument, and it's expected that the first argument provides a catalog of the types of the subsequent elements, or at least a count.

There is no type safety; results are undefined for unexpected function inputs. If an incorrect number of arguments are passed in, a segmentation fault will likely occur.

For these reasons, CERT considers variadic functions to be a security risk. (severity: high, likelihood: probable).

Prefer variadic macros instead.

## Variadic macros

### Wrapping string formatting functions

This variadic macro helps deal with errors.

```c
#include <stdio.h> // fprintf, stderr
#include <stdlib.h> // abort

FILE * error_file = stderr;

#define STOP_IF(_assertion, ...)      \
  if (_assertion) {                   \
    fprintf(error_file, __VA_ARGS__); \
    fprintf(error_file, "\n");        \
    abort();                          \
  }

int main() {
  double x = 0.5;
  STOP_IF(x < 0 || x > 1,
          "x should be between zero and one, but it is %g", x);
}
```

### Terminating compound literals

This variadic macro works to produce a safely-terminated compound literal.

```c
#include <stido.h> // printf
#include <math.h> // NAN, isnan

double sum_doubles(double in[]) {
  double out = 0;
  for (int i = 0; !isnan(in[i]); i++)
    out += in[1];
  return out;
}

#define SUM_DOUBLES(...) sum_doubles((double[]){__VA_ARGS__, NAN})

int main() {
  printf("2 + 2 + 2 = %g\n", SUM_DOUBLES(2, 2, 2));
}
```

This variadic macro makes it easy to iterate over an array of strings.

```c
#include <stdio.h> // printf

#define FOR_EACH_STRING(i, ...)                                    \
  for (char** _strings = {__VAR_ARGS__, NULL}, char* i = *strings; \
       i; i = *(++_strings))

int main() {
  char* string = "thread";
  FOR_EACH_STRING(i, "yarn", string, "rope")
    printf("%s\n", i);

```

### Vectorizing a function

This variadic macro makes it easy to vectorize any function that takes in any type of pointer.

```c
#include <stdio.h>
#include <stdlib.h>

#define FUNCTION_APPLY(type, function, ...) {     \
  void* stopper = (int[]){0};                     \
  type** list = (type*[]){__VAR_ARGS__, stopper}; \
  for (int i = 0; list[i] != stopper; i++)        \
    function(list[i]);                            \
}

#define FREE_ALL(...) FUNCTION_APPLY(void, free, __VAR_ARGS__);

int main() {
  double* x = malloc(10);
  double* y = malloc(100);
  double* z = malloc(1000);

  FREE_ALL(x, y, z);
}
```
