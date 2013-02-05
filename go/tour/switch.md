# Switch

A case body breaks automatically, unless it ends with a `fallthrough` statement.

``` go
func main() {
    fmt.Print("Go runs on ")
    switch os := runtime.GOOS; os {
    case "linux":
        fmt.Println("Linux.")
    case "darwin":
        fmt.Println("OS X.")
    default:
        fmt.Printf("%s.", os)
    }
}
```

Switch cases evaluate cases from top to bottom, stopping when a case succeeds.

``` go
switch i {
case 0:
case f():
}
// does not call f if i == 0
```

``` go
func main() {
    fmt.Println("When's Saturday?")
    today := time.Now().Weekday()
    switch time.Saturday {
    case today + 0:
        fmt.Println("Today.")
    case today + 1:
        fmt.Println("Tomorrow.")
    case today + 2:
        fmt.Println("In two days.")
    default:
        fmt.Println("Too far away.")
}
```

A switch without a condition is the same as `switch true`. This construct can be a clean way to write long `if-then-else` chains.
