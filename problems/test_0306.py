import unittest


# O(n^2). Array slicing
class Solution:
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if not num:
            return False

        def is_valid_additive(a, b, c_index):
            while True:
                c = a + b
                c_str = str(c)
                if not num[c_index:].startswith(c_str):
                    return False
                a, b, c_index = b, c, c_index + len(c_str)
                if c_index >= len(num):
                    return c_index == len(num)

        a_max_len = (len(num) - 1) >> 1
        if num[0] == '0':
            a_max_len = min(a_max_len, 1)

        for a_len in range(1, a_max_len + 1):
            a = int(num[:a_len])
            remaining = len(num) - a_len
            b_max_len = min(remaining >> 1, remaining - a_len)
            if num[a_len] == '0':
                b_max_len = min(b_max_len, 1)

            for b_len in range(1, b_max_len + 1):
                c_index = a_len + b_len
                b = int(num[a_len:c_index])
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
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
