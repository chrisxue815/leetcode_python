import collections
import unittest
import utils


# O(n) time. O(n) space. Hash table, math.
class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        return sum((count + answer) // (answer + 1) * (answer + 1) for answer, count in
                   collections.Counter(answers).iteritems())


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p781.json').test_cases

        for case in cases:
            actual = Solution().numRabbits(case.answers)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
