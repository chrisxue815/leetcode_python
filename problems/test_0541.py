import unittest


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        chars = list(s)
        l = len(s)
        left = 0

        while left < l:
            reverse_len = min(k, l - left)
            right = left + reverse_len - 1
            for i in range(reverse_len // 2):
                chars[left + i], chars[right - i] = chars[right - i], chars[left + i]
            left = right + 1 + k

        return ''.join(chars)


class Test(unittest.TestCase):
    def test(self):
        self._test('123456', 3, '321456')
        self._test('1234567', 3, '3214567')
        self._test('12345678', 3, '32145687')
        self._test('123456789', 3, '321456987')
        self._test('1234567890', 3, '3214569870')

    def _test(self, s, k, expected):
        self.assertEqual(expected, Solution().reverseStr(s, k))


if __name__ == '__main__':
    unittest.main()
