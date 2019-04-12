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
                   collections.Counter(answers).items())


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().numRabbits(**case.args._asdict())
            self.assertEqual(case.expected, actual, msg=case.args)


if __name__ == '__main__':
    unittest.main()
