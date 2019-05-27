import collections
import unittest
import utils


# O(n) time. O(n) space. Hash table, math.
class Solution:
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
            args = str(case.args)
            actual = Solution().numRabbits(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
