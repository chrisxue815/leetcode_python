import unittest


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        counts1 = [0] * 128
        counts2 = [0] * 128
        lo = 0

        for ch in s1:
            counts1[ord(ch)] += 1

        for hi, hi_ch in enumerate(s2):
            hi_ch = ord(hi_ch)
            counts2[hi_ch] += 1
            if counts2[hi_ch] == counts1[hi_ch]:
                if hi - lo + 1 == len(s1):
                    return True
            else:
                while counts2[hi_ch] > counts1[hi_ch]:
                    counts2[ord(s2[lo])] -= 1
                    lo += 1

        return False


class Test(unittest.TestCase):
    def test(self):
        self._test('ab', 'eidbaooo', True)
        self._test('ab', 'eidboaoo', False)
        self._test('aab', 'eidabbaooo', False)
        self._test('aab', 'eidaaabooo', True)
        self._test('adc', 'dcda', True)

    def _test(self, s1, s2, expected):
        actual = Solution().checkInclusion(s1, s2)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
