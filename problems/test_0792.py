import collections
import unittest
from typing import List

import utils


# O(n) time. O(len(words)) space. Hash table, queue.
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        result = 0
        q = collections.defaultdict(list)

        for word in words:
            it = iter(word)
            q[next(it)].append(it)

        for c in S:
            for it in q.pop(c, ()):
                next_c = next(it, None)
                if next_c:
                    q[next_c].append(it)
                else:
                    result += 1

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().numMatchingSubseq(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
