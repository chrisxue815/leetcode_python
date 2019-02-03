import unittest


# O(n) time. O(1) space.
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if not chars:
            return 0

        prev = chars[0]
        count = 0
        w = 0

        for r in range(len(chars) + 1):
            ch = chars[r] if r < len(chars) else '\0'
            if ch == prev:
                count += 1
            else:
                chars[w] = prev
                w += 1
                if count > 1:
                    count_str = str(count)
                    chars[w:w + len(count_str)] = count_str
                    w += len(count_str)
                prev = ch
                count = 1

        return w


class Test(unittest.TestCase):
    def test(self):
        self._test(["a", "a", "b", "b", "c", "c", "c"], ["a", "2", "b", "2", "c", "3"])
        self._test(["a"], ["a"])
        self._test(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"], ["a", "b", "1", "2"])

    def _test(self, chars, expected):
        actual = Solution().compress(chars)
        self.assertEqual(expected, chars[:actual])


if __name__ == '__main__':
    unittest.main()
