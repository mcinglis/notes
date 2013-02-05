# Functions

``` go
func add(x int, y int) int {
    return x + y
}

func main() {
    fmt.Println(add(42, 13))
}
```

When two or more consecutive named function parameters share a type, you can omit the type from all but the last. For example, the `add` function above can be shortened to:

``` go
func add(x, y int) int {
    return x + y
}
```

## Multiple results

A function can return any number of results.

``` go
func swap(x, y string) (string, string) {
    return y, x
}

func main() {
    a, b := swap("hello", "world")
    fmt.Println(a, b)   // prints "world hello"
}
```

Functions can return multiple "result parameters", not just a single value, and they can be named and act just like variables.

``` go
func split(sum int) (x, y int) {
    x = (sum * 4) / 9
    y = sum - x
    return
}

func main() {
    fmt.Println(split(17))
}
```

## Function values

``` go
func main() {
    hypotenuse := func(x, y float64) float64 {
        return math.Sqrt((x * x) + (y * y))
    }

    fmt.Println(hypotenuse(3, 4))       // 5
}
```

## Function closures

``` go
func adder() func(int) int {
    sum := 0
    return func(x int) int {
        sum += x
        return sum
    }
}

func main() {
    pos, neg = adder(), adder()
    for i := 0; i < 10; i++ {
        fmt.Println(pos(i), neg(-2 * i))        // 0 0, 1 -2, 3 -6 ...
    }
}
```
