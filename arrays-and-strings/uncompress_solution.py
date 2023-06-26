# using two pointers

def uncompress(s):
  numbers = '0123456789'
  result = []
  i = 0
  j = 0
  while j < len(s):
    if s[j] in numbers:
      j += 1
    else:      
      num = int(s[i:j])
      # Using a list here produces a better time complexity compared with
      # concatinating strings as strings are immutable in Python.
      # Therefore, a new string needs to be created.
      result.append(s[j] * num)
      j += 1
      i = j
      
  return ''.join(result)

'''
    n = number of groups
    m = max num found in any group
    Time: O(n*m)
    Space: O(n*m)
'''
