import re

def uncompress(s):
  char_ptr = 0
  num_ptr = 0
  uncompressed = ''
  while char_ptr < len(s):
    while s[char_ptr].isnumeric():
      char_ptr += 1
    char = s[char_ptr]
    num = s[num_ptr:char_ptr]
    uncompressed += char * int(num)  # See solution as to why this might not be best
    char_ptr += 1
    num_ptr = char_ptr
  return uncompressed

print(uncompress("12j3k"))