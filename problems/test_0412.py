import unittest


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = [0] * n
        for i in range(1, n + 1):
            if i % 15 == 0:
                result[i - 1] = 'FizzBuzz'
            elif i % 3 == 0:
                result[i - 1] = 'Fizz'
            elif i % 5 == 0:
                result[i - 1] = 'Buzz'
            else:
                result[i - 1] = str(i)
        return result


class Test(unittest.TestCase):
    def test(self):
        self._test(15, [
            '1',
            '2',
            'Fizz',
            '4',
            'Buzz',
            'Fizz',
            '7',
            '8',
            'Fizz',
            'Buzz',
            '11',
            'Fizz',
            '13',
            '14',
            'FizzBuzz'
        ])

    def _test(self, n, expected):
        actual = Solution().fizzBuzz(n)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
