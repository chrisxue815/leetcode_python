import unittest
import utils

prime_numbers = {
    2, 3, 5, 7, 11, 13, 17, 19,
}


def bit_counts(r):
    counts = [0] * (r + 1)
    for x in xrange(1, r + 1):
        counts[x] = counts[x >> 1] + (x & 1)
    return counts


# O(n) time. O(n) space. DP.
class Solution(object):
    def countPrimeSetBits(self, l, r):
        """
        :type l: int
        :type r: int
        :rtype: int
        """
        count = 0
        counts = bit_counts(r)
        for num in xrange(l, r + 1):
            if counts[num] in prime_numbers:
                count += 1
        return count


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p762.json').test_cases

        for case in cases:
            actual = Solution().countPrimeSetBits(case.l, case.r)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
