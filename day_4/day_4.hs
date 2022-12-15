{-# LANGUAGE DataKinds #-}
import Prelude 
import Debug.Trace
import Data.List.Split
import qualified Data.Set as Set

-- Advent Of Code 2022
-- Day 4

test1 = "2-4,6-8\n2-3,4-5\n5-7,7-9\n2-8,3-7\n6-6,4-6\n2-6,4-8"
test2 = "2-4,6-8"
test3 = "1-10,2-4"
test4 = "12-91,13-90\n7-94,96-99\n5-85,5-81\n56-57,57-58\n26-26,27-98\n12-28,11-58\n11-32,10-32\n10-42,10-56\n46-63,38-62\n31-95,3-94\n76-82,41-75\n87-88,4-88\n21-33,20-32"
    

runTests =  do
  f <- readTestFile
  putStrLn $  testInput f
    

-- Read all of the test data from file
readTestFile :: IO String
readTestFile = readFile "./4.txt"

-- Count number of overlapping schedules given the string of section
-- assignment pairs.
-- 
-- Format: Assignment := "<bound 1>-<bound 2>"
--         Schedule   := "<Assignment>, <Assignment>"

testInput :: String -> String
testInput testStr = show $ foldr (\e r -> if e then r + 1 else r) 0 pLines
  where
    lines  = reverse $ drop 1 $ reverse $ splitOn "\n" testStr
    pLines = map isOverlap lines

-- getSpan "2-3" = [2,3]
-- getSpan "1-10" = [1 .. 10]
getSpan :: String -> [Integer]
getSpan s = [nums !! 0 .. nums !! 1]
  where nums = map (\x -> read x :: Integer) $ splitOn "-" s

-- parseLine "4-5,2-5" ==> [[4,5], [2,3,4,5]]
parseLine :: String -> [[Integer]]
parseLine s = [getSpan (scs !! 0), getSpan (scs !! 1)]
  where scs = splitOn "," s

-- isOverlap "1-4, 2-3" ==> True
isOverlap :: String -> Bool
isOverlap line =  (s1 `Set.isSubsetOf` s2) || (s2 `Set.isSubsetOf` s1) 
  where
    l = parseLine line
    s1 = Set.fromList $ l !! 0
    s2 = Set.fromList $ l !! 1
