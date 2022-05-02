import unittest
from typing import Optional

import utils
from linkedlist import ListNode


# O(n) time. O(1) space. Two pointers
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_lo = lo = ListNode(0)
        dummy_hi = hi = ListNode(0)

        while head:
            if head.val < x:
                lo.next = head
                lo = head
            else:
                hi.next = head
                hi = head
            head = head.next

        lo.next = dummy_hi.next
        hi.next = None
        return dummy_lo.next


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution,
                   process_args=self.process_args,
                   process_result=utils.linked_list_to_array)

    @staticmethod
    def process_args(args):
        args.head = ListNode.from_array(args.head)


if __name__ == '__main__':
    unittest.main()
