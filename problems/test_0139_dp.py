import collections
import unittest
from typing import List

import utils


# O(len(s) * len(wordDict)) time. O(len(s) + len(wordDict)) space. DP.
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] = wordBreak(s[:i])
        dp = [False] * (len(s) + 1)
        dp[0] = True
        words = collections.defaultdict(lambda: collections.defaultdict(set))

        for word in wordDict:
            words[word[-1]][len(word)].add(word)

        for i, ch in enumerate(s):
            end = i + 1
            for length, words_with_length in words[ch].items():
                if end >= length and dp[end - length] and s[end - length:end] in words_with_length:
                    dp[end] = True
                    break

        return dp[-1]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().wordBreak(**case.args._asdict())
            self.assertEqual(case.expected, actual, msg=case.args)


if __name__ == '__main__':
    unittest.main()
