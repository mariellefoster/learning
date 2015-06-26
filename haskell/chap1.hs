doubleMe x = x + x


numList c = [x+y | x <- [1,2,3], y <- [10, 100,1000]]


removeNonUpperCase st = [ c | c <- st, c `elem` ['A'.. 'Z']]