import unittest
import utils


class TrieNode:
    def __init__(self):
        self.val = None
        self.children = [None] * 26

    def add(self, s):
        curr = self

        for ch in s:
            index = ord(ch) - ord('a')
            child = curr.children[index]
            if not child:
                curr.children[index] = child = TrieNode()
            curr = child

        curr.val = s


# O(n) time. O(n) space. Trie.
class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        result = ['']
        root = TrieNode()

        for word in words:
            root.add(word)

        def dfs(curr):
            for child in curr.children:
                if child and child.val:
                    dfs(child)

            if curr.val and len(result[0]) < len(curr.val):
                result[0] = curr.val

        dfs(root)
        return result[0]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().longestWord(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
