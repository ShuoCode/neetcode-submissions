class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = ListNode(homepage, None, None)
        self.curr = self.homepage

    def visit(self, url: str) -> None:
        newPage = ListNode(url, None, None)
        self.curr.next = newPage
        newPage.prev = self.curr
        self.curr = newPage
        return None
        

    def back(self, steps: int) -> str:
        while steps and self.curr.prev:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val
        

    def forward(self, steps: int) -> str:
        while steps and self.curr.next:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)