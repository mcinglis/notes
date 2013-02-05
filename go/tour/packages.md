# Packages

Every Go program is made up of packages.

``` go
package main

import (
  "fmt"
  "math"
)

func main() {
  fmt.Println("Happy", math.Pi, "Day");
}
```

After importing a package, you can refer to the names it exports. In Go, a name is exported if it begins with a capital letter. This won't work:

``` go
import "math"
...
fmt.Println(math.pi)
```

Because `pi` is lower-case is can't be exported.
