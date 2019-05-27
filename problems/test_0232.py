import unittest


class MyQueue:
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

        self.assertEqual(1, que.pop())
        self.assertEqual(2, que.peek())
        self.assertEqual(False, que.empty())

        self.assertEqual(2, que.pop())
        self.assertEqual(3, que.peek())
        self.assertEqual(False, que.empty())

        que.push(4)

        self.assertEqual(3, que.pop())
        self.assertEqual(4, que.peek())
        self.assertEqual(False, que.empty())

        self.assertEqual(4, que.pop())
        self.assertEqual(True, que.empty())


if __name__ == '__main__':
    unittest.main()
