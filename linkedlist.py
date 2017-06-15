# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def from_array(vals):
        if not vals:
            return None
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

    @staticmethod
    def reverse_list(root):
        prev = None
        while root:
            next_ = root.next
            root.next = prev
            prev = root
            root = next_
        return prev

    @staticmethod
    def count(root):
        result = 0
        while root:
            result += 1
            root = root.next
        return result
