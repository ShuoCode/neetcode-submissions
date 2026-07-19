# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # recursive method
        # recuse to the end to find the new reversed head
        # flip the pointer on the way back
        # Three aspects for recursive method:
        #   1. Base case
        #   2. recursive call
        #   3. Operations on the way back
        #   3. End case

        # Base case
        if not head:
            return head
        
        newHead = None
        # Recursive call
        if head.next:
            newHead = self.reverseList(head.next)
            # On the way back: flip the pointer
            head.next.next = head
            head.next = None
        else:
            # End case, where head.next == null, 
            # i.e. current head is the last node
            return head
        return newHead