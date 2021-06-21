import unittest
from typing import List

import utils

int_max = 0x7fffffff


def distance(a, b):
    for i in range(1, len(a)):
        if b.startswith(a[i:]):
            return len(b) - len(a) + i
    return len(b)


# O(n^2 * 2^n) Time. O(2^n) space. DP.
class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)
        graph = [[distance(words[i], words[j]) for j in range(n)] for i in range(n)]
        dp = [[int_max] * n for _ in range(1 << n)]
        path = [[0] * n for _ in range(1 << n)]
        last = -1
        min_ = int_max

        for i in range(1, 1 << n):
            for j in range(n):
                if i & (1 << j):
                    prev = i - (1 << j)
                    if prev == 0:
                        dp[i][j] = len(words[j])
                    else:
                        for k in range(n):
                            if dp[prev][k] < int_max and dp[prev][k] + graph[k][j] < dp[i][j]:
                                dp[i][j] = dp[prev][k] + graph[k][j]
                                path[i][j] = k
                if i == (1 << n) - 1 and dp[i][j] < min_:
                    min_ = dp[i][j]
                    last = j

        curr = (1 << n) - 1
        stack = []
        while curr > 0:
            stack.append(last)
            tmp = curr
            curr -= 1 << last
            last = path[tmp][last]

        i = stack.pop()
        result = [words[i]]

        while stack:
            j = stack.pop()
            start = len(words[j]) - graph[i][j]
            result.append(words[j][start:])
            i = j

        return ''.join(result)


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, check_result=self.check_result)

    def check_result(self, case, actual, msg):
        self.assertEqual(len(case.expected), len(actual), msg)


if __name__ == '__main__':
    unittest.main()
