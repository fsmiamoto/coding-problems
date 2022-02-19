from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Recursive
    def _deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        head.next = self.deleteDuplicates(head.next)
        if head.next and head.val == head.next.val:
            return head.next
        else:
            return head

    # Iterative
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        prev, curr = dummy, head
        while curr and curr.next:
            if curr.val == curr.next.val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next
