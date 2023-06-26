'''
Write a function, compress, that takes in a string as an argument. The function should return a compressed version of the string where consecutive occurrences of the same characters are compressed into the number of occurrences followed by the character. Single character occurrences should not be changed.

'aaa' compresses to '3a'
'cc' compresses to '2c'
't' should remain as 't'

You can assume that the input only contains alphabetic characters.

compress('ccaaatsss') # -> '2c3at3s'
'''

def compress(s):
  index_ptr = 0
  char_ptr = 0
  compressed_str = []
  while index_ptr < len(s):
    char = s[char_ptr]
    while char == s[index_ptr]:
        index_ptr += 1
        if not index_ptr < len(s):
          break
    num_of_chars = index_ptr - char_ptr
    # I was thinking it might be cleaner to append the # of chars and the chars
    # in two seperate append operations, then I could remove all of the `1` entries from
    # the list. I think the below is faster and more efficient, since we only need to
    # call the append method once.
    # Update: append operations to the end of a list are O(1)!
    if num_of_chars > 1:
      compressed_str.append(f'{num_of_chars}{char}')
    else:
      compressed_str.append(f'{char}')
    char_ptr = index_ptr
  return ''.join(compressed_str)


print(compress('ddoggooooos'))
