'''
sum list

Write a function, sum_list, that takes in the head of a linked list containing numbers as an argument. The function should return the total sum of all values in the linked list.

a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e

# 2 -> 8 -> 3 -> -1 -> 7

sum_list(a) # 19

x = Node(38)
y = Node(4)

x.next = y

# 38 -> 4

sum_list(x) # 42

z = Node(100)

# 100

sum_list(z) # 100

sum_list(None) # 0
'''

# I didn't get this one working on my own.