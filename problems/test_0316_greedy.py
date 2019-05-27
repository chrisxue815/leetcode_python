import unittest


def _find_max_possible_index(s, count, counts):
    counts = list(counts)
    for i in range(len(s) - 1, -1, -1):
        ch = ord(s[i])
        if counts[ch]:
            counts[ch] = 0
            count -= 1
            if count == 0:
                return i


class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        counts = [0] * (ord('z') + 1)

        for ch in s:
            counts[ord(ch)] = 1

        count = sum(counts)
        hi = _find_max_possible_index(s, count, counts)
        lo = 0

        for _ in range(count):
            min_ch = 256
            min_i = 0
            for i in range(lo, hi + 1):
                ch = ord(s[i])
                if counts[ch] and ch < min_ch:
                    min_ch = ch
                    min_i = i

            result.append(chr(min_ch))
            counts[min_ch] = 0
            count -= 1
            lo = min_i + 1

            if min_ch == ord(s[hi]):
                hi = _find_max_possible_index(s, count, counts)

        return ''.join(result)


class Test(unittest.TestCase):
    def test(self):
        self._test('bcab', 'bca')
        self._test('bcabc', 'abc')
        self._test('cbacdcbc', 'acdb')

    def _test(self, s, expected):
        actual = Solution().removeDuplicateLetters(s)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
