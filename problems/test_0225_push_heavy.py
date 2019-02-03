import unittest
from collections import deque


class MyStack(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._que = deque()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self._que.append(x)
        for i in range(len(self._que) - 1):
            self._que.append(self._que.popleft())

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self._que.popleft()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self._que[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self._que


class Test(unittest.TestCase):
    def test(self):
        stack = MyStack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(3, stack.pop())
        self.assertEqual(2, stack.top())
        self.assertEqual(False, stack.empty())

        self.assertEqual(2, stack.pop())
        self.assertEqual(1, stack.top())
        self.assertEqual(False, stack.empty())

        stack.push(4)

        self.assertEqual(4, stack.pop())
        self.assertEqual(1, stack.top())
        self.assertEqual(False, stack.empty())

        self.assertEqual(1, stack.pop())
        self.assertEqual(True, stack.empty())


if __name__ == '__main__':
    unittest.main()
