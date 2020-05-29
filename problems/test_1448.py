import unittest
import utils
from tree import TreeNode


# O(n) time. O(log(n)) space. Recursive DFS, monotonic queue.
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = [[root.val, 1]]
        result = 1

        def dfs(curr):
            nonlocal result

            if not curr:
                return

            if curr.val >= q[-1][0]:
                result += 1
                if curr.val > q[-1][0]:
                    q.append([curr.val, 1])
                else:
                    q[-1][1] += 1
            else:
                q[-1][1] += 1

            dfs(curr.left)
            dfs(curr.right)

            q[-1][1] -= 1
            if q[-1][1] <= 0:
                q.pop()

        dfs(root.left)
        dfs(root.right)

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            root = TreeNode.from_array(case.args.root)
            actual = Solution().goodNodes(root)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
