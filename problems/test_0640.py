import unittest


# O(n)
class Solution:
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        coeff = const = num = 0
        sign = side = 1

        for i, ch in enumerate(equation):
            if ch.isdigit():
                num = num * 10 + ord(ch) - ord('0')
            elif ch == '+':
                const -= side * sign * num
                num = 0
                sign = 1
            elif ch == '-':
                const -= side * sign * num
                num = 0
                sign = -1
            elif ch == 'x':
                if num == 0 and (i == 0 or equation[i - 1] != '0'):
                    num = 1
                coeff += side * sign * num
                num = 0
            elif ch == '=':
                const -= side * sign * num
                num = 0
                side = -1
                sign = 1
        const -= side * sign * num

        if coeff:
            return 'x=' + str(const // coeff)
        return 'No solution' if const else 'Infinite solutions'


class Test(unittest.TestCase):
    def test(self):
        self._test('x+5-3+x=6+x-2', 'x=2')
        self._test('x=x', 'Infinite solutions')
        self._test('2x=x', 'x=0')
        self._test('2x+3x-6x=x+2', 'x=-1')
        self._test('x=x+2', 'No solution')
        self._test('0x=x+2', 'x=-2')

    def _test(self, equation, expected):
        actual = Solution().solveEquation(equation)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
