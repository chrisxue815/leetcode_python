class Node(object):
    """
    # Definition for a QuadTree node.
    """

    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


# O(n^2) time. O(n) space. Recursion.
class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """

        def dfs(row, col, width):
            if width == 1:
                return Node(grid[row][col], True, None, None, None, None)

            half_width = width >> 1

            top_left = dfs(row, col, half_width)
            top_right = dfs(row, col + half_width, half_width)
            bottom_left = dfs(row + half_width, col, half_width)
            bottom_right = dfs(row + half_width, col + half_width, half_width)

            if top_left.isLeaf and top_right.isLeaf and bottom_left.isLeaf and bottom_right.isLeaf \
                    and top_left.val == top_right.val == bottom_left.val == bottom_right.val:
                return top_left

            return Node(0, False, top_left, top_right, bottom_left, bottom_right)

        return dfs(0, 0, len(grid))
