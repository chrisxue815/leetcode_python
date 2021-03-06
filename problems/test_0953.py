import unittest
import utils


# O(n) time. O(1) space. Hash table.
class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        indices = {ch: i for i, ch in enumerate(order)}

        for i in range(1, len(words)):
            a = words[i - 1]
            b = words[i]

            for j in range(min(len(a), len(b))):
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
            args = str(case.args)
            actual = Solution().isAlienSorted(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
