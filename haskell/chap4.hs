-- recursive zip
zip' :: [a] -> [b] -> [(a,b)]
zip' _ [] = []
zip' [] _ = []
zip' (x:xs) (y:ys) = (x, y):zip' xs ys

-- quicksort

quicksort :: (Ord a) => [a] -> [a]
quicksort [] = [] --base case
quicksort (x:xs) = --recursive case
    let smallerOrEqual = [a | a <- xs, a <= x]
        larger = [a | a <- xs, a > x] --lolz got that wrong the first time
    in quicksort smallerOrEqual ++ [x] ++ quicksort larger    --set that pivottttttt

