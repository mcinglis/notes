use core::*;

fn main() {
  for ["Alice", "Bob", "Carol"].each |&name| {
    do task::spawn {
      let shuffled_nums = rand::Rng().shuffle([1, 2, 3]);
      for shuffled_nums.each |&num| {
        io::print(fmt!("%s says: '%d'\n", name, num));
      }
    }
  }
}
