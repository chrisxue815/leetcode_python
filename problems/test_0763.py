import unittest
from typing import List

import utils


# O(n) time. O(1) space. Two pointers, greedy.
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        if not S:
            return []

        result = []
        lo = 0
        lo_ch = ord(S[0])
        rightmost_index = [-1] * (ord('z') + 1)

        for hi in range(len(S) - 1, -1, -1):
            hi_ch = ord(S[hi])
            if rightmost_index[hi_ch] == -1:
                rightmost_index[hi_ch] = hi

            if hi_ch == lo_ch:
                break

        while lo < len(S):
            hi = rightmost_index[ord(S[lo])]
            i = lo

            while i < hi:
                ch = ord(S[i])
                rightmost = rightmost_index[ch]
                if rightmost > hi:
                    hi = rightmost
                i += 1

            result.append(hi - lo + 1)
            lo = hi + 1

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().partitionLabels(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
