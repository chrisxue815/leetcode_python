import collections
import unittest
from typing import Optional

import utils
from tree import TreeNode


# BFS.
class CBTInserter:

    # O(n) time. O(n) space.
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.q = q = collections.deque()
        q.append(root)
        while True:
            curr = q[0]
            if curr.left:
                q.append(curr.left)
            else:
                break
            if curr.right:
                q.append(curr.right)
            else:
                break
            q.popleft()

    # O(1) time. O(1) space.
    def insert(self, val: int) -> int:
        curr = self.q[0]
        new_node = TreeNode(val)
        if curr.left:
            curr.right = new_node
            self.q.popleft()
        else:
            curr.left = new_node
        self.q.append(new_node)
        return curr.val

    # O(1) time. O(1) space.
    def get_root(self) -> Optional[TreeNode]:
        return self.root


class Test(unittest.TestCase):
    def test(self):
        utils.test_invocations(self, __file__, CBTInserter, process_args=self.process_args,
                               process_result=self.process_result)

    @staticmethod
    def process_args(func, parameters):
        if func == CBTInserter.__name__:
            parameters[0] = TreeNode.from_array(parameters[0])

    @staticmethod
    def process_result(func, actual):
        if func == CBTInserter.get_root.__name__:
            return TreeNode.to_array_static(actual)
        return actual


if __name__ == '__main__':
    unittest.main()
