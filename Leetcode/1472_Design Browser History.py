class BrowserHistory:
    # history = []
    # total = 0
    # curr = 0

    def __init__(self, homepage: str):
        BrowserHistory.history = []
        BrowserHistory.total = 0
        BrowserHistory.curr = 0
        BrowserHistory.history.append(homepage)

    def visit(self, url: str) -> None:
        BrowserHistory.curr += 1
        BrowserHistory.history.insert(BrowserHistory.curr, url)
        BrowserHistory.total = BrowserHistory.curr

    def back(self, steps: int) -> str:
        BrowserHistory.curr -= steps
        if BrowserHistory.curr < 0:
            BrowserHistory.curr = 0
        return BrowserHistory.history[BrowserHistory.curr]

    def forward(self, steps: int) -> str:
        BrowserHistory.curr += steps
        if BrowserHistory.curr > BrowserHistory.total:
            BrowserHistory.curr = BrowserHistory.total
        return BrowserHistory.history[BrowserHistory.curr]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
