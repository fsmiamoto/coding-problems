from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Iterative
    def _removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev, curr = None, head
        result = head
        while curr:
            if curr.val == val:
                if not prev:
                    # Move the head
                    result = curr.next
                    curr = curr.next
                else:
                    prev.next = curr.next
                    curr = curr.next
            else:
                prev = curr
                curr = curr.next
        return result

    # Recursive
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head

        if head.val == val:
            return self.removeElements(head.next, val)

        head.next = self.removeElements(head.next, val)

        return head
