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

``` ruby
def message_as(name)
  lambda { |message| puts "#{name}: #{message}" }
end

matz_messager = message_as("matz")
matz_messager.call "Hi there!"
# => matz: Hi there!
```

## Blocks

```ruby
(1..10).each do |x|
  puts x
end

contents = File.open('/path/to/file', 'r') do |file|
  file.read
end
```

### Passing blocks around

``` ruby
def print_words
  each_word { |w| puts w }
end

# &block here turns the block into a proc
def each_word(&block)
  # &block here turns the proc back into a block
  ["hello", "world"].each(&block)
end

# Don't do this:
def each_word
  ["hello", "world"].each { |word| yield word }
end
```

### Optional blocks

``` ruby
def print_stuff
  stuff = ["hello", "world"]
  if block_given?
    stuff.each { |x| puts yield x }
  else
    puts stuff.join(", ")
  end
end

print_stuff
# => hello, world

print_stuff { |x| "stuff: #{x}" }
# => stuff: hello
# => stuff: world
```

#### Optional blocks in constructors

``` ruby
class Tweet
  def initialize
    yield self if block_given?
  end
end

Tweet.new do |tweet|
  tweet.status = "Set in initialize!"
  tweet.created_at = Time.now
end
```

## Procs

### `Symbol#to_proc`

``` ruby
# Rather than:
[1, 2, 3].reduce { |acc, n| acc + n }
tweets.map { |tweet| tweet.user }

# You can do this:
[1, 2, 3].reduce(&:+)
tweets.map(&:user)

# But you can't do this:
tweets.map(&:user.name)
```

## Lambdas


