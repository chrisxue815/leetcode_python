import unittest


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}
        s = list(s)
        lo = 0
        hi = len(s) - 1

        while True:
            while lo < hi:
                if s[lo].lower() in vowels:
                    break
                lo += 1
            else:
                break

            while lo < hi:
                if s[hi].lower() in vowels:
                    break
                hi -= 1
            else:
                break

            s[lo], s[hi] = s[hi], s[lo]
            lo += 1
            hi -= 1

        return ''.join(s)


class Test(unittest.TestCase):
    def test(self):
        self._test('hello', 'holle')
        self._test('leetcode', 'leotcede')

    def _test(self, s, expected):
        actual = Solution().reverseVowels(s)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
