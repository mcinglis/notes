# Structs

A `struct` is a collection of fields. `type` does what you'd expect.

``` go
type Vertex struct {
    X int
    Y int
}

func main() {
    fmt.Println(Vertex{1, 2})   // {1 2}
    v := Vertex{2, 3}
    v.X = 4
    fmt.Println(v.X)            // 4
}
```

## Struct literals

``` go
type Vertex struct { X, Y int }

var (
    p = Vertex{1, 2}    // has type Vertex
    q = &Vertex{1, 2}   // has type *Vertex
    r = Vertex{X: 1}    // Y:0 is implicit
    s = Vertex{}        // X:0 and Y:0
)

func main() {
    fmt.Println(p, q, r, s)     // {1 2} &{1 2} {1 0} {0 0}
}
```
