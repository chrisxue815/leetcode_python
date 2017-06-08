import unittest


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        min_ = x if not self.stack or x < self.stack[-1][1] else self.stack[-1][1]
        self.stack.append((x, min_))

    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0] if self.stack else None

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1] if self.stack else None


class Test(unittest.TestCase):
    def test(self):
        stack = MinStack()
        stack.push(-2)
        stack.push(0)
        stack.push(-3)

        self.assertEqual(stack.top(), -3)
        self.assertEqual(stack.getMin(), -3)

        stack.pop()
        self.assertEqual(stack.top(), 0)
        self.assertEqual(stack.getMin(), -2)

        stack.pop()
        self.assertEqual(stack.top(), -2)
        self.assertEqual(stack.getMin(), -2)


if __name__ == '__main__':
    unittest.main()
