import unittest
import p385


class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = []
        self.next_index = -1

        if nestedList:
            self.curr_list = nestedList
            self.next_item = self._move_next()
        else:
            self.curr_list = []
            self.next_item = None

    def _move_next(self):
        while True:
            while True:
                self.next_index += 1
                if self.next_index >= len(self.curr_list):
                    break
                next_item = self.curr_list[self.next_index]
                if next_item.isInteger():
                    return next_item.getInteger()
                children = next_item.getList()
                if len(children) > 0:
                    self.stack.append((self.next_index, self.curr_list))
                    self.next_index = -1
                    self.curr_list = children

            if self.stack:
                self.next_index, self.curr_list = self.stack.pop()
            else:
                return None

    def next(self):
        """
        :rtype: int
        """
        curr = self.next_item
        self.next_item = self._move_next()
        return curr

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.next_item is not None


class Test(unittest.TestCase):
    def test(self):
        self._test('[[1,1],2,[1,1]]', [1, 1, 2, 1, 1])
        self._test('[[1,1],2,[],[1,1,[1,1]]]', [1, 1, 2, 1, 1, 1, 1])
        self._test('[1]', [1])
        self._test('[]', [])
        self._test('[[]]', [])

    def _test(self, nested_list, expected):
        nested_list = p385.Solution().deserialize(nested_list).getList()

        i = NestedIterator(nested_list)
        actual = []
        while i.hasNext():
            actual.append(i.next())

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
