import unittest

import utils


# Stack.
class MyQueue:

    # O(1) time. O(1) space.
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.push_stack = []
        self.pop_stack = []

    # O(1) time. O(1) space.
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.push_stack.append(x)

    # O(n) time. O(1) space.
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.refill_pop_stack()
        return self.pop_stack.pop()

    # O(n) time. O(1) space.
    def peek(self) -> int:
        """
        Get the front element.
        """
        self.refill_pop_stack()
        return self.pop_stack[-1]

    # O(n) time. O(1) space.
    def refill_pop_stack(self):
        if not self.pop_stack:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())

    # O(1) time. O(1) space.
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.push_stack and not self.pop_stack


class Test(unittest.TestCase):
    def test(self):
        utils.test_invocations(self, __file__, MyQueue)


if __name__ == '__main__':
    unittest.main()
