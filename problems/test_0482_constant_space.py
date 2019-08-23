import unittest

import utils


# O(n) time. O(1) space. Iteration, math.
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        num_alphanum = len(S) - S.count('-')
        if num_alphanum == 0:
            return ''

        num_dashes, first_group_len = divmod(num_alphanum - 1, K)
        first_group_len += 1

        dst = [' '] * (num_alphanum + num_dashes)
        si = 0
        group_len = first_group_len

        for di in range(len(dst)):
            if group_len > 0:
                while S[si] == '-':
                    si += 1
                dst[di] = S[si].upper()
                si += 1
                group_len -= 1
            else:
                dst[di] = '-'
                group_len = K

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
