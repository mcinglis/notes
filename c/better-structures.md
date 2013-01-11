# Better structures

## Designated initializers

Designated initializers allow us to initialize structs by naming their elements.

They are extremely useful in giving meaning to function inputs.

```c
// struct tags have a separate namespace from other identifiers
typedef struct Character {
  char *name, *hometown;
  double strength, armor;
  int age;
} Character;

void Character_speak( Character character ) {
  printf( "Greetings! I'm %s of %s.", character.name, character.hometown );
}

int main() {
  Character william = {
    // Ordering of elements doesn't matter
    .age = 24,
    .name = "William",
    .strength = 4.3
  };
  // hometown nor strength were not specified, thus were initialized to zero
  assert( william.hometown == NULL );
  assert( william.strength == 0 );

  // Or, we can use anonymous compound literals, but this requires a typecast
  Character_speak((Character){
    .name = "Bob",
    .hometown = "Townsville"
  });
}
```

