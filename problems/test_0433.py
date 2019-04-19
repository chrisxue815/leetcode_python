import collections
import unittest
from typing import List

import utils


# O(n^2) time. O(n) space. Graph, BFS.
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1

        q = collections.deque()
        q.append((start, 0))

        while q:
            curr, distance = q.popleft()
            successors = []

            for nxt in bank:
                diff = 0

                for a, b in zip(curr, nxt):
                    if a == b:
                        continue
                    if diff == 0:
                        diff += 1
                    elif diff == 1:
                        break
                else:
                    if diff == 1:
                        if nxt == end:
                            return distance + 1
                        successors.append(nxt)

            bank.difference_update(successors)
            for nxt in successors:
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
