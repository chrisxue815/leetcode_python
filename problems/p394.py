import unittest


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        stack = []
        buf = []
        i = 0
        k = 0
        while i < n:
            ch = s[i]
            if ch.isdigit():
                k = k * 10 + ord(ch) - ord('0')
            elif ch == '[':
                stack.append((buf, k))
                buf = []
                k = 0
            elif ch == ']':
                sub = ''.join(buf)
                buf, k = stack.pop()
                buf.append(sub * k)
                k = 0
            else:
                buf.append(ch)
            i += 1

        return ''.join(buf)


class Test(unittest.TestCase):
    def test(self):
        self._test('3[a]2[bc]', 'aaabcbc')
        self._test('3[a2[c]]', 'accaccacc')
        self._test('2[abc]3[cd]ef', 'abcabccdcdcdef')
        self._test('2[a2[bc]]gh2[cd]ef', 'abcbcabcbcghcdcdef')

    def _test(self, s, expected):
        actual = Solution().decodeString(s)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
