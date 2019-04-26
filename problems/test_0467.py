import unittest

import utils


# O(n) time. O(1) space. String, DP.
class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        if not p:
            return 0

        lengths = [0] * 26
        lo = 0

        for hi in range(1, len(p)):
            if ord(p[hi - 1]) + 1 == ord(p[hi]) or p[hi - 1] == 'z' and p[hi] == 'a':
                continue

            start = ord(p[lo]) - ord('a')
            lengths[start] = max(lengths[start], hi - lo)
            lo = hi

        hi = len(p)
        start = ord(p[lo]) - ord('a')
        lengths[start] = max(lengths[start], hi - lo)

        count = [[0] * 26 for _ in range(26)]

        for start in range(26):
            max_length = lengths[start]
            if max_length == 0:
                continue

            for offset in range(max_length):
                q, r = divmod(max_length - offset, 26)
                lo = (start + offset) % 26

                for length in range(26):
                    hi = (lo + length) % 26
                    count[lo][hi] = max(count[lo][hi], q + (length < r))

        return sum(sum(c) for c in count)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().findSubstringInWraproundString(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
