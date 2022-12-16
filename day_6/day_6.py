test1 = ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5)
test2 = ("nppdvjthqldpwncqszvftbrmjlhg", 6)
test3 = ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10)
test4 = ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11)

def parse_stream(data):
  "Parse as instructed for the first problem"
  buf  = data[:4]
  i    = 0

  while True:
    # incrementing i moves the buffer and rest forward
    buf  = data[i : 4 + i]
    
    # If current buffer is unique, the return
    # the index of the buffer [i + 4]
    if str_unique(buf):
      return i + 4
    else: i += 1

def parse_stream2(data):
  "Parse as instructed for the second problem"
  buf  = data[:14]
  i    = 0

  while True:
    # incrementing i moves the buffer and rest forward
    buf  = data[i : 14 + i]
    
    # If current buffer is unique, the return
    # the index of the buffer [i + 4]
    if str_unique(buf):
      return i + 14
    else: i += 1
    
    
def str_unique(s):
  "Return True if there are no duplicate chars in s, else False"
  
  seen_chars = 0
  char_val   = 0
  sftbuf     = 0

  for c in s:    
    char_val = ord(c)
    sftbuf   = (1 << char_val)

    if seen_chars & sftbuf > 0:
      return False      
    else:
      seen_chars |= sftbuf
      
  return True

with open("./6.txt") as f:
  res = parse_stream2(f.read())
  print(f"Found at: {res}")
