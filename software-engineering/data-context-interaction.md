# Data, context and interaction

* <http://en.wikipedia.org/wiki/Data,_context_and_interaction>
* <http://mikepackdev.com/blog_posts/24-the-right-way-to-code-dci-in-ruby>
* <http://mikepackdev.com/blog_posts/37-dci-the-king-of-the-open-closed-principle>
* <http://blog.codeclimate.com/blog/2012/12/19/dci-concerns-and-readable-code/>

DCI is an object-oriented paradigm that separates the domain model (data) from use cases (context) and roles that objects play (interaction).

DCI is complementary to model-view-controller (MVC), which is a pattern language used to separate data and its processing from its presentation.

DCI aims to:

* improve readability by giving behavior first-class status
* separate behavior from domain knowledge
* help developers reason about system state and behavior rather than object state and behavior
* support object-oriented thinking, rather than class-oritned thinking

The **data** are "what the system is." Data object interfaces are simple and minimal: just enough to capture the domain properties, but without operations that are unique to any particular scenario. The data should only consist of persistence-level methods, but never how the persisted data is used.

The **context** is the environment in which data objects execute their roles. There is always at least one context for every one user story. Depending on the complexity of the user story, there may be more than one context, possibly necessitating a story break-down. The goal of the context is to connect roles (what the system *does*) to data objects (what the system *is*).

The **interaction** is "what the system *does*". The interaction is implemented as roles which are played by objects at run time. These objects combine the state and methods of a data object with methods (but no state, as roles are stateless).

## Example

```ruby
# The data: no methods, just class-level definitions of persistence,
# association, and data validation. The ways in which Book is used should not
# be a concern of the Book model.
class Book
  include ActiveRecord::Validations

  validates :title, presence: true
end

# Roles play nicely with polymorphism. This Customer role could be played by
# any object who responds to the #cart method. The role itself never knows
# what type of object it will augment, leaving that decision up to the Context.
module Customer
  def add_to_cart(product)
    self.cart << product
  end
end

# A context is defined as a class. The act of instantiating an object and
# calling it's #call method is known as triggering.
class AddToCartContext

  # A context should expose the actors for which it is enabling. (@product
  # isn't an actor in this context, but it's exposed for completeness)
  attr_reader customer, product

  # Convenience method to aid in triggering the context
  def self.call(customer, product)
    self.new(customer, product).call
  end

  def initialize(roles)
    @customer = roles[:customer]
    @product = roles[:product]

    # The essence of DCI. Augmenting data objects with roles ad hoc is what
    # allows for strong decoupling.
    @customer.extend Customer
  end

  def call
    @customer.add_to_cart(@product)
  end
end
```

## Fitting into Rails

```ruby
class BookController < ApplicationController
  def add_to_cart
    AddToCartContext.call(
      customer: current_user,
      product: Book.find(params[:id]
    )
  end
end
```

Assuming `Book` was implemented to have a `#find` method.

## Testing

With RSpec and Capybara.

```ruby
describe "as a user" do
  it "has a link to add the book to my cart" do
    @book = Book.new(title: "Lean Architecture")
    visit book_path(book)
    page.should have_link('Add To Cart')
  end
end

describe Customer do
  let :customer { User.new }
  let :book { Book.new }

  before do
    customer.extend Customer
  end

  describe "#add_to_cart" do
    it "puts the book in the cart" do
      customer.add_to_cart book
      user.cart.should include(book)
    end
  end
end

describe AddToCartContext do
  let :user { User.new }
  let :book { Book.new }

  it "adds to book to the user's cart" do
    context = AddToCartContext.new(user, book)
    context.user.should_receive(:add_to_cart).with(context.book)
    context.call
  end
end
```

## Results

We've highly decoupled the functionality of the system from how the data is actually stored. This gives us the added benefit of compression and easy polymorphism.

We've created readable, well-organized code. It's easy to reason about the code both by the filenames and the algorithms within.

Our data model (what the system *is*) can remain stable while we progress and refactor Roles (what the system *does*).

We've come closer to representing the end-user's mental model.

**But**, we've added yet another layer of complexity. We have to keep track of contexts and roles on top of our traditional MVC. Contexts, specifically, exhibit more code.
