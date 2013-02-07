# Methods

Go does not have classes. However, you can define methods on struct types. The *method receiver* appears in its own argument list between the `func` keyword and the method name.

``` go
type Vertex struct {
    X, Y float64
}

func (v *Vertex) Abs() float64 {
    return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func main() {
    v := &Vertex{3, 4}
    fmt.Println(v.Abs())
}
```

You can define a method on *any* type you define in your package; not just structs. However, you can't define a method on a type from another package, or on a basic type.

``` go
type MyFloat float64

func (f MyFloat) Abs() float64 {
    if f < 0 {
        return float64(-f)
    }
    return float64(f)
}

func main() {
    f := MyFloat(-math.Sqrt2)
    fmt.Println(f.Abs())
}
```

## Pointer receivers

There are two reasons to use a pointer receiver. First, it avoids copying the value on each method call. Second, it allows the method to modify the value that its receiver points to.

``` go
type Vertex struct {
    X, Y float64
}

func (v *Vertex) Scale(f float64) {
    v.X = v.X * f
    v.Y = v.Y * f
}

func (v *Vertex) Abs() float64 {
    return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func main() {
    v := &Vertex{3, 4}
    v.Scale(5)
    fmt.Println(v, v.Abs())     // &{15 20} 25
}
```
