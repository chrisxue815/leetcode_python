import unittest
from typing import List

import utils


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda h_k: (-h_k[0], h_k[1]))

        r = []
        for p in people:
            r.insert(p[1], p)

        return r


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
