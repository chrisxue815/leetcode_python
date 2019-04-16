import collections
import unittest

import utils


# O(R * C) time. O(R + C) space. BFS.
class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        result = []
        visited = [[False] * C for _ in range(R)]
        q = collections.deque()
        q.append((r0, c0))

        while q:
            r, c = q.popleft()

            if visited[r][c]:
                continue

            visited[r][c] = True
            result.append([r, c])

            if r >= 1 and not visited[r - 1][c]:
                q.append((r - 1, c))
            if r + 1 < R and not visited[r + 1][c]:
                q.append((r + 1, c))
            if c >= 1 and not visited[r][c - 1]:
                q.append((r, c - 1))
            if c + 1 < C and not visited[r][c + 1]:
                q.append((r, c + 1))

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().allCellsDistOrder(**case.args.__dict__)

            i = 0
            for expected in case.expected:
                self.assertCountEqual(expected, actual[i:i + len(expected)], msg=case.args)
                i += len(expected)


if __name__ == '__main__':
    unittest.main()
