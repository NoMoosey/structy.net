def sum_list(head):
  if head is None:
    return 0
  return head.val + sum_list(head.next)

    # n = number of nodes
    # Time: O(n)
    # Space: O(n)
