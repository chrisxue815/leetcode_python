import unittest


class NestedInteger(object):
    """
    This is the interface that allows for creating nested lists.
    You should not implement it, or speculate about its implementation
    """

    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        self.value = value if value is not None else []

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        return isinstance(self.value, int)

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        if self.isInteger():
            self.value = [NestedInteger(self.value)]
        self.value.append(elem)

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """
        self.value = value

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        if self.isInteger():
            return self.value
        return None

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        if self.isInteger():
            return None
        return self.value


def _serialize(value):
    if value.isInteger():
        return str(value.getInteger())
    children = value.getList()
    children_text = ','.join(_serialize(child) for child in children)
    return '[' + children_text + ']'


class Solution(object):
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
        for hi in xrange(len(s)):
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
        actual = _serialize(Solution().deserialize(s))
        self.assertEqual(actual, s)


if __name__ == '__main__':
    unittest.main()
