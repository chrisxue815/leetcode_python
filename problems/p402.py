import unittest


class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if not k:
            return num
        n = len(num)
        stack = []
        for i in xrange(n):
            digit = num[i]
            while k and stack and ord(digit) < ord(stack[-1]):
                stack.pop()
                k -= 1
            stack.append(digit)
        hi = len(stack) - k
        lo = 0
        while lo < hi and stack[lo] == '0':
            lo += 1
        return ''.join(stack[lo:hi]) if lo < hi else '0'


class Test(unittest.TestCase):
    def test(self):
        self._test('1432219', 3, '1219')
        self._test('10200', 1, '200')
        self._test('10', 2, '0')
        self._test('10', 1, '0')
        self._test('123', 1, '12')

    def _test(self, num, k, expected):
        actual = Solution().removeKdigits(num, k)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
