def linked_list_find(head, target):
  current = head
  while current is not None:
    if current.val == target:
      return True
    current = current.next
  return False

    # n = number of nodes
    # Time: O(n)
    # Space: O(1)
