import unittest
from linkedlist import ListNode
import random


class Solution(object):
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        self.curr = head
        self.rand = random.Random()

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        for _ in xrange(self.rand.randint(0, 4)):
            if self.curr.next:
                self.curr = self.curr.next
            else:
                self.curr = self.head
        return self.curr.val


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3])

    def _test(self, nums):
        head = ListNode.from_array(nums)
        solution = Solution(head)

        iteration = 1000
        hit = 0

        for _ in xrange(iteration):
            val = solution.getRandom()
            if val == nums[0]:
                hit += 1

        self.assertAlmostEqual(float(hit) / iteration, 1.0 / len(nums), places=1)


if __name__ == '__main__':
    unittest.main()
