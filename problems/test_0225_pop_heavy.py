import unittest
import collections

import utils


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._q = collections.deque()
        self._top = None

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self._q.append(x)
        self._top = x

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        q = self._q

        for _ in range(len(q) - 2):
            q.append(q.popleft())

        if len(q) > 1:
            self._top = q.popleft()
            q.append(self._top)
        else:
            self._top = None

        return q.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self._top

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self._q


class Test(unittest.TestCase):
    def test(self):
        cls = MyStack
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
