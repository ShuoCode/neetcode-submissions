class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = ListNode(0)
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        curr = self.head
        for i in range(index+1):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val, None) 
        newNode.next = self.head.next
        self.head.next = newNode
        self.size += 1
        return None

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val, None)
        curr = self.head
        for i in range(self.size):
            curr = curr.next
        curr.next = newNode
        self.size += 1
        return None

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return None
        curr = self.head
        for i in range(index):
            curr = curr.next
        newNode = ListNode(val, curr.next)
        curr.next = newNode
        self.size += 1
        return None

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return None
        curr = self.head
        for i in range(index):
            curr = curr.next 
        curr.next = curr.next.next
        self.size -= 1
        return None
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)