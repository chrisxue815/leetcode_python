import collections
import unittest

import utils


# O(n) time. O(n) space. Queue.
class RecentCounter(object):
    def __init__(self):
        self.q = collections.deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        q = self.q

        while q and q[0] < t - 3000:
            q.popleft()

        q.append(t)
        return len(q)


class Test(unittest.TestCase):
    def test(self):
        cls = RecentCounter
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            obj = None

            for func, parameters, expected in zip(case.functions, case.args, case.expected):
                if func == cls.__name__:
                    obj = cls(*parameters)
                else:
                    actual = getattr(obj, func)(*parameters)
                    self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
