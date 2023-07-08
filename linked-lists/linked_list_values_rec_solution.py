# recursive

def linked_list_values(head):
  values = []
  _linked_list_values(head, values)
  return values

def _linked_list_values(head, values):
  if head is None:
    return
  values.append(head.val)
  _linked_list_values(head.next, values)

    # n = number of nodes
    # Time: O(n)
    # Space: O(n)
