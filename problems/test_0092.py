import unittest
from typing import Optional

import utils
from linkedlist import ListNode


# O(n) time. O(1) space.
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = start = ListNode(0)
        dummy.next = head

        for _ in range(left - 1):
            start = start.next

        end = start.next
        prev = end
        curr = prev.next

        for _ in range(right - left):
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_

        start.next = prev
        end.next = curr

        return dummy.next


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
