import unittest
import utils
from tree import TreeNode


def merge(merged, distance, a, i):
    while i < len(a) and a[i][0] <= distance - 2:
        merged.append((a[i][0] + 1, a[i][1]))
        i += 1


# Recursive DFS.
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        result = 0

        def dfs(curr):
            if not curr.left and not curr.right:
                return [(1, 1)]

            left = dfs(curr.left) if curr.left else []
            right = dfs(curr.right) if curr.right else []

            if left and right:
                nonlocal result
                s = 0
                lh = left[0][0]
                for ri, (height, count) in enumerate(right):
                    if lh + height > distance:
                        ri -= 1
                        break
                    s += count

                li = 0
                while li < len(left) and ri >= 0:
                    result += left[li][1] * s
                    li += 1
                    if li < len(left):
                        lh = left[li][0]
                        while ri >= 0 and lh + right[ri][0] > distance:
                            s -= right[ri][1]
                            ri -= 1

            merged = []
            li = 0
            ri = 0
            while li < len(left) and ri < len(right):
                lh = left[li][0]
                rh = right[ri][0]
                if lh > distance - 2 or rh > distance - 2:
                    break
                if lh == rh:
                    merged.append((lh + 1, left[li][1] + right[ri][1]))
                    li += 1
                    ri += 1
                elif lh < rh:
                    merged.append((lh + 1, left[li][1]))
                    li += 1
                else:
                    merged.append((rh + 1, right[ri][1]))
                    ri += 1

            merge(merged, distance, left, li)
            merge(merged, distance, right, ri)

            return merged

        if root:
            dfs(root)

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            root = TreeNode.from_array(case.args.root)
            actual = Solution().countPairs(root, case.args.distance)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
