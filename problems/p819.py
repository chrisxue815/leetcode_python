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
        words = re.split(r'\W+', paragraph)
        counter = collections.Counter(word.lower() for word in words if word)
        banned = set(banned)
        for word, count in counter.most_common():
            if word not in banned:
                return word


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p819.json').test_cases

        for case in cases:
            actual = Solution().mostCommonWord(case.paragraph, case.banned)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
