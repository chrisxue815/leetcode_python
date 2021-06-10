import collections
import unittest

import utils


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._q = collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        q = self._q

        q.append(x)
        for _ in range(len(q) - 1):
            q.append(q.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self._q.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self._q[0] if self._q else None

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self._q


class Test(unittest.TestCase):
    def test(self):
        utils.test_invocations(self, __file__, MyStack)


if __name__ == '__main__':
    unittest.main()
