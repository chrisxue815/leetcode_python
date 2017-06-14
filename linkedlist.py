# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def from_array(vals):
        root_parent = ListNode(0)
        parent = root_parent

        for val in vals:
            curr = ListNode(val)
            parent.next = curr
            parent = curr

        return root_parent.next

    @staticmethod
    def to_array(root):
        vals = []
        while root:
            vals.append(root.val)
            root = root.next
        return vals
