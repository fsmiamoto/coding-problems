from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
      length = self.listLen(head)

      if length == 1:
        return None

      count = length-n-1
      if count < 0:
        head = head.next
        return head

      node = head
      for _ in range(count):
        node = node.next

      next = node.next
      assert next is not None
      node.next= next.next

      return head

    def listLen(self, head: Optional[ListNode]) -> int:
      if not head:
        return 0
      return 1 + self.listLen(head.next)
