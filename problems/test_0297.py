import collections
import unittest

import utils
from tree import TreeNode


class Codec:
    # O(n) time. O(n) space. BFS.
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        values = []
        q = collections.deque()
        q.append(root)

        while q:
            node = q.popleft()

            if node:
                values.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                values.append('#')

        while q and q[-1] == '#':
            q.pop()

        return ' '.join(map(str, values))

    # O(n) time. O(n) space. BFS.
    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        dummy = TreeNode(0)
        q = collections.deque()
        q.append((dummy, True))

        for val in data.split(' '):
            parent, is_left = q.popleft()

            if val == '#':
                continue

            node = TreeNode(int(val))

            if is_left:
                parent.left = node
            else:
                parent.right = node

            q.append((node, True))
            q.append((node, False))

        return dummy.left


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Codec, Codec.serialize,
                   process_args=TreeNode.from_root_array,
                   check_result=self.check_result)

    def check_result(self, case, actual, msg):
        expected = TreeNode.to_array_static(case.args.root)
        actual = TreeNode.to_array_static(Codec().deserialize(actual))
        self.assertEqual(expected, actual, msg)


if __name__ == '__main__':
    unittest.main()
