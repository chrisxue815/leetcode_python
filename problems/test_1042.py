import unittest

import utils


def to_color(candidates):
    for i in range(1, 5):
        candidates >>= 1
        if candidates & 1:
            return i


# O(V+E) time. O(1) space. Four color theorem, graph, bit manipulation.
class Solution:
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in range(N)]

        for x, y in paths:
            if x < y:
                x, y = y, x
            graph[x - 1].append(y - 1)

        colors = [0] * N
        colors[0] = 1

        for x in range(1, N):
            candidates = 0b11110
            for y in graph[x]:
                candidates &= ~(1 << colors[y])
            colors[x] = to_color(candidates)

        return colors


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().gardenNoAdj(**case.args.__dict__)
            for x, y in case.args.paths:
                self.assertNotEqual(actual[x - 1], actual[y - 1], msg=args)


if __name__ == '__main__':
    unittest.main()
