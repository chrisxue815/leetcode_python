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
            nonlocal result

            left = dfs(curr.left) if curr.left else []
            right = dfs(curr.right) if curr.right else []

            if left and right:
                rsum = []
                s = 0
                for height, count in right:
                    if left[0][0] + height > distance:
                        break
                    s += count
                    rsum.append((height, s))

                li = 0
                ri = len(rsum) - 1
                while li < len(left) and ri >= 0:
                    result += left[li][1] * rsum[ri][1]
                    li += 1
                    if li < len(left):
                        while ri >= 0 and left[li][0] + rsum[ri][0] > distance:
                            ri -= 1

            if not curr.left and not curr.right:
                return [(1, 1)]
            else:
                merged = []
                li = 0
                ri = 0
                while li < len(left) and ri < len(right):
                    if left[li][0] > distance - 2 or right[ri][0] > distance - 2:
                        break
                    if left[li][0] == right[ri][0]:
                        merged.append((left[li][0] + 1, left[li][1] + right[ri][1]))
                        li += 1
                        ri += 1
                    elif left[li][0] < right[ri][0]:
                        merged.append((left[li][0] + 1, left[li][1]))
                        li += 1
                    else:
                        merged.append((right[ri][0] + 1, right[ri][1]))
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
