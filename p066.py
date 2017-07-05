import unittest


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in xrange(len(digits) - 1, -1, -1):
            digit = digits[i] + 1
            if digit >= 10:
                digits[i] = digit - 10
            else:
                digits[i] = digit
                break
        else:
            digits.insert(0, 1)

        return digits


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3], [1, 2, 4])
        self._test([8, 9, 9], [9, 0, 0])
        self._test([9, 9, 9], [1, 0, 0, 0])

    def _test(self, digits, expected):
        actual = Solution().plusOne(digits)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
