import unittest


class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        num_a = 0
        num_l = 0

        for ch in s:
            if ch == 'A':
                if num_a == 1:
                    return False
                num_a += 1
                num_l = 0
            elif ch == 'L':
                if num_l == 2:
                    return False
                num_l += 1
            else:
                num_l = 0
        return True


class Test(unittest.TestCase):
    def test(self):
        self._test('PPALLP', True)
        self._test('PPALLL', False)

    def _test(self, s, expected):
        actual = Solution().checkRecord(s)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
