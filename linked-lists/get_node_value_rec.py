class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def get_node_value(head, index, index_ptr=0):
  if not head:
    return
  if index_ptr == index:
    return head.val
  index_ptr += 1
  return get_node_value(head.next, index, index_ptr=index_ptr)

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(get_node_value(a, 2)) # 'c'