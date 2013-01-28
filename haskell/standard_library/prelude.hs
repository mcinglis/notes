
-- ## Miscellaneous functions

-- Identity function
id :: a -> a
id x = x

-- Constant function
const :: a -> b -> a
const x _ = x

-- Function composition
(.) :: (b -> c) -> (a -> b) -> a -> c
f . g = \x -> f (g x)

-- `flip f` takes its (first) two arguments in the reverse order of `f`.
flip :: (a -> b -> c) -> (b -> a -> c)
flip f x y = f y x

-- Application operator. This operator is redundant, since ordinary
-- application `(f x)` means the same thing as `(f $ x)`. However, `$` has
-- low, right-associative binding precedence, so it sometimes allows
-- parentheses to be omitted; for example:
--
--     f $ g $ h x = f (g (h x))
--
-- It is also useful in higher-order situations, such as `map ($ 0) xs`, or
-- `zipWith ($) fs xs`.
($) :: (a -> b) -> a -> b
f $ x = f x

until :: (a -> Bool) -> (a -> a) -> a -> a
until p f x | p x       = x
            | otherwise = until p f (f x)

