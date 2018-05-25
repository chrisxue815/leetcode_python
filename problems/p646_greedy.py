import unittest
import utils


# O(nlog(n)) time. O(n) space. Sort, greedy.
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        if not pairs:
            return 0

        pairs.sort(key=lambda x: x[1])
        result = 1
        prev = pairs[0][1]

        for i in xrange(1, len(pairs)):
            if prev < pairs[i][0]:
                prev = pairs[i][1]
                result += 1

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p646.json').test_cases

        for case in cases:
            actual = Solution().findLongestChain(case.pairs)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
