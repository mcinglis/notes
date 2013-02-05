# Pointers

Go has pointers, but no pointer arithmetic.

Struct fields can be accessed through a struct pointer. The indirection through the pointer is transparent.

``` go
type Vertex struct {
    X int
    Y int
}

func main() {
    p := Vertex{1, 2}
    q := &p
    q.X = 5
    fmt.Println(p, q)   // {5 2} &{5 2}
}
