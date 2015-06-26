--Marielle Foster 2015 Notes and Code

-- :t tells you what type something is


-- The Eq type class are types that support equality testing
-- (==) :: Eq a => a -> a -> Bool
-- (/=) :: Eq a => a -> a -> Bool


-- The Ord type class is for types whose values can be put in an order
-- (<) :: Ord a => a -> a -> Bool
-- (>) :: Ord a => a -> a -> Bool
-- compare :: Ord a => a -> a -> Ordering


-- Show type class have values that can be represented as strings
-- show :: Show a => a -> String


-- Read type, opposite of Show
-- read :: Read a => String -> a


-- Enum instances are sequentially ordered types ex. () Bool, Char, Ordering, Int, Integer, Float, Double
-- succ :: Enum a => a -> a


-- Bounded types have an upper and lower bound
--minBound :: Bounded a => a
--maxBound :: Bounded a => a


--Num type has instances that can act like numbers
-- 20 :: Num a => a
-- (*) :: Num a => a -> a -> a
-- (-) :: Num a => a -> a -> a


--Floating type number
--(sin) :: Floating a => a -> a
--(cos) :: Floating a => a -> a
--(sqrt) :: Floating a => a -> a

--Integral type, only whole numbers
-- fromIntegral :: (Num b, Integral a) => a -> b




-- RANDOM
-- head :: [a] -> a
-- fst :: (a, b) -> a
-- last :: [a] -> a
