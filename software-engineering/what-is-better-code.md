# What is 'better' code?

http://www.naildrivin5.com/blog/2012/06/27/what-is-better-code.html

In decreasing order of frequency, code is *executed*, *read*, *changed*, and *written*.

Code that runs and passes its tests is the absolute minimum of acceptibility. Average developers typically stop at this point. If it works, ship it!

We aren't average developers. We want to do better.

## Readability

Readability of code is defined as how quickly someone can understand it. A good rule of thumb for defining "someone" is "any developer that could be hired to work here".

### Size

The more code you must evaluate, the longer it will take to come to an understanding.

Size means two things: length (number of lines) and density (information per line).

Short dense code can be just as difficult to understand as long sparse code.

Ruby and Scala communities tend to encourage shorter, denser programs.

Some densely-packed statements are idiomatic, and are easily understood, while others become impenetrable code golf.

### Variables

The more variables there are in the scope, the more abstract pieces of data you must hold in your head to understand the piece of code.

Descriptive and accurate variable names are important.

#### Bad: using instance variables to pass variables between methods

```ruby
class PeopleController < ApplicationController
  def destroy
    id = params[:id]
    @person = Person.find(id)
    if can_destroy?
      @person.destroy
      redirect_to persons_path
    else
      flash[:error] = @error
      redirect_to persons_path
    end
  end

  private

  def can_destroy?
    if @person.admin?
      @error = 'You cannot delete an admin'
      false
    elsif @person.orders.unfulfilled.any?
      @error = 'Person has unfullied orders'
      false
    else
      true
    end
  end
end
```

#### Good: keeping variables to a minimum scope

```ruby
class PeopleController < ApplicationController
  def destroy
    person = Person.find(params[:id])
    error = can_destroy?(person)
    if error.nil?
      person.destroy
      redirect_to persons_path
    else
      flash[:error] = error
      redirect_to persons_path
    end
  end

  private

  def can_destroy?(person)
    if person.admin?
      'You cannot delete an admin'
    elsif person.orders.unfulfilled.any?
      'Person has unfullied orders'
    else
      nil
    end
  end
end
```

### Number of classes and methods

If you need to follow the control flow through many methods or classes to get an understanding of some code, it's going to be harder to do so.

On the other hand, with fewer classes, you'll tend towards larger methods which, of course, can also be hard to understand.

### Paths through the code

Often referred to as 'complexity' in computer science, the number of possible paths of execution through a piece of code can greatly affect how easily a person can understand it.

Consider this method:

```ruby
def can_destroy?(person)
  errors = []
  if person.admin?
    errors << 'You cannot delete an admin'
  end
  if person.orders.unfulfilled.any?
    errors << 'Person has unfullied orders'
  end
  return errors.join(',')
end
```

There are two `if` statements here, which results in four possible ways through this code.

What if we needed to add a feature where employees are also not allowed to be destroyed in our controller?

```ruby
def can_destroy?(person)
  errors = []
  if person.admin? || person.is_employee?
    errors << 'You cannot delete an admin or employee'
  end
  if person.orders.unfulfilled.any?
    errors << 'Person has unfullied orders'
  end
  return errors.join(',')
end
```

We now have eight possible paths.

We can extract the first `if` statement's expression to a method to reduce the complexity of the code.

```ruby
class Person
  def deletable?
    person.admin? || person.is_employee?
  end
end

def can_destroy?(person)
  errors = []
  if person.deletable?
    errors << 'You cannot delete an admin or employee'
  end
  if person.orders.unfulfilled.any?
    errors << 'Person has unfulfilled orders'
  end
  return errors.join(',')
end
```

## Ability to change

When changing code, you need to know where to make the change. You also want to keep the scope of the change as small as possible.

**Coupling** is an indicator of the scope of a particular change. If two classes are tightly coupled, it means that a change in one is likely to necessitate a change in another.  A class that is coupled to many classes makes the system harder to change.

Ability to change conflicts with other facets of readability.
