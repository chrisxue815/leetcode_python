import unittest

import utils


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._push_stack = []
        self._pop_stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self._push_stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self._refill_pop_stack()
        return self._pop_stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        self._refill_pop_stack()
        return self._pop_stack[-1]

    def _refill_pop_stack(self):
        if not self._pop_stack:
            while self._push_stack:
                self._pop_stack.append(self._push_stack.pop())

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self._push_stack and not self._pop_stack


class Test(unittest.TestCase):
    def test(self):
        cls = MyQueue
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            obj = None

            for func, parameters, expected in zip(case.functions, case.args, case.expected):
                if func == cls.__name__:
                    obj = cls(*parameters)
                else:
                    actual = getattr(obj, func)(*parameters)
                    self.assertEqual(expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
