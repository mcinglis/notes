# The `new` function

The expression `new(T)` allocates a zeroed `T` value and returns a pointer to it.

``` go
type Vertex struct { X, Y int }

func main() {
    v := new(Vertex)
    fmt.Println(v)      // &{0 0}
    v.X, v.Y = 11, 9
    fmt.Println(v)      // &{11 9}
}
```
