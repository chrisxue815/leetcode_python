import unittest


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        s = list(s)

        # trim whitespaces at start, end and between words
        i = 0
        target_lo = 0

        while True:
            while i < n and s[i] == ' ':
                i += 1
            lo = i

            while i < n and s[i] != ' ':
                i += 1
            hi = i

            if lo == hi:
                break

            if target_lo > 0:
                s[target_lo] = ' '
                target_lo += 1

            target_hi = hi - lo + target_lo

            s[target_lo:target_hi] = s[lo:hi]

            target_lo = target_hi

        n = target_lo
        s = s[:n]

        # reverse entire string
        s.reverse()

        # reverse back each word
        lo = 0
        for hi in range(n):
            if s[hi] == ' ':
                s[lo:hi] = reversed(s[lo:hi])
                lo = hi + 1
        if lo < n:
            s[lo:n] = reversed(s[lo:n])

        return ''.join(s)


class Test(unittest.TestCase):
    def test(self):
        self._test("  the sky is    blue   ", "blue is sky the")
        self._test("     ", "")

    def _test(self, s, expected):
        actual = Solution().reverseWords(s)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
