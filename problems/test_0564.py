import unittest

import utils


# O(4^n) time. O(n) space. Partition problem, backtracking.
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        k = len(n)
        candidates = {10 ** (k - 1) - 1, 10 ** k + 1}

        n_prefix = int(n[:(k + 1) // 2])

        for i in range(-1, 2):
            prefix = str(n_prefix + i)
            if k & 1:
                suffix = prefix[:-1]
            else:
                suffix = prefix
            candidates.add(int(prefix + suffix[::-1]))

        n = int(n)
        candidates.discard(n)

        return str(min(candidates, key=lambda x: (abs(x - n), x)))


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().nearestPalindromic(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
