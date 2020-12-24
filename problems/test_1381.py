import unittest

import utils


class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.max_size = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) >= self.max_size:
            return

        self.stack.append([x, 0])

    def pop(self) -> int:
        stack = self.stack
        if not stack:
            return -1

        x, inc = stack.pop()

        if stack:
            stack[-1][1] += inc

        return x + inc

    def increment(self, k: int, val: int) -> None:
        if not self.stack:
            return

        k = min(k, len(self.stack))
        self.stack[k - 1][1] += val


class Test(unittest.TestCase):
    def test(self):
        cls = CustomStack
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
