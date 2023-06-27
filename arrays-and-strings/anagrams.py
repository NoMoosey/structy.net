'''
Write a function, anagrams, that takes in two strings as arguments. The function should return a boolean indicating whether or not the strings are anagrams. Anagrams are strings that contain the same characters, but in any order.

anagrams('restful', 'fluster') # -> True

anagrams('cats', 'tocs') # -> False
'''

def anagrams(s1, s2):
  char_list = [*s2]
  if len(s1) != len(s2):
    return False
  while char_list:
    for char in s1:
      if char in char_list:
        char_list.remove(char)
      else:
        return False
  return True

print(anagrams("a", "bad"))
print(anagrams('restful', 'fluster'))
print(anagrams("tacs", "cots"))