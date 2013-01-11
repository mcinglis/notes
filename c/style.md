# A modern style guide for C

C can be written very badly. It has a lot of historical baggage and cultural remnants of a bygone era in programming.

This style guide is aimed at promoting modern best practices for C, that produces code that is a joy to read.

## Typedefs

Typedefs should be used for all struct definitions and function pointers.

Never use typedefs for struct pointers, or to mask built-in types.

## Structs

In `struct` definitions, both the `struct` identifier and `typedef` identifiers should be the same, and should be capitalized by `CamelCase`.

Only the first letter of acronyms (like HTML or RPC) should be capitalized.

Don't put function pointer members in structs unless those functions are intended to be changed.

```c
typedef struct TemplateConfig {
  int someSetting;
  char someCode;
}
```
