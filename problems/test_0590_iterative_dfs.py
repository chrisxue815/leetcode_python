class Node(object):
    """
    # Definition for a Node.
    """

    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []

        result = []
        stack = [root]

        while stack:
            curr = stack[-1]

            if len(stack) >= 2 and curr is stack[-2]:
                stack.pop()
                stack.pop()
                result.append(curr.val)
            else:
                stack.append(curr)
                stack += reversed(curr.children)

        return result
