# ActiveRecord callbacks

* [DevMynd - ActiveRecord callbacks](http://www.devmynd.com/blog/2013-2-effective-rails-part-1-activerecord-callbacks)

The callbacks below are dependent on the order in which they are processed.

``` ruby
# app/models/order.rb

class Order < ActiveRecord::Base

  has_many :line_items
  has_many :coupons

  before_save :update_weight, :update_shipping_cost, :update_total

  def update_weight
    self.total_weight = line_items.pluck(:weight).reduce(:+)
  end

  def update_shipping_cost
    self.shipping_cost = ShippingCalculator.get_cost(self.total_weight)
  end

  def update_total
    sub_total = line_items.pluck(:price).reduce(:+)
    percent_off = coupons.max_by(&:percent_off)
    discount = sub_total * percent_off
    self.total_cost = (shipping_cost + sub_total) - discount
  end

end
```

The design below makes the ordering dependency explicit, and reveals the intention of the component methods. We're alright to continue using a callback in this case because we're only changing data within the model itself. With this approach we can still call and test each component individually.

``` ruby
# app/models/order.rb

class Order < ActiveRecord::Base

  has_many :line_items
  has_many :coupons

  before_save :update_totals

  def update_totals
    update_weight
    update_shipping_cost
    update_total
  end

  def update_total
    self.total_cost = (shipping_cost + sub_total) - discount
  end

  def update_weight
    self.total_weight = line_items.pluck(:weight).reduce(:+)
  end

  def update_shipping_cost
    self.shipping_cost = ShippingCalculator.get_cost(self.total_weight)
  end

  def sub_total
    line_items.pluck(:price).reduce(:+)
  end

  def discount
    sub_total * coupons.max_by(&:percent_off)
  end

end
```

We could improve on this further by moving these disparate concerns to service classes.

## External effects

It's usually bad to use callbacks to interact with outside systems. It's bug-prone and hard to test.

``` ruby
# app/models/comment.rb

class Comment < ActiveRecord::Base

  belongs_to :post
  belongs_to :user

  after_save :update_comment_count, :send_to_twitter, :send_email_notification

  def send_to_twitter
    Twitter.post "#{user} commented: #{body}"
  end

  def send_email
    CommentMailer.new_comment_email(self).deliver
  end

  def update_comment_count
    post.comment_count = Comment.where(post_id: post.id).count
    post.save
  end

end
```

With this design, ssers will actually receive two emails now, because the `Post` model also has an `after_save` callback to send an email.

Also, although it's not obvious, we can't call `save` on a comment without sending an email, posting to Twitter, and updating the count. This makes testing hard, where side-effects need to be kept to a minimum.

Here's a refactoring that attempts to solve these problems.

``` ruby
# app/models/comment.rb
class Comment < ActiveRecord::Base
  belongs_to :post
  belongs_to :user

  after_save :update_comment_count

  def update_comment_count
    post.update_comment_count!
  end
end

# app/services/creates_comments.rb
class CommentCreator
  attr_reader :post, :user

  def initialze(post, user)
    @post = post
    @user = user
  end

  def create(attrs)
    Comment.create attrs.merge(user: user, post: post)
  end

  def create_and_notify(comment_attrs)
    comment = create(comment_attrs)
    tweet comment
    email comment
    comment
  end

  def tweet(comment)
    Twitter.post "#{user} commented: #{comment}"
  end

  def email(comment)
    CommentMailer.new_comment_email(self).deliver
  end
end

# app/controllers/comments_controller.rb
class CommentsController
  def create
    post = Post.find(params[:id])
    creator = CommentCreator.new(post, current_user)
    creator.create_and_notify params[:comment]
    redirect_to post_path(post), notice: "Comment added!"
  end
end
```

