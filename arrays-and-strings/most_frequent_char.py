'''
most frequent char

Write a function, most_frequent_char, that takes in a string as an argument. The function should return the most frequent character of the string. If there are ties, return the character that appears earlier in the string.

You can assume that the input string is non-empty.

most_frequent_char('bookeeper') # -> 'e'

most_frequent_char('david') # -> 'd'

most_frequent_char('abby') # -> 'b'

most_frequent_char('mississippi') # -> 'i'

most_frequent_char('potato') # -> 'o'

most_frequent_char('eleventennine') # -> 'e'

most_frequent_char('riverbed') # -> 'r'
'''
from collections import Counter

def most_frequent_char(s):
  return Counter(s).most_common(1)[0][0]
