'''
pair sum

Write a function, pair_sum, that takes in a list and a target sum as arguments. The function should return a tuple containing a pair of indices whose elements sum to the given target. The indices returned must be unique.

Be sure to return the indices, not the elements themselves.

There is guaranteed to be one such pair that sums to the target.

pair_sum([3, 2, 5, 4, 1], 8) # -> (0, 2)

pair_sum([4, 7, 9, 2, 5, 1], 5) # -> (0, 5)

pair_sum([4, 7, 9, 2, 5, 1], 3) # -> (3, 5)
'''

'''
This is my second attempt at the hash map method
described in the approach video.

This is a better approach as it now has a time complexity of O(n)
compared to O(n^2). It trades this for a space complexity of O(n),
vs the previous solution which had a space complexity of O(1).

This trade is always worth making.
'''

def pair_sum(numbers, target_sum):
  prev_values = {}
  for index, num in enumerate(numbers):
    compliment = target_sum - num
    if compliment in prev_values:
      return prev_values[compliment], index
    prev_values[num] = index
    

print(pair_sum([4, 7, 9, 2, 5, 1], 3)) # -> (3, 5)