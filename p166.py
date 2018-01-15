import unittest


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if not denominator:
            return 'Inf'
        if not numerator:
            return '0'

        positive = (numerator > 0) == (denominator > 0)
        if numerator < 0:
            numerator = -numerator
        if denominator < 0:
            denominator = -denominator

        q, r = divmod(numerator, denominator)
        if not r:
            return str(q) if positive else '-' + str(q)

        fraction = [str(q), '.'] if positive else ['-', str(q), '.']
        visited = {}
        numerator = r * 10

        while True:
            start_index = visited.get(numerator, None)
            if start_index:
                fraction.insert(start_index, '(')
                fraction.append(')')
                return ''.join(fraction)

            visited[numerator] = len(fraction)

            q, r = divmod(numerator, denominator)

            fraction.append(str(q))
            if not r:
                return ''.join(fraction)

            numerator = r * 10


class Test(unittest.TestCase):
    def test(self):
        self._test(1, 2, '0.5')
        self._test(2, 1, '2')
        self._test(2, 3, '0.(6)')
        self._test(22, 7, '3.(142857)')
        self._test(20, 18, '1.(1)')

    def _test(self, numerator, denominator, expected):
        actual = Solution().fractionToDecimal(numerator, denominator)
        self.assertEqual(expected, actual)

        actual = Solution().fractionToDecimal(-numerator, -denominator)
        self.assertEqual(expected, actual)

        expected = '-' + expected

        actual = Solution().fractionToDecimal(-numerator, denominator)
        self.assertEqual(expected, actual)

        actual = Solution().fractionToDecimal(numerator, -denominator)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
