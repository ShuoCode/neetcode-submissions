# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # A few problems need to be solved
        # 1. for merging two lists, we need a node to start with - dummy node
        # 2. how to deal with one of the list reaches to the end - attach the rest of nodes from the other non-end list to the result list
        # 3. one concern: will a new list cost too much space waste?
        #       answer: no, because it is singly nodes who constitue the list, 
        #               so the so called "merging" is actually the modification of these nodes' next pointers
        #               of course, this is because the problem doesn't ask for reserving the original two lists, 
        #               which means we can break the original lists' and modify these nodes' pointers
        # 4. to insert new node to the merged list, we need a pointer reference to the last node in the list
        # 5. to be able to return the new merged list, we need a pointer to stay at the beginning of the list
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next



