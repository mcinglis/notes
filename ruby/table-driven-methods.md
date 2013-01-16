# Lookup tables with lambdas

If you find yourself many `elsif`s or `case`s, consider using a table-driven method. Ruby provides excellent tools to make this easy to do.

Steve McConnell describes table-driven methods in *Code Complete* as:

> a scheme that allows you to look up information in a table rather than using logic statements to figure it out.

Table-driven methods take some time to become accustom to, but they do offer a few benefits:

1. Table-driven methods can provide a clear mapping between the default case and its result.
2. Table-driven methods can provide a clear mapping between special cases and their results.
3. Lookup tables can be easily made dynamic (e.g. based off user configuration) without sacrificing simplicity.

## Example: credit card countries

Consider this method that determines, based on the type of a credit card, what countries that card can be used in:

```ruby
def countries_usable_in
  case card_type
    when "mastercard"
      ["US", "UK", "IE"]
    when "visa"
      ["US", "UK", "IE"]
    when "discover"
      ["US"]
    when "maestro"
      ["UK"]
    end
  end
end
```

Using table-driven methods:

```ruby
CARD_TYPE_COUNTRIES = {
    "mastercard" => ["US", "UK", "IE"],
    "visa"       => ["US", "UK", "IE"],
    "discover"   => ["US"],
    "maestro"    => ["UK"]
}

def countries_usable_in
  CARD_TYPE_COUNTRIES[card_type]
end
```

But `visa` and `mastercard` map to the same list.

Ruby"s `Hash#new` can take a block that returns the value to use when the key is missing.

```ruby
CARD_TYPE_COUNTRIES = Hash.new { |_, _|
  # default
  ["US", "UK", "IE"]
}.merge {
  # special cases
  "discover" => ["US"],
  "maestro"  => ["UK"]
}
```

Now, suppose we have a new requirement to add American Express. Suppose that American Express isn't supported in African countries, but works everywhere else. Since we don't want to hardcode what countries are in Africa, we"ll need to consult the database.

The code below has two problems:

* the database query is only run on app startup, so any changes won't affect things until we restart
* we"re running a database query inside a class definition and we don't necessarily have a guarantee that the database connection is even established at that point

```ruby
DEFAULT_COUNTRIES = ["US", "UK", "IE"]
CARD_TYPE_COUNTRIES = Hash.new { |_, _|
  DEFAULT_COUNTRIES
}.merge {
  # special cases
  "discover"         => ["US"],
  "maestro"          => ["UK"],
  "american_express" => DEFAULT_COUNTRIES - Continent.find("Africa").countries
}
```

We need a lookup table that calculates its results on demand. Ruby has a structure for that: `lambda`.

```ruby
DEFAULT_COUNTRIES = ["US", "UK", "IE"]
CARD_TYPE_COUNTRIES = Hash.new { |_, _|
  DEFAULT_COUNTRIES
}.merge {
  # special cases
  "discover" => lambda {
    ["US"]
  },
  "maestro" => lambda {
    ["UK"]
  },
  "american_express" => lambda {
    DEFAULT_COUNTRIES - Continent.find("Africa").countries
  }
}

def countries_usable_in
  CARD_TYPE_COUNTRIES[card_type].call
end
```

## Command-line application

Suppose we need to determine the size of the user's terminal so that we can properly format output.

```ruby
def terminal_columns
  if ENV["COLUMNS"] =~ /^\s+$/
    ENV["COLUMNS"]
  elsif command_exists? "tput"
    `tput lines`.chomp.to_i
  elsif command_exists? "stty"
    parse_stty
  else
    DEFAULT_COLUMNS
  end
end
```

Lets use a lambda lookup table instead:

```ruby
TERMINAL_COLUMNS = [{
    test: lambda { ENV["COLUMNS"] =~ /^\s+$/ },
    value: lambda { ENV["COLUMNS"] }
  }, {
    test: lambda { command_exists? "tput" },
    value: lambda { `tput lines`.chomp.to_i }
  }, {
    test: lambda { command_exists? "stty" },
    value: lambda { parse_stty }
  }, {
    test: lambda { true },
    value: lambda { DEFAULT_COLUMNS }
}]

def terminal_columns
  TERMINAL_COLUMNS.find { |size| size[:test].call }.first[:value].call
end
```
