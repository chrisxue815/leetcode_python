import collections
import unittest
from typing import List

import utils


# O(n) time. O(n) space. Graph, BFS.
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1

        q = collections.deque()
        q.append((start, 0))

        while q:
            curr, distance = q.popleft()

            for i in range(len(curr)):
                for c in 'ATCG':
                    if c == curr[i]:
                        continue

                    nxt = curr[:i] + c + curr[i + 1:]

                    if nxt not in bank:
                        continue

                    if nxt == end:
                        return distance + 1

                    bank.remove(nxt)
                    q.append((nxt, distance + 1))

        return -1


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().minMutation(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=case.args)


if __name__ == '__main__':
    unittest.main()
