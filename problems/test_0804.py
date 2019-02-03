import unittest
import utils

to_morse = [
    ".-", "-...", "-.-.", "-..", ".", "..-.", "--.",  # abcdefg
    "....", "..", ".---", "-.-", ".-..", "--", "-.",  # hijklmn
    "---", ".--.", "--.-", ".-.", "...", "-",  # opqrst
    "..-", "...-", ".--", "-..-", "-.--", "--..",  # uvwxyz
]


# O(n) time. O(n) space. Hash table.
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        return len({''.join(to_morse[ord(ch) - ord('a')] for ch in word) for word in words})


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().uniqueMorseRepresentations(**case.args._asdict())
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
