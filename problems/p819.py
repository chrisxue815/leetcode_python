import collections
import re
import unittest
import utils


# O(n) time. O(n) space. Hash table.
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banned = set(banned)
        words = re.split(r'\W+', paragraph)
        words = (word.lower() for word in words if word and word.lower() not in banned)
        counter = collections.Counter(words)
        return counter.most_common(1)[0][0]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p819.json').test_cases

        for case in cases:
            actual = Solution().mostCommonWord(case.paragraph, case.banned)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
