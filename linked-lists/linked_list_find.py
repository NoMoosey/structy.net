class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def linked_list_find(head, target):
  if not head:
    return False
  elif head.val == target:
    return True
  return linked_list_find(head.next, target)

# Note that this recursive solution has an O(n) space complexity whereas the
# iterative solutino would only use O(1)! Both have an O(n) time complexity.