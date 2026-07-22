# Dynamic Array
class BrowserHistory:

    def __init__(self, homepage: str):
        self.pages = [homepage]
        self.currIdx = 0

    def visit(self, url: str) -> None:
        if self.currIdx == len(self.pages) - 1:
            self.pages.append(url)
            self.currIdx += 1
        elif self.currIdx < len(self.pages) -1:
            self.currIdx += 1
            self.pages[self.currIdx] = url
            while self.currIdx < len(self.pages) - 1:
                self.pages.pop()

    def back(self, steps: int) -> str:
        self.currIdx = max(0, self.currIdx - steps)
        return self.pages[self.currIdx]
        

    def forward(self, steps: int) -> str:
        self.currIdx = min(len(self.pages) - 1, self.currIdx + steps)
        return self.pages[self.currIdx]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)