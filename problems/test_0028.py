import unittest


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Naive string search algorithm
        for haystack_start in range(len(haystack) - len(needle) + 1):
            for needle_index, needle_char in enumerate(needle):
                if needle_char != haystack[haystack_start + needle_index]:
                    break
            else:
                return haystack_start
        return -1


# See also: CPython fast search
# https://github.com/python/cpython/blob/master/Objects/stringlib/fastsearch.h

class Test(unittest.TestCase):
    def test(self):
        self._test('abcdefghi', 'def', 3)
        self._test('abcdefghi', 'xyz', -1)
        self._test('abcdefghi', 'dez', -1)

    def _test(self, haystack, needle, expected):
        actual = Solution().strStr(haystack, needle)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
