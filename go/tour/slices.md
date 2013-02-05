# Slices

A slice points to an array of values and also includes a length.

``` go
func main() {
    p := []int { 2, 3, 5, 7, 11, 13 }
    fmt.Println(p)      // [2 3 5 7 11 13]

    for i := 0; i < len(p); i++ {
        fmt.Printf("p[%d] == %d\n", i, p[i])
    }
}
```

Slices can be re-sliced, creating a new slice that points to the same array.

The expression `s[lo:hi]` evaluates to a slice of the elements from `lo` through `hi - 1` inclusive. Thus `s[x:x]` is empty and `s[x:x+1]` has one element.

``` go
func main() {
    p := []int { 2, 3, 5, 7, 11, 13 }

    fmt.Println(p[1:4])         // [3 5 7]

    // missing low index implies 0
    fmt.Println(p[:3])          // [2 3 5]

    // missing high index implies len(p)
    fmt.Println(p[3:])          // [7 11 13]
}
```

## Making slices

Slices are created with `make`; it allocates a zeroed array and returns a slice that refers to that array.

``` go
func main() {
    a := make([]int, 5)
    printSlice("a", a)          // a len=5 cap=5 [0 0 0 0 0]
    b := make([]int, 0, 5)
    printSlice("b", b)          // b len=0 cap=5 []
    c := b[:2]
    printSlice("c", c)          // c len=2 cap=5 [0 0]
    d := c[2:5]
    printSlice("d", d)          // d len=3 cap=3 [0 0 0]
}

func printSlice(s string, x []int) {
    fmt.Printf("%s len=%d cap=%d %v\n",
               s, len(x), cap(x), x)
}
```

## Nil slices

The zero value of a slice is `nil`. A nil slice has a length and capacity of 0.

``` go
func main() {
    var z []int
    fmt.Println(z, len(z), cap(z))      // [] 0 0
    if z == nil {
        fmt.Println("nil!")
    }
}
```
