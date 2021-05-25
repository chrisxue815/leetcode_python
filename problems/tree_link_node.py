from tree import TreeNode


class Node(TreeNode):
    def __init__(self, x):
        super(Node, self).__init__(x)
        self.next = None

    @staticmethod
    def to_next_value_array(root):
        result = []

        while root:
            curr = root
            while curr:
                result.append(curr.val)
                curr = curr.next
            result.append(None)
            root = root.left

        return result
