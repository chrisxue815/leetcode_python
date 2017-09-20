import unittest


# O(n^2). Array slicing
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if not num:
            return False

        def parse_int(start, end):
            i = 0
            while start < end:
                i = i * 10 + ord(num[start]) - ord('0')
                start += 1
            return i

        def is_valid_additive(a, b, c_index):
            while True:
                c = a + b
                c_str = str(a + b)
                if not num[c_index:].startswith(c_str):
                    return False
                a, b, c_index = b, c, c_index + len(c_str)
                if c_index >= len(num):
                    if c_index == len(num):
                        return True
                    else:
                        return False

        a_max_len = (len(num) - 1) >> 1
        if num[0] == '0':
            a_max_len = min(a_max_len, 1)

        for a_len in xrange(1, a_max_len + 1):
            a = parse_int(0, a_len)
            remaining = len(num) - a_len
            b_max_len = min(remaining >> 1, remaining - a_len)
            if num[a_len] == '0':
                b_max_len = min(b_max_len, 1)

            for b_len in xrange(1, b_max_len + 1):
                c_index = a_len + b_len
                b = parse_int(a_len, c_index)
                if is_valid_additive(a, b, c_index):
                    return True

        return False


class Test(unittest.TestCase):
    def test(self):
        self._test('112358', True)
        self._test('199100199', True)
        self._test('101', True)
        self._test('011', True)
        self._test('000', True)
        self._test('111122335588143', True)

    def _test(self, num, expected):
        actual = Solution().isAdditiveNumber(num)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
