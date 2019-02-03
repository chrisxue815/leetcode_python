import unittest


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = [1]

        for _ in range(n - 1):
            next_ = []
            curr = result[0]
            count = 0

            for digit in result:
                if digit == curr:
                    count += 1
                else:
                    next_.append(count)
                    next_.append(curr)
                    curr = digit
                    count = 1

            next_.append(count)
            next_.append(curr)
            result = next_

        return ''.join(str(digit) for digit in result)


class Test(unittest.TestCase):
    def test(self):
        self._test(1, '1')
        self._test(2, '11')
        self._test(3, '21')
        self._test(4, '1211')
        self._test(5, '111221')
        self._test(6, '312211')

    def _test(self, n, expected):
        actual = Solution().countAndSay(n)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
