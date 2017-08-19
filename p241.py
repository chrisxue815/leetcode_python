import unittest
import operator


class Solution(object):
    def diffWaysToCompute(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        tokens = []
        operand = 0
        for ch in s:
            if ch.isdigit():
                operand = operand * 10 + ord(ch) - ord('0')
            else:
                tokens.append(operand)
                operand = 0
                if ch == '+':
                    tokens.append(operator.add)
                elif ch == '-':
                    tokens.append(operator.sub)
                elif ch == '*':
                    tokens.append(operator.mul)
        tokens.append(operand)

        def dfs(start, end):
            if start + 1 == end:
                yield tokens[start]
            else:
                for i in xrange(start + 1, end, 2):
                    op = tokens[i]
                    for a in dfs(start, i):
                        for b in dfs(i + 1, end):
                            yield op(a, b)

        return list(dfs(0, len(tokens)))


class Test(unittest.TestCase):
    def test(self):
        self._test('2-1-1', [0, 2])
        self._test('2*3-4*5', [-34, -14, -10, -10, 10])

    def _test(self, s, expected):
        actual = Solution().diffWaysToCompute(s)
        self.assertItemsEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
