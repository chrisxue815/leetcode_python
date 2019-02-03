import unittest
import utils


# O(nlog(n)) time. O(n) space. Sorting, hash table.
class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        result = ''
        words.sort()
        visited = set()

        for word in words:
            if len(word) == 1 or word[:-1] in visited:
                visited.add(word)
                if len(result) < len(word):
                    result = word

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().longestWord(**case.args._asdict())
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
