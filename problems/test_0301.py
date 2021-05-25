import unittest
from typing import List

import utils


def dfs_left_to_right(s, start, last_deleted, result):
    count = 0
    for i in range(start, len(s)):
        if s[i] == '(':
            count += 1
        elif s[i] == ')':
            count -= 1
            if count < 0:
                for j in range(last_deleted, i + 1):
                    if s[j] == ')' and (j == last_deleted or s[j - 1] != ')'):
                        dfs_left_to_right(s[:j] + s[j + 1:], i, j, result)
                return

    dfs_right_to_left(s, len(s) - 1, len(s) - 1, result)


def dfs_right_to_left(s, start, last_deleted, result):
    count = 0
    for i in range(start, -1, -1):
        if s[i] == ')':
            count -= 1
        elif s[i] == '(':
            count += 1
            if count > 0:
                for j in range(last_deleted, i - 1, -1):
                    if s[j] == '(' and (j == last_deleted or s[j + 1] != '('):
                        dfs_right_to_left(s[:j] + s[j + 1:], i - 1, j - 1, result)
                return

    result.append(s)


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        result = []
        dfs_left_to_right(s, 0, 0, result)
        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, check_result=self.check_result)

    def check_result(self, case, actual, msg):
        self.assertCountEqual(case.expected, actual, msg)


if __name__ == '__main__':
    unittest.main()
