def sum_list(head):
  total_sum = 0
  current = head
  while current is not None:
    total_sum += current.val
    current = current.next
  return total_sum

    # n = number of nodes
    # Time: O(n)
    # Space: O(1)
