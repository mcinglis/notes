# Modules

Modules must be imported before defining any functions, so imports are usually done at the top of the file.

``` haskell
import Data.List

-- All the functions that `Data.List` exports are now available in the
-- global namespace.

numUniques :: (Eq a) => [a] -> Int
numUniques = length . nub
```

## In GHCI

To "import" modules into the global namespace when using GHCI:

    ghci> :m + Data List

Or, to load several modules:

    ghci> :m + Data.List Data.Map Data.Set

However, if you've loaded a script that already imports a module, you don't need to use `:m +` to get access to it.

## Dealing with name clashes

``` haskell
-- Selective imports
import Data.List (nub, sort)

-- Exclusive imports
import Data.Char hiding (isUpper)

-- Qualified imports
import qualified Data.Map
-- `Data.Map` exports now accessible as `Data.Map.<name>`
import qualified Data.Map as M
-- `Data.Map` exports now accessible as `M.<name>`
```
