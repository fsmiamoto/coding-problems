from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        middle = self.findMiddle(head)
        reversedSecondHalf = self.reverseList(middle.next)
        middle.next = None
        self.merge(head, reversedSecondHalf)


    def merge(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> None:
      while list1 and list2:
        nextInList1 = list1.next
        nextInList2 = list2.next

        list1.next = list2
        list2.next = nextInList1

        list1 = nextInList1
        list2 = nextInList2

    def findMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
      if not head:
        return None

      slow, fast = head, head
      while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next

      return slow

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      if not head:
        return None

      prev, curr = None, head
      while curr:
        next = curr.next
        curr.next = prev
        prev, curr = curr, next

      return prev
