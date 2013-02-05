# Variables

``` go
var x, y, z int
var c, python, java bool

func main() {
    fmt.Println(x, y, z, c, python, java)
    // 0 0 0 false false false
}
```

## Initializers

If an initializer is present, the type can be omitted; the variable will take the type of the initializer.

``` go
var x, y, z int = 1, 2, 3
var c, python, java = true, false, "no!"
```

## Short variable declarations

Inside a function, `:=` can be used in place of `var` with implicit type. Outside a function, every construct begins with a keyword so `:=` is not available.

``` go
func main() {
    var x, y, z int = 1, 2, 3
    c, python, java := true, false, "no!"
}
```

## Constants

Constants can be character, string, boolean or numeric values.

``` go
const pi = 3.14

func main() {
    const world = "世界"
    fmt.Println("Hello", world)
    fmt.Println("Happy", pi, "Day")
}
```

### Numeric constants

Numeric constants are high-precious values. An untyped constant takes the type needed by its context.

``` go
const (
    Big = 1 << 100
    Small = Big >> 9
)

func needInt(x int) int {
    return (x * 10) + 1
}

func needFloat(x float64) float64 {
    return x * 0.1
}

// needInt(Small) ==> 21
// needFloat(Small) ==> 0.2
// needInt(Big) ==> overflow error on compile
// needFloat(Big) ==> 1.267e+29
```

