import unittest
from collections import deque


class MyStack(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._que = deque()
        self._top = None

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self._que.append(x)
        self._top = x

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        for i in xrange(len(self._que) - 2):
            self._que.append(self._que.popleft())
        self._top = self._que.popleft()
        self._que.append(self._top)
        return self._que.popleft()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self._top

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

        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.top(), 2)
        self.assertEqual(stack.empty(), False)

        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.top(), 1)
        self.assertEqual(stack.empty(), False)

        stack.push(4)

        self.assertEqual(stack.pop(), 4)
        self.assertEqual(stack.top(), 1)
        self.assertEqual(stack.empty(), False)

        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.empty(), True)


if __name__ == '__main__':
    unittest.main()
