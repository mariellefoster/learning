-- swap the elements of a pair
swap :: (a,b) -> (b,a)

swap (a, b) = (b, a)

--Vector fun times
addVectors :: (Double, Double) -> (Double, Double) -> (Double, Double)
addVectors a b = (fst a + fst b, snd a + snd b)

--triples stuff
first :: (a, b, c) -> a
first (x, _, _) = x

