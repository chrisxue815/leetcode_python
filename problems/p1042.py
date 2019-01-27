import unittest

import utils


def to_color(candidates):
    for i in xrange(1, 5):
        candidates >>= 1
        if candidates & 1:
            return i


# O(V+E) time. O(1) space. Four color theorem, graph, bit manipulation.
class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in xrange(N)]

        for x, y in paths:
            if x < y:
                x, y = y, x
            graph[x - 1].append(y - 1)

        colors = [0] * N

        for x in xrange(N):
            candidates = 0b11110
            for y in graph[x]:
                candidates &= ~(1 << colors[y])
            colors[x] = to_color(candidates)

        return colors


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().gardenNoAdj(**vars(case.args))
            self.check_answer(actual, case.args.paths)

    def check_answer(self, colors, paths):
        for x, y in paths:
            self.assertNotEqual(colors[x - 1], colors[y - 1])


if __name__ == '__main__':
    unittest.main()
