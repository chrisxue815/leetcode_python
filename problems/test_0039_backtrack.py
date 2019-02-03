import unittest


class Solution(object):
    def __init__(self):
        self.candidates = None
        self.num_candidates = 0
        self.combination = []
        self.result = []

    def combinationSum(self, candidates, target):
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
        for i in range(start_index, self.num_candidates):
            candidate = self.candidates[i]

            if candidate == target:
                self.result.append(self.combination + [candidate])
                break
            elif candidate > target:
                break

            self.combination.append(candidate)
            self._combine(target - candidate, i)
            self.combination.pop()


class Test(unittest.TestCase):
    def test(self):
        self._test([2, 3, 6, 7], 7, [
            [7],
            [2, 2, 3],
        ])

    def _test(self, candidates, target, expected):
        actual = Solution().combinationSum(candidates, target)
        self.assertCountEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
