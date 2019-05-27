import unittest
import collections
from tree import TreeNode


class Solution:
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        if not root:
            return []

        result = []
        dups = collections.defaultdict(list)

        def down(node, parent):
            node.parent = parent
            node.id = -1

            if node.left:
                down(node.left, node)
            if node.right:
                down(node.right, node)

            if not node.left and not node.right:
                dups[node.val].append(node)

        def up(dups):
            id = 1
            while dups:
                new_dups = collections.defaultdict(list)
                for nodes in dups.values():
                    if len(nodes) < 2:
                        continue
                    result.append(nodes[0])
                    for node in nodes:
                        parent = node.parent
                        if not parent:
                            continue
                        if node is parent.left:
                            right_id = parent.right.id if parent.right else 0
                            if right_id == -1:
                                node.id = id
                            else:
                                new_dups[(parent.val, id, right_id)].append(parent)
                        else:
                            left_id = parent.left.id if parent.left else 0
                            if left_id == -1:
                                node.id = id
                            else:
                                new_dups[(parent.val, left_id, id)].append(parent)
                    id += 1
                dups = new_dups

        down(root, None)
        up(dups)
        return result


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3, 4, None, 2, 4, None, None, 4], [
            [2, 4],
            [4],
        ])

    def _test(self, root, expected):
        root = TreeNode.from_array(root)

        actual = Solution().findDuplicateSubtrees(root)

        actual = [node.to_array() for node in actual]
        self.assertCountEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
