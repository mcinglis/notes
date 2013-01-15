# Table-driven methods in Ruby

Steve McConnell describes table-driven methods in *Code Complete* as:

> a scheme that allows you to look up information in a table rather than using logic statements to figure it out.

Consider this method that determines, based on the type of a credit card, what countries that card can be used in:

```ruby
def countries_usable_in
  case card_type
    when 'master_card'
      ['US', 'UK', 'IE']
    when 'visa'
      ['US', 'UK', 'IE']
    when 'discover'
      ['US']
    when 'maestro'
      ['UK']
    end
  end
end
```

Using table-driven methods:

```ruby
def countries_usable_in
  {
    'master_card' => ['US', 'UK', 'IE'],
    'visa'        => ['US', 'UK', 'IE'],
    'discover'    => ['US'],
    'maestro'     => ['UK']
  }[card_type]
end
```

But `visa` and `master_card` map to the same list.

Ruby's `Hash#new` can take a block that returns the value to use when the key is missing.

```ruby
def countries_usable_in
  Hash.new { |_, _|
    ['US', 'UK', 'IE']
  }.merge({
    'discover' => ['US'],
    'maestro'  => ['UK']
  })[card_type]
end
```
