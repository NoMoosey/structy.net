'''
pair sum

Write a function, pair_sum, that takes in a list and a target sum as arguments. The function should return a tuple containing a pair of indices whose elements sum to the given target. The indices returned must be unique.

Be sure to return the indices, not the elements themselves.

There is guaranteed to be one such pair that sums to the target.

pair_sum([3, 2, 5, 4, 1], 8) # -> (0, 2)

pair_sum([4, 7, 9, 2, 5, 1], 5) # -> (0, 5)

pair_sum([4, 7, 9, 2, 5, 1], 3) # -> (3, 5)
'''

# This is my initial pass, which it seems in the brute force
# approach, as this has a time complexity of O(n^2) due to the 
# nested `for` loops.

def pair_sum(numbers, target_sum):
  # Tracking the index manually as the .index()
  # method will always return the first index
  # if there are duplicate numbers in the list
  i_index = 0
  j_index = 0
  for i in numbers:
    for j in numbers:
      if (j_index != i_index and i + j == target_sum):
        return (i_index, j_index)
      j_index += 1
    j_index = 0
    i_index += 1
    

print(pair_sum([4, 7, 9, 2, 5, 1], 3)) # -> (3, 5)