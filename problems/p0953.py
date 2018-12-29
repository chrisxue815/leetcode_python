import unittest
import utils


# O(n) time. O(1) space. Hash table.
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        indices = {ch: i for i, ch in enumerate(order)}

        for i in xrange(1, len(words)):
            a = words[i - 1]
            b = words[i]

            for j in xrange(min(len(a), len(b))):
                if a[j] != b[j]:
                    if indices[a[j]] < indices[b[j]]:
                        break
                    else:
                        return False
            else:
                if len(a) > len(b):
                    return False

        return True


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().isAlienSorted(case.words, case.order)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
