# My personal style guide

Taken mostly from [GitHub's Ruby style guide](//github.com/styleguide/ruby).

## Coding style

Indent with two spaces.

Keep lines fewer than 80 characters.

Never leave trailing whitespace.

Use spaces around operators and curly braces `{` `}`, and after comas.

```ruby
sum = 1 + 2
a, b = 1, 2
[1, 2, 3].each { |e| puts e }
```

No spaces around `(`, `[` or before `]`.

```ruby
some(arg).other
[1, 2, 3].length
```

Use parentheses for method invocations on objects, except when no arguments are being passed.

```ruby
john.talk
john.eat(green, eggs, ham)
```

Indent `when` and `else` as deep as the corresponding `case`.

```ruby
case
when song.name == 'Misty'
  puts "Not again!"
when song.duration > 120
  puts "Too long!"
when Time.now.hour > 21
  puts "It's too late"
else
  song.play
end

kind = case year
       when 1850..1889 then 'Blues'
       when 1890..1909 then 'Ragtime'
       when 1910..1929 then 'New Orleans Jazz'
       when 1930..1939 then 'Swing'
       else 'Jazz'
       end
```

Separate method definitions with one line. Use blank lines sparingly within methods to break it up into logical paragraphs; this is usually a sign that the method should be broken up, though.

```ruby
def some_method
  data = initialize(options)
  # ...

  data.manipulate!

  data.result
end

def some_other_method
  result
end
```

## Naming

Use `snake_case` for methods and variables.

Use `CamelCase` for classes and modules, but keep acronyms like `HTTP`, `RFC`, `XML` uppercase.

Use `SCREAMING_SNAKE_CASE` for other constants.

The names of predicate methods (methods that return a boolean value) should end in a question mark (e.g., `Array#empty?`).

The names of potentially "dangerous" methods (e.g. methods that modify `self` or the arguments, `exit!`, etc.) should end with an exclamation mark. Bang methods should only exist if a non-bang method exists. ([more on this](http://dablog.rubypal.com/2007/8/15/bang-methods-or-danger-will-rubyist))

## Syntax

Use `def` with parentheses when there are arguments. Omit the parentheses when there are no arguments.

```ruby
def some_method
end

def with_arguments(arg1, arg2)
end
```

Never use `for`, unless you know exactly why.

Never use `then` for `if` or `unless`.

Only use the ternary operator where all expressions are extremely trivial.

```ruby
# bad
result = if some_condition then something else something_else end

# bad - unless the expressions aren't trivial
result = if some_condition
           something
         else
           something_else
         end

# good
result = some_condition ? something : something_else
```

Never use `unless` with `else`. Rewrite it with the positive case first.

Don't use parentheses around conditional expressions, unless the expression contains an assignment.

```ruby
# bad
if (x > 10)
end

# good
if x > 10
end

# good
if (x = next_line)
end
```

Use `{`/`}` for single-line blocks, and `do`/`end` for multi-line blocks.

```ruby
names.each { |name| puts name }

names.each do |name|
  # multiple lines
end
```

Use block chaining sparingly, but if you do, use `do` and `end`. Most block chains should be refactored.

```ruby
names.select do |name|
  name.start_with?("S")
end.map do |name|
  name.upcase
end
```

## Strings

Always use double-quoted strings, so that interpolation and escaping will always work.

Avoid using `+` on strings; it creates a bunch of new string objects. Instead, prefer the `<<` operator, which mutates the string in-place.

```ruby
html = '<h1>Page title</h1>'
paragraphs.each do |paragraph|
    html << "<p>#{paragraph}</p>"
end
```

Use `%w` freely for string arrays.

```ruby
STATES = %w(draft open closed)
```

Use `%()` for single-line strings which require both interpolation and embedded double quotes. For multi-line strings, prefer heredocs.

```ruby
%(<tr><td class="name">#{name}</td>)

<<END
Lorem "ipsum dolor" sit amet,
consectetur adipisicing #{elit}.
END
```

## Regular expressions

Avoid using `$1` to `$9`. Prefer named groups instead.

```ruby
# bad
/(regexp)/ =~ string
process $1

# good
/(?<name>regexp)/ =~ string
process name
```

Be careful with `^` and `$` as they only match the start and end of a line, not string endings. If you want to match the whole string, use `\A` and `\Z`.

Use the `x` modifier for complex regular expressions where it can make them more readable. You can also add useful comments. Be careful though, because spaces are ignored.

```ruby
regexp = %r{
    start           # some text
    \s              # whitespace character
    (group)         # first group
    (?:alt1|alt2)   # some alternation
    end
}x
```

Use `%r` only for regular expressions matching *more than one* `/` character.

```ruby
# good
%r(^/blog/2011/(.*)$)

# bad
%r(\s+)

# bad
%r(^/(.*)$)
# should be
/^\/(.*)$/
```
