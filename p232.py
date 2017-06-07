import unittest


class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.push_stack = []
        self.pop_stack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.push_stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.pop_stack:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.pop_stack:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.pop_stack and not self.push_stack


class Test(unittest.TestCase):
    def test(self):
        que = MyQueue()
        que.push(1)
        que.push(2)
        que.push(3)

        self.assertEqual(que.pop(), 1)
        self.assertEqual(que.peek(), 2)
        self.assertEqual(que.empty(), False)

        self.assertEqual(que.pop(), 2)
        self.assertEqual(que.peek(), 3)
        self.assertEqual(que.empty(), False)

        que.push(4)

        self.assertEqual(que.pop(), 3)
        self.assertEqual(que.peek(), 4)
        self.assertEqual(que.empty(), False)

        self.assertEqual(que.pop(), 4)
        self.assertEqual(que.empty(), True)


if __name__ == '__main__':
    unittest.main()
