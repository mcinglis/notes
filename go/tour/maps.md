# Maps

A map maps keys to values.

Maps must be created with `make` (and not `new`) before use; the `nil` map is empty and cannot be assigned to.

``` go
type Vertex struct {
    Lat, Long float64
}

var m map[string] Vertex

func main() {
    m = make(map[string] Vertex)
    m["Bell Labs"] = Vertex{
        40.68433, -74.39967
    }
    fmt.Println(m)      // map[Bell Labs:{40.68433, -74.39967}]
    fmt.Println(m["Bell Labs"])
}
```

## Map literals

``` go
var m = map[string] Vertex {
    "Bell Labs": Vertex{ 40.68433, -74.39967 },
    "Google": Vertex{ 37.42202, -122.08408 },
}
```

If the top-level type is just a type name, you can omit it from the elements of the literal.

``` go
var m = map[string] Vertex {
    "Bell Labs": { 40.68433, -74.39967 },
    "Google": { 37.42202, -122.08408 },
}
```

## Mutating maps

``` go
// Insert or update
m[key] = elem

// Retrieve
elem = m[key]

// Test presence
elem, ok = m[key]
// If key is in m, ok is true
// If not, ok is false and elem is the zero value for its type

// Delete
delete(m, key)
```
