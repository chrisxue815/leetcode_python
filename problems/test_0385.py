import unittest
import nested_integer
from nested_integer import NestedInteger


class Solution:
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        if s[0] != '[':
            return NestedInteger(int(s))

        stack = []
        curr = NestedInteger()
        lo = 0
        for hi in range(len(s)):
            ch = s[hi]
            if ch == '[':
                child = NestedInteger()
                curr.getList().append(child)
                stack.append(curr)
                curr = child
                lo = hi + 1
            elif ch == ']':
                if lo < hi:
                    child = NestedInteger(int(s[lo:hi]))
                    curr.getList().append(child)
                curr = stack.pop()
                lo = hi + 1
            elif ch == ',':
                if lo < hi:
                    child = NestedInteger(int(s[lo:hi]))
                    curr.getList().append(child)
                lo = hi + 1

        return curr.getList()[0]


class Test(unittest.TestCase):
    def test(self):
        self._test('1')
        self._test('[1]')
        self._test('[[1]]')
        self._test('[1,[2,[3]]]')
        self._test('[1,[2,[3]]]')
        self._test('[1,2,3,[4,5,6]]')
        self._test('[1,2,-3,[],[4,5,6]]')
        self._test('[]')
        self._test('[[]]')

    def _test(self, s):
        actual = nested_integer.serialize(Solution().deserialize(s))
        self.assertEqual(s, actual)


if __name__ == '__main__':
    unittest.main()
