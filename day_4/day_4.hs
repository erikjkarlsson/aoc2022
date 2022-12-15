{-# LANGUAGE DataKinds #-}
import Prelude 
import Debug.Trace
import Data.List.Split
import qualified Data.Set as Set

-- Advent Of Code 2022
-- Day 4

-- Run tests from 4.txt on part 1
runTests1 =  do
  f <- readTestFile
  putStrLn $  testInput f

-- Run tests from 4.txt on part 2 
runTests2 =  do
  f <- readTestFile
  putStrLn $  testInput2 f

-- Read all of the test data from file
readTestFile :: IO String
readTestFile = readFile "./4.txt"

-- Count number of overlapping schedules given the string of section
-- assignment pairs.
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

-- Test input for part 2 
testInput2 :: String -> String
testInput2 testStr = show $ foldr (\e r -> if e then r + 1 else r) 0 pLines
  where
    lines  = reverse $ drop 1 $ reverse $ splitOn "\n" testStr
    pLines = map disjoint lines

-- Return True if the pairs on line intersect at any point
disjoint line =  not $ Set.disjoint s2 s1
  where
    l = parseLine line
    s1 = Set.fromList $ l !! 0
    s2 = Set.fromList $ l !! 1



