# Know your closures: blocks, procs and lambdas

* <http://www.dev.gd/20130107-know-your-closures-blocks-procs-and-lambdas.html>

[First class functions](http://en.wikipedia.org/wiki/First-class_function)

> In computer science, a programming language is said to have first-class functions if it treats functions as first-class citizens. Specifically, this means the language supports passing functions as arguments to other functions, returning them as the values from other functions, and assigning them to variables or storing them in data structures.

Ruby methods aren't first-class functions:

```ruby
def method_a
  def method_b
    puts "I'm method b"
  end
end

x = method_a
x() # => NoMethodError: undefined method 'x' for main:Object
```

However, Ruby provides three different ways to define functions in ways that do behave as first-class functions: blocks, procs and lambdas. These are all [closures](http://en.wikipedia.org/wiki/Closure_(computer_science\)):

> In computer science, a closure (also lexical closure or function closure) is a function or reference to a function together with a referencing environment — a table storing a reference to each of the non-local variables (also called free variables) of that function. A closure — unlike a plain function pointer — allows a function to access those non-local variables even when invoked outside of its immediate lexical scope.

## Blocks

```ruby
(1..10).each do |x|
  puts x
end

contents = File.open('/path/to/file', 'r') do |file|
  file.read
end
```

