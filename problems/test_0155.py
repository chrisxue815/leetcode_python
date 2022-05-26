import unittest

import utils


class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        min_ = val if not self.stack or val < self.stack[-1][1] else self.stack[-1][1]
        self.stack.append((val, min_))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None


class Test(unittest.TestCase):
    def test(self):
        utils.test_invocations(self, __file__, MinStack)


if __name__ == '__main__':
    unittest.main()
