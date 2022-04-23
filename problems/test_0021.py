import unittest
from typing import Optional

import utils
from linkedlist import ListNode


# O(n) time. O(1) space. Merging linked list
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        prev = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                prev = list1
                list1 = list1.next
            else:
                prev.next = list2
                prev = list2
                list2 = list2.next

        prev.next = list1 if list1 else list2
        return dummy.next


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution,
                   process_args=self.process_args,
                   process_result=utils.linked_list_to_array)

    @staticmethod
    def process_args(args):
        args.list1 = ListNode.from_array(args.list1)
        args.list2 = ListNode.from_array(args.list2)


if __name__ == '__main__':
    unittest.main()
