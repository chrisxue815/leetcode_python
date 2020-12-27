import unittest

import utils
from tree import TreeNode


# O(log(n)) space.
class BSTIterator:

    def __init__(self, root: TreeNode):
        stack = []
        while root:
            stack.append(root)
            root = root.left
        self.stack = stack

    # O(1) time.
    def next(self) -> int:
        stack = self.stack
        if not stack:
            return 0

        cur = stack.pop()
        nxt = cur.right

        while nxt:
            stack.append(nxt)
            nxt = nxt.left

        return cur.val

    # O(1) time.
    def hasNext(self) -> bool:
        return len(self.stack) > 0


class Test(unittest.TestCase):
    def test(self):
        cls = BSTIterator
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            obj = None

            for func, parameters, expected in zip(case.functions, case.args, case.expected):
                if func == cls.__name__:
                    root = TreeNode.from_array(parameters[0])
                    obj = cls(root)
                else:
                    actual = getattr(obj, func)(*parameters)
                    self.assertEqual(expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
