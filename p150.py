import unittest


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                stack.append(-stack.pop() + stack.pop())
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                op = stack.pop()
                stack.append(int(float(stack.pop()) / op))
            else:
                stack.append(int(token))
        return stack.pop()


class Test(unittest.TestCase):
    def test(self):
        self._test(['2', '1', '+', '3', '*'], 9)
        self._test(['4', '13', '5', '/', '+'], 6)
        self._test(['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+'], 22)

    def _test(self, tokens, expected):
        actual = Solution().evalRPN(tokens)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
