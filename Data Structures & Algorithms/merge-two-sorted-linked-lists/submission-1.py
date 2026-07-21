# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # This is a solution where no dummy node used
        # This is a recursion method

        # Base case
        if not list1:
            return list2
        if not list2:
            return list1

        # recursion
        # keep the smaller node, 
        # and point its pointer to the sorted list of the rest of two linked list
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        