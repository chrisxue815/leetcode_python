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

    # Amortized O(1) time.
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
        utils.test_invocations(self, __file__, BSTIterator, process_args=self.process_args)

    @staticmethod
    def process_args(func, parameters):
        if func == BSTIterator.__name__:
            parameters[0] = TreeNode.from_array(parameters[0])


if __name__ == '__main__':
    unittest.main()
