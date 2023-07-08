'''
linked list values

Write a function, linked_list_values, that takes in the head of a linked list as an argument. The function should return a list containing all values of the nodes in the linked list.

Hey. This is our first linked list problem, so you should be liberal with watching the Approach and Walkthrough. Be productive! -AZ

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

linked_list_values(a) # -> [ 'a', 'b', 'c', 'd' ]

x = Node("x")
y = Node("y")

x.next = y

# x -> y

linked_list_values(x) # -> [ 'x', 'y' ]

q = Node("q")

# q

linked_list_values(q) # -> [ 'q' ]

linked_list_values(None) # -> [ ]
'''

def linked_list_values(head):
  results = []
  return create_results(head, results)

def create_results(head, results):
  if head is not None:
    results.append(head.val)
    print(results)
    create_results(head.next, results)
  return results