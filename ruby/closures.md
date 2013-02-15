# Know your closures: blocks, procs and lambdas

* [Know your closures: blocks, procs and lambdas](http://www.dev.gd/20130107-know-your-closures-blocks-procs-and-lambdas.html)
* [Closures in Ruby](http://innig.net/software/ruby/closures-in-ruby)

Ruby provides multiple ways of defining closures. Each way is slightly different in syntax and semantics.

## [Methods](http://www.ruby-doc.org/core-1.9.3/Method.html)

```ruby
def method_a
  def method_b
    puts "I'm method b"
  end
  method :method_b
end

x = method_a
x.call          #=> "I'm method b"
```

``` ruby
m = 12.method(:+)
m.call 3        #=> 15
m.call 20       #=> 32
```

## Blocks

Blocks are the most Ruby-like way to use closures.

```ruby
(1..10).each do |x|
  puts x
end

contents = File.open('/path/to/file', 'r') do |file|
  file.read
end
```

### Writing functions that take blocks

``` ruby
def time
  start = Time.now
  result = yield
  puts "Completed in #{Time.now - start} seconds."
  result
end

time do
  sleep 2
end
# => Completed in 2.001109 seconds.
```

### Yielding values to blocks

``` ruby
def example(n)
  yield n
end

example(3) { |x| x + 3 }        #=> 6
```

### Passing blocks around

When the last argument in a method's definition starts with an ampersand, it gives a name to the block that can then be referenced within the method.

``` ruby
def each_word(&block)
  ["hello", "world"].each { |word| yield word }
end

each_word { |w| puts w }
```

Note that that this isn't a real argument -- you can't explicitly pass in a proc to it.

``` ruby
each_word(lambda {})
#=> ArgumentError: wrong number of arguments (1 for 0)
```

When you give a name to a passed block, though, you can treat it as both a proc (invoking it with `call`) or as usual with `yield`. The two methods below do the same thing, though using `yield` is [significantly faster](http://stackoverflow.com/a/1410176/337184) than `call`.

``` ruby
def blocky_yield
  yield
end

def blocky_call(&block)
  block.call
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

print_stuff     #=> hello, world

print_stuff { |x| "stuff: #{x}" }
#=> stuff: hello
#=> stuff: world
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

### Blocks are just procs

``` ruby
def blocky(&block)
  block.class
end

block {}        #=> Proc
```

## Procs

Procs (short for procedures) are blocks of code that have been bound to a set of local variables. Once bound, the code may be called in different contexts and still access those variables.

Ruby 1.9 introduced `Kernel.proc` as an alias of `Proc.new`.

``` ruby
def times(factor)
  proc { |n| n * factor }
end

times(3).call(12)                       # => 36
times(5).call(5)                        # => 25
times(3).call(times(5).call(4))         # => 60
```

### `Symbol#to_proc`

``` ruby
(1..100).reduce { |acc, n| acc + n }    #=> 5050
tweets.map { |tweet| tweet.user }

(1..100).reduce(&:+)                    #=> 5050
tweets.map(&:user)

# But you can't do this:
tweets.map(&:user.name)
```

### Non-local returns

Procs return from the context in which they were defined.

``` ruby
def return_proc
  proc { return "Now you see me" }.call
  return "Now you don't!"
end

return_proc     #=> "Now you see me"
```

## Lambdas

``` ruby
def message_as(name)
  lambda { |message| puts "#{name}: #{message}" }
end

matz_messager = message_as("matz")
matz_messager.call "Hi there!"          # => matz: Hi there!
```

Lambdas and procs are *almost* identical.

``` ruby
lambda {}.class
#=> Proc
```

### Lambdas check the number of arguments; procs don't

``` ruby
proc { |x| x.class }.call
#=> NilClass

lambda { |x| x.class }.call
#=> ArgumentError: wrong number of arguments (0 for 1)
```

### Lambdas have localized returns; procs don't

``` ruby
def return_lambda
  lambda { return "Now you see me" }.call
  return "Now you don't"
end

return_lambda           #=> "Now you don't!
```

## The mysterious ampersand

``` ruby
def ampersandy(n)
  yield n
end

ampersandy(10) { |x| x + 10 }                   #=> 20

l = lambda { |x| x + 10 }
ampersandy(10, &l)                              #=> 20

ampersandy(10, lambda { |x| x + 10 })
#=> ArgumentError: wrong number of arguments (2 for 1)

ampersandy(10, &(lambda { |x| x + 10 }))        #=> 20
```
