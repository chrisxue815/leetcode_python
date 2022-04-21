import unittest

import utils


def parse_num(s, i):
    while i < len(s) and s[i] == ' ':
        i += 1

    num = 0
    while i < len(s) and s[i].isdigit():
        num = num * 10 + ord(s[i]) - ord('0')
        i += 1

    return i, num


def parse_operator(s, i):
    while i < len(s) and s[i] == ' ':
        i += 1

    operator = s[i] if i < len(s) else '+'
    return i + 1, operator


# O(n) time. O(1) space. Parsing.
class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        sign = 1
        i, product = parse_num(s, 0)

        while i <= len(s):
            i, operator = parse_operator(s, i)
            i, num = parse_num(s, i)

            if operator == '*':
                product *= num
            elif operator == '/':
                product //= num
            elif operator == '+' or operator == '-':
                result += sign * product
                sign = 44 - ord(operator)  # '+' == 43, '-' == 45
                product = num

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
