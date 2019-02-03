import unittest


# Below is the interface for Iterator, which is already defined for you.

class Iterator(object):
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.nums = nums
        self.curr = -1

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self.curr + 1 < len(self.nums)

    def __next__(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        self.curr += 1
        return self.nums[self.curr]


class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.it = iterator
        # We need to introduce a hasNext variable if None is a valid item in the iterator
        self.next_item = next(iterator) if iterator.hasNext() else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.next_item

    def __next__(self):
        """
        :rtype: int
        """
        next_item = self.next_item
        self.next_item = next(self.it) if self.it.hasNext() else None
        return next_item

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.next_item is not None


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].


class Test(unittest.TestCase):
    def test(self):
        self._test([0, 1, 2, 3])

    def _test(self, nums):
        it = PeekingIterator(Iterator(nums))
        for num in nums:
            self.assertEqual(True, it.hasNext())
            self.assertEqual(num, it.peek())
            self.assertEqual(num, next(it))
        self.assertEqual(False, it.hasNext())


if __name__ == '__main__':
    unittest.main()
