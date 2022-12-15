from functools import reduce
import functools as ft

test = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


def get_row(l, n):
  if len(l[0]) >= (1 + (n - 1) * 4):
    l1 = list(map(lambda x: x[1 + (n - 1) * 4], l))
    l2 = list(filter(lambda x: x != " ", l1))
    return l2[:-1]
  else:
    return None

def get_max_row(lines):
  for line in lines:
    if "[" in line:
      continue
    else:
      l1 = list(map(int, line.split("   ")))
      return reduce(lambda a, b: b if b > a else a, l1)


def gen_stacks(stacks_raw):
  stack = {} 

  for row in range(1, get_max_row(stacks_raw) + 1):
    stack[row] = get_row(stacks_raw, row)

  return stack

def run(indata):
  l1         = indata.split("\n\n")
  stacks_raw = l1[0].split("\n")
  moves      = l1[1].split("\n")
  stacks     = gen_stacks(stacks_raw)

  for move in parse_move(moves):
    exec_move(stacks, move)

  res = ""
  for t in stacks.keys():
    res += stacks[t][0]

  return res


def parse_move(lines):
  parsed = []
  for line in lines:
    if line == "\n": break
    else:
      l1 = line.split(" ")
      if l1 == [""]:  break
      l2 = list(filter(lambda a: a not in ["move", "from", "to"], l1))

      parsed.append( { "move": int(l2[0]),
                       "from": int(l2[1]),
                       "to": int(l2[2]) } )
      
  return parsed
    
      
def exec_move(stacks, move):
  "Move Nr amount of elements from from_row to to_row"

  nr       = move["move"]
  from_row = move["from"]
  to_row   = move["to"]
  
  elems            = stacks[from_row][:nr]
  stacks[from_row] = stacks[from_row][nr:]
  for e in elems:
    stacks[to_row].insert(0, e)
  

file_s = ""    
with open("5.txt") as f:
  file_s = f.read()

  

