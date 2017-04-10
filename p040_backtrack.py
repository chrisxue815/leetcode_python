import unittest


class Solution(object):
    def __init__(self):
        self.candidates = None
        self.num_candidates = 0
        self.combination = []
        self.result = []

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.candidates = candidates
        self.num_candidates = len(candidates)

        self._combine(target, 0)

        return self.result

    def _combine(self, target, start_index):
        for i in xrange(start_index, self.num_candidates):
            candidate = self.candidates[i]

            if i > start_index and candidate == self.candidates[i - 1]:
                continue

            if candidate == target:
                self.result.append(self.combination + [candidate])
                break
            elif candidate > target:
                break

            self.combination.append(candidate)
            self._combine(target - candidate, i + 1)
            self.combination.pop()


class Test(unittest.TestCase):
    def test(self):
        self._test([10, 1, 2, 7, 6, 1, 5], 8, [
            [1, 7],
            [1, 2, 5],
            [2, 6],
            [1, 1, 6]
        ])

    def _test(self, candidates, target, expected):
        actual = Solution().combinationSum2(candidates, target)
        self.assertItemsEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
