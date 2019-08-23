import unittest

import utils


# O(n) time. O(1) space. Iteration, math.
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        num_alphanum = sum(1 for c in S if c != '-')
        if num_alphanum == 0:
            return ''

        num_dashes, first_group_len = divmod(num_alphanum, K)
        if first_group_len == 0:
            first_group_len = K
            num_dashes -= 1

        dst = ['_'] * (num_alphanum + num_dashes)
        si = 0
        di = 0

        for _ in range(first_group_len):
            while S[si] == '-':
                si += 1
            dst[di] = S[si].upper()
            si += 1
            di += 1

        for _ in range(num_dashes):
            dst[di] = '-'
            di += 1

            for _ in range(K):
                while S[si] == '-':
                    si += 1
                dst[di] = S[si].upper()
                si += 1
                di += 1

        return ''.join(dst)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().licenseKeyFormatting(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
