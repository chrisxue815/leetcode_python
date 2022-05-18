import unittest
from typing import List, Optional

import utils
from tree import TreeNode


# O(n*2) time. O(log(n)) space. DFS
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(preorder_index, inorder_left, inorder_right):
            if inorder_left >= inorder_right:
                return None

            root_val = preorder[preorder_index]

            for i in range(inorder_left, inorder_right):
                if inorder[i] == root_val:
                    break

            left_tree_size = i - inorder_left
            root = TreeNode(root_val)
            root.left = dfs(preorder_index + 1, inorder_left, i)
            root.right = dfs(preorder_index + left_tree_size + 1, i + 1, inorder_right)

            return root

        return dfs(0, 0, len(inorder))


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, process_result=TreeNode.to_array_static)


if __name__ == '__main__':
    unittest.main()
