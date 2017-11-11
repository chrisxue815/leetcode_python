import unittest


class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []

        for num in xrange(left, right + 1):
            quotient = num
            while quotient:
                quotient, digit = divmod(quotient, 10)
                if digit == 0 or num % digit != 0:
                    break
            else:
                result.append(num)

        return result


class Test(unittest.TestCase):
    def test(self):
        test_cases = [
            [1, 22, [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]],
        ]

        for test_case in test_cases:
            actual = Solution().selfDividingNumbers(test_case[0], test_case[1])
            self.assertEqual(actual, test_case[2])


if __name__ == '__main__':
    unittest.main()
