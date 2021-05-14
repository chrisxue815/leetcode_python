import unittest

import utils
from linkedlist import ListNode


# O(n) time. O(1) space. Floyd's cycle detection algorithm.
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        t = head
        h = head.next
        while t is not h:
            if not h or not h.next:
                return False
            h = h.next.next
            t = t.next
        return True


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, process_args=self.process_args)

    def process_args(self, args):
        args.head = ListNode.from_array(args.head)

        if args.pos >= 0:
            cycle_start = args.head
            for i in range(args.pos):
                cycle_start = cycle_start.next

            curr = cycle_start
            while curr.next:
                curr = curr.next
            curr.next = cycle_start

        del args.pos


if __name__ == '__main__':
    unittest.main()
