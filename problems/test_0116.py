import unittest

import utils
from tree_link_node import Node


# O(n) time. O(1) space. Next right pointer traversal.
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        leftmost = root

        while leftmost.left:
            curr = leftmost

            while curr:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                curr = curr.next

            leftmost = leftmost.left

        return root


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution,
                   process_args=Node.from_root_array,
                   process_result=Node.to_next_value_array)


if __name__ == '__main__':
    unittest.main()
