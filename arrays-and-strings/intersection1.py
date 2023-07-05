'''
intersection

Write a function, intersection, that takes in two lists, a,b, as arguments. The function should return a new list containing elements that are in both of the two lists.

You may assume that each input list does not contain duplicate elements.

intersection([4,2,1,6], [3,6,9,2,10]) # -> [2,6]

intersection([2,4,6], [4,2]) # -> [2,4]

intersection([4,2,1], [1,2,4,6]) # -> [1,2,4]

intersection([0,1,2], [10,11]) # -> []

a = [ i for i in range(0, 50000) ]
b = [ i for i in range(0, 50000) ]
intersection(a, b) # -> [0,1,2,3,..., 49999]
'''

'''
This was my first attempt. I misunderstood that using the 'in'
operator against a list actually has an O(n) time complexity, 
as under the hood it is just iterating the list to check for
membership.

Instead, a 'set' should be used as all related operations are O(1).

'''

def intersection(a, b):
  if a == b:
    return a
  if len(a) >= len(b):
    matches = find_interseciton(a, b)
  else:
    matches = find_interseciton(b, a)
  return matches
    
def find_interseciton(short, compare):
  matches = []
  for num in compare:
    if num in short:
      matches.append(num)
  return matches
  
print(intersection([4,2,1,6], [3,6,9,2,10])) # -> [2,6]