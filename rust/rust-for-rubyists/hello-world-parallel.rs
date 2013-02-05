use task::spawn;

fn main() {
  for 10.times {
    do spawn {
      io::println("Hello?");
    }
  }
}
