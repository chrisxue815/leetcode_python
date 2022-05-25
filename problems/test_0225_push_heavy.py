import collections
import unittest

import utils


class MyStack:

    def __init__(self):
        self._q = collections.deque()

    def push(self, x: int) -> None:
        q = self._q

        q.append(x)
        for _ in range(len(q) - 1):
            q.append(q.popleft())

    def pop(self) -> int:
        return self._q.popleft()

    def top(self) -> int:
        return self._q[0] if self._q else None

    def empty(self) -> bool:
        return not self._q


class Test(unittest.TestCase):
    def test(self):
        utils.test_invocations(self, __file__, MyStack)


if __name__ == '__main__':
    unittest.main()
