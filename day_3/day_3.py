import functools as ft
import numpy     as np

# Problems Day 3

# Rucksack
# - Two large compartments
# - Input is list of all items in rucksack
# - Each item is either lower or uppercase of item
#   'A' and 'a' are different items.
# - The compartment are represented as one half of the line
# - Each item can not appear in both compartments, but
#   multiple times in one compartments
# - Lowercase item types a through z have priorities 1 through 26.
# - Uppercase item types A through Z have priorities 27 through 52.


EXAMPLE_DATA = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".split("\n")


def load_test_data():
  "Load the file containing the test data, and return a list of all lines."
  s = ""
  with open("3.txt") as f:
    s = f.read()

  return s[:-1].split("\n")

def run_tests():
  "Run the tests on the problem" 
  test_data = load_test_data()

  t1 = ft.reduce(
    lambda a, b: a + b,
    list(map(lambda s: in_both(separate(s)), EXAMPLE_DATA)),
    0
  )

  if not t1 == 157:
    return False

  t2 = ft.reduce(
    lambda a, b: a + b,
    list(map(lambda s: in_both(separate(s)), test_data)),
    0
  )

  print(f"Answer 1 = {t2}")

  t3 = sum(list(map(in_group, make_groups(EXAMPLE_DATA))))

  if not t3 == 70:
    return False

  t4 = sum(list(map(in_group, make_groups(test_data))))

  print(f"Answer 2 = {t4}")
  
  return True


def in_both(compartments: (str, str)) -> int:
  "Return the sum of all chars appearing in both compartments."
  sum_of_prio = 0
  for c in set(compartments[0]):
    if c in compartments[1]:
      sum_of_prio += priority(c)
  return sum_of_prio


def make_groups(in_data: [str]):
  i      = 0
  groups = []

  while i + 3 <= len(in_data):
    groups.append(in_data[i : i + 3])
    i += 3

  return groups


def in_group(rucksacks: [str]) -> int:
  "Return the sum of all chars appearing in all groups of three elfs."
  sum_of_prio = 0

  for c in set(rucksacks[0]):
    if c in rucksacks[1] and c in rucksacks[2]: 
      sum_of_prio += priority(c)
      
  return sum_of_prio


def separate(in_data: str) -> (str, str):
  "Separate `in_data` into two compartments." 
  n = round( len(in_data) / 2 )
  return ( in_data[n:], in_data[:n] )


def priority(item: chr) -> int:
  "Return the priority of `item`."
  if item.isupper():
    return ord(item)  - ord('Z') + 26 * 2  
  else:
    return ord(item) - ord('z') + 26 

