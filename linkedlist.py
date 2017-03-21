# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def from_array(cls, vals):
        root_parent = ListNode(0)
        parent = root_parent

        for val in vals:
            curr = ListNode(val)
            parent.next = curr
            parent = curr
            
        return root_parent.next
