import unittest


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_to_t = [0] * 256
        t_to_s = [0] * 256
        for a, b in zip(s, t):
            a, b = ord(a), ord(b)
            b2 = s_to_t[a]
            a2 = t_to_s[b]
            if b2 == 0:
                if a2 == 0:
                    s_to_t[a] = b
                    t_to_s[b] = a
                else:
                    return False
            elif b2 != b or a2 != a:
                return False
        return True


class Test(unittest.TestCase):
    def test(self):
        self._test('egg', 'add', True)
        self._test('foo', 'bar', False)
        self._test('paper', 'title', True)
        self._test('ab', 'aa', False)

    def _test(self, s, t, expected):
        actual = Solution().isIsomorphic(s, t)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
