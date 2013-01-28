
-- ## Basic functions

-- Append two lists.
-- If the first list is infinite, the result is the first list.
(++) :: [a] -> [a] -> [a]
(++) []     ys = ys
(++) (x:xs) ys = x : xs ++ ys

-- Extract the first element of a list, which must be non-empty.
head :: [a] -> a
head []     = errorEmptyList "head"
head (x:xs) = x

-- Extract the last element of a list, which must be finite and non-empty.
last :: [a] -> a
last []     = errorEmptyList "last"
last [x]    = x
last (x:xs) = last xs

-- Extract the elements after the head of a list, which must be non-empty.
tail :: [a] -> [a]
tail []     = errorEmptyList "tail"
tail (x:xs) = xs

-- Return all the elements of a list except the last one. The list must be
-- non-empty.
init :: [a] -> [a]
init []     = errorEmptyList "init"
init [x]    = []
init (x:xs) = x : init xs

-- Test whether a list is empty.
null :: [a] -> Bool
null []     = True
null (x:xs) = False

-- Returns the length of a finite list.
length :: Num n => [a] -> n
length []     = 0
length (x:xs) = 1 + length xs

-- ## Reducing lists (folds)

-- `foldl`, applied to a binary operator, a starting value (typically the
-- left-identity of the operator), and a list, reduces the list using the
-- binary operator, from left to right. The list must be finite.
foldl :: (a -> b -> a) -> a -> [b] -> a
foldl f x []     = x
foldl f x (y:ys) = foldl (f x y) ys

-- A variant of `foldl` that has no starting value argument, and thus must be
-- applied to non-empty lists.
foldl1 :: (a -> a -> a) -> [a] -> a
foldl1 f []     = errorEmptyList "foldl1"
foldl1 f (x:xs) = foldl f x xs

-- `foldr`, applied to a binary operator, a starting value (typically the
-- right-identity of the operator), and a list, reduces the list using the
-- binary operator, from right to left.
foldr :: (a -> b -> b) -> b -> [a] -> b
foldr f x []     = x
foldr f x (y:ys) = f y (foldr f x ys)

-- ## Special folds

-- Concatenates a list of lists.
concat :: [[a]] -> [a]
concat = foldr (++) []

-- ## List transformations

-- `map f xs` is the list obtained by applying `f` to each element of `xs`.
map :: (a -> b) -> [a] -> [b]
map f []     = []
map f (x:xs) = f x : map f xs

-- Returns the elements of a finite list in reverse order.
reverse :: [a] -> [a]
reverse []     = errorEmptyList "reverse"
reverse (x:xs) = foldl (flip (:)) []

-- Takes an element and a list and "intersperses" that element between the
-- elements of the list.
intersperse :: a -> [a] -> [a]
intersperse x []     = []
intersperse x [y]    = y
intersperse x (y:ys) = y : x : intersperse ys

-- Inserts `xs` in between the lists in `xss` and concatenates the result.
intercalate :: [a] -> [[a]] -> [a]
intercalate = concat . intersperse

-- Transposes the rows and columns of the given list of lists.
transpose :: [[a]] -> [[a]]
transpose []           = []
transpose ([]:xss)     = transpose xss
transpose ((x:xs):xss) = (x : [h | (h:_) <- xss]) : transpose (xs : [t | (_:t) <- xss])

-- ## Error code

-- Common up near-identical calls to `error` to reduce the number of constant
-- strings created when compiled.

errorEmptyList :: String -> a
errorEmptyList functionName =
  error (functionName ++ ": empty list")


