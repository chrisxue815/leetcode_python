import heapq
import unittest
from typing import List

import utils
from linkedlist import ListNode


# O(klog(n)) time. O(k) space. Min-heap.
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = curr = ListNode(0)
        q = []
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(q, (head.val, i, head))

        while q:
            val, i, head = q[0]
            curr.next = head
            curr = head
            head = head.next

            if head:
                heapq.heapreplace(q, (head.val, i, head))
            else:
                heapq.heappop(q)

        return dummy.next


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution,
                   process_args=self.process_args,
                   process_result=utils.linked_list_to_array)

    @staticmethod
    def process_args(args):
        args.lists = [ListNode.from_array(head) for head in args.lists]
