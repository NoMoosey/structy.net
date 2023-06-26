'''
Write a function, uncompress, that takes in a string as an argument. The input string will be formatted into multiple groups according to the following pattern:

<number><char>

for example, '2c' or '3a'.

The function should return an uncompressed version of the string where each 'char' of a group is repeated 'number' times consecutively. You may assume that the input string is well-formed according to the previously mentioned pattern.

ie: uncompress("2c3a1t") # -> 'ccaaat'

'''

import re

def uncompress(s):
  nums = re.findall("[0-9]+", s)
  chars = re.findall("[a-z]+", s)
  uncompressed = ''
  for index, char in enumerate(chars):
    uncompressed += char * int(nums[index])
  return uncompressed

uncompress("12j3k")