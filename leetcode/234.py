from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow is at the middle of the list
        # start reversing
        curr = None
        while slow:
            next = slow.next
            slow.next = curr
            curr = slow
            slow = next


        start = head
        end = curr
        while start and end:
            if end.val != start.val:
                return False
            start = start.next
            end = end.next

        return True

