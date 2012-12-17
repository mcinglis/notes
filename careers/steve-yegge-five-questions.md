# The five essential phone-screen questions

https://sites.google.com/site/steveyegge2/five-essential-phone-screen-questions

Steve Yegge writes about the best ways to screen candidates over the phone for in-person interviews, learning from experience phone screening at Google.

## Phone screen antipatterns

What commonly went wrong in failed phone screens:

* the candidate did most of the talking
* the candidate was only asked about what they know: one-trick ponies only know one trick

## Five essential questions

1. **Coding**: the candidate should write some simple code, with correct syntax, in C, C++ or Java.
2. **OO design**: the candidate has to define basic OO concepts, and come up with classes to model a simple problem.
3. **Scripting and regexes**: the candidate has to define how to find the phone numbers in 50,000 HTML pages.
4. **Data structures**: the candidate has to demonstrate basic knowledge of the most common data structures.
5. **Bits and bytes**: the candidate has to answer simple questions about bits, bytes and binary numbers.

These five areas are litmus tests. You have to probe all five areas; you can't skip any of them. Each area is a proxy for a huge body of knowledge, and failing it very likely means failing the interviews. They were chosen on the following criteria:

1. They're *universal* - every programmer needs to know them, regardless of experience, so you can use them in all SDE phone screens, from college hires through 30-year veterans.
2. They're *quick* - each area can be probed very quickly with 1 to 5 minutes of "weeder questions".
3. They're *predictors* - there are certain common "SDE profiles" that are easy to spot because they tend to fail in one or more of these five areas.

What you should be looking for is a *total vacuum* in one of these areas. It's OK if they struggle a little and then figure it out.

## Coding

Some properties of good weeder coding questions are:

1. It's simple
2. You've solved it
3. It has loops or recursion
4. It has formatted output
5. It has text-file I/O

### Write a function to reverse a string

### Write a function to compute the nth fibonacci number

### Write a function to print out the multiplication table up to 12x12

### Write a function that sums up integers from a text file, one int per line

### Write a function to print the odd numbers from 1 to 99

### Find the largest int value in an int array

### Format an RGB value (three 1-byte numbers) as a 6-digit hexadecimal string

## Object-oriented programming

### Terminology

Candidates should know the following list cold. It's not a complete list.

* class, object (and the difference between the two)
* instantiation
* method (as opposed to, say, a C function)
* virtual method, pure virtual method
* class/static method
* static/class initializer
* constructor
* destructor/finalizer
* superclass or base class
* subclass or derived class
* inheritance
* encapsulation
* multiple inheritance (and give an example)
* delegation/forwarding
* composition/aggregation
* abstract class
* interface/protocol (and difference from an abstract class)
* method overriding
* method overloading (and difference from overriding)
* polymorphism (without resorting to examples)
* is-a versus has-a relationships (with examples)
* method signatures (what's included in one)
* method visibility (e.g. public/private/other)

### Design

This is where most candidates fail with OO. For OO-design weeder questions, have candidates describe:

1. What classes they would define
2. What methods go in each class (including signatures)
3. What the class constructors are responsible for
4. What data structures the class will have to maintain
5. Whether any design patterns are applicable to this problem.

#### Questions

##### Weeder questions

###### Design a deck of cards that can be used for different card game applications

###### Model the animal kingdom as a class system, for use in a virtual zoo program

###### Create a class design to represent a filesystem

###### Design an OO representation to model HTML

##### In-depth questions

###### Design a parking garage

###### Design a bank of elevators in a skyscraper

###### Model the monorail system at Disney World

###### Design a restaurant reservation system

###### Design a hotel room-reservation system

