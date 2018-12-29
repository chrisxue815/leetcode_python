import unittest
import utils


# O(n) time. O(1) space. Two pointers, greedy.
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        if not s:
            return []

        result = []
        lo = 0
        lo_ch = ord(s[0])
        rightmost_index = [-1] * (ord('z') + 1)

        for hi in xrange(len(s) - 1, -1, -1):
            hi_ch = ord(s[hi])
            if rightmost_index[hi_ch] == -1:
                rightmost_index[hi_ch] = hi
            if hi_ch == lo_ch:
                break

        while lo < len(s):
            hi = rightmost_index[ord(s[lo])]
            i = lo
            while i < hi:
                ch = ord(s[i])
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
            actual = Solution().partitionLabels(case.s)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
