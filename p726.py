import unittest
import collections


def _read_element(formula, i):
    i += 1
    while i < len(formula) and formula[i].islower():
        i += 1
    return i


def _read_num(formula, i):
    num = ord(formula[i]) - ord('0')
    i += 1
    while i < len(formula) and formula[i].isdigit():
        num = num * 10 + ord(formula[i]) - ord('0')
        i += 1
    return i, num


def _mul(stack, num):
    brackets = 1
    i = len(stack) - 2
    while i >= 0:
        if stack[i] == '(':
            if brackets == 1:
                break
            brackets -= 1
            i -= 1
        elif stack[i] == ')':
            brackets += 1
            i -= 1
        else:
            stack[i] *= num
            i -= 2


def _count(stack):
    counter = collections.Counter()
    i = 0
    while i < len(stack):
        item = stack[i]
        if item == '(' or item == ')':
            i += 1
            continue
        counter[item] += stack[i + 1]
        i += 2
    return ''.join(element + (str(num) if num > 1 else '') for element, num in sorted(counter.items()))


# O(n) time. O(n) space. Iteration.
class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        stack = []
        i = 0
        while i < len(formula):
            ch = formula[i]
            if ch.isupper():
                hi = _read_element(formula, i)
                stack.append(formula[i:hi])
                stack.append(1)
                i = hi
            elif ch.isdigit():
                hi, num = _read_num(formula, i)
                stack[-1] = num
                i = hi
            elif ch == '(':
                stack.append('(')
                i += 1
            else:
                stack.append(')')
                if i + 1 < len(formula) and formula[i + 1].isdigit():
                    hi, num = _read_num(formula, i + 1)
                    _mul(stack, num)
                    i = hi
                else:
                    i += 1
        return _count(stack)


class Test(unittest.TestCase):
    def test(self):
        self._test('H2O', 'H2O')
        self._test('Mg(OH)2', 'H2MgO2')
        self._test('K4(ON(SO3)2)2', 'K4N2O14S4')
        self._test('Mg12', 'Mg12')

    def _test(self, formula, expected):
        actual = Solution().countOfAtoms(formula)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
