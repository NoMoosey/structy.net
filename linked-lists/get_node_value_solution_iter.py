def get_node_value(head, index):
  count = 0
  current = head
  while current is not None:
    if count == index:
      return current.val
    
    current = current.next
    count += 1
    
  return None

    # n = number of nodes
    # Time: O(n)
    # Space: O(1)
