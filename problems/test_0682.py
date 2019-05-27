import unittest


# O(n)
class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        for op in ops:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                stack.append(stack[-1] * 2)
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)


class Test(unittest.TestCase):
    def test(self):
        self._test(["5", "2", "C", "D", "+"], 30)
        self._test(["5", "-2", "4", "C", "D", "9", "+", "+"], 27)

    def _test(self, ops, expected):
        actual = Solution().calPoints(ops)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
