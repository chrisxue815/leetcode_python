import unittest


# O(n) time. O(sqrt(n)) space. DFS.
class Solution:
    def floodFill(self, image, sr, sc, new_color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type new_color: int
        :rtype: List[List[int]]
        """
        old_color = image[sr][sc]
        if old_color == new_color:
            return image

        height = len(image)
        width = len(image[0])

        def dfs(r, c):
            if 0 <= r < height and 0 <= c < width and image[r][c] == old_color:
                image[r][c] = new_color
                dfs(r - 1, c)
                dfs(r + 1, c)
                dfs(r, c - 1)
                dfs(r, c + 1)

        dfs(sr, sc)
        return image


class Test(unittest.TestCase):
    def test(self):
        test_cases = [
            [[
                [1, 1, 1],
                [1, 1, 0],
                [1, 0, 1],
            ], 1, 1, 2, [
                [2, 2, 2],
                [2, 2, 0],
                [2, 0, 1],
            ]],
        ]

        for test_case in test_cases:
            actual = Solution().floodFill(*test_case[:-1])
            self.assertEqual(test_case[-1], actual)


if __name__ == '__main__':
    unittest.main()
