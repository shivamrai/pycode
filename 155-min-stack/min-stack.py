class MinStack:

    def __init__(self):
        # Store (value, current_min_at_push) tuples to maintain O(1) min tracking
        self.minstack = []

    def push(self, val: int) -> None:
        if self.minstack:
            # Compute new min using previous top's stored min value
            current_min = self.minstack[-1][1]
            new_min = min(val, current_min)
            self.minstack.append((val, new_min))
        else:
            # First element: value is its own minimum
            self.minstack.append((val, val))

    def pop(self) -> None:
        # O(1) pop - min state preserved in remaining stack elements
        self.minstack.pop()

    def top(self) -> int:
        return self.minstack[-1][0]

    def getMin(self) -> int:
        return self.minstack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()