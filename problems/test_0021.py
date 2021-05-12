import unittest

import utils
from linkedlist import ListNode


# O(n) time. O(1) space. Merging linked list
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        prev = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                prev = l1
                l1 = l1.next
            else:
                prev.next = l2
                prev = l2
                l2 = l2.next

        prev.next = l1 if l1 else l2
        return dummy.next


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution,
                   process_args=self.process_args,
                   process_result=utils.linked_list_to_array)

    @staticmethod
    def process_args(args):
        args.l1 = ListNode.from_array(args.l1)
        args.l2 = ListNode.from_array(args.l2)


if __name__ == '__main__':
    unittest.main()
