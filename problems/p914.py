import collections
import fractions
import unittest
import utils


# O(n) time. O(1) space. Math.
class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        counter = collections.Counter(deck)
        gcd = None

        for count in counter.itervalues():
            gcd = fractions.gcd(gcd, count) if gcd else count

            if gcd == 1:
                return False

        return True


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p914.json').test_cases

        for case in cases:
            actual = Solution().hasGroupsSizeX(case.deck)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
