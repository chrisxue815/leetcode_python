import random
import unittest

from linkedlist import ListNode


# Reservoir sampling.
class Solution:
    # O(1) time. O(1) space.
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    # O(n) time. O(1) space.
    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        result = self.head.val
        curr = self.head.next
        rand = random.Random()
        i = 2

        while curr:
            if rand.randrange(i) == 0:
                result = curr.val
            i += 1
            curr = curr.next

        return result


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3])

    def _test(self, nums):
        head = ListNode.from_array(nums)
        solution = Solution(head)

        iteration = 1000
        hit = 0

        for _ in range(iteration):
            val = solution.getRandom()
            if val == nums[0]:
                hit += 1

        self.assertAlmostEqual(1.0 / len(nums), float(hit) / iteration, places=1)


if __name__ == '__main__':
    unittest.main()
