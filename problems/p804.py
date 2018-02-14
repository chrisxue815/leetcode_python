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
        transforms = set()

        for word in words:
            transform = ''.join(to_morse[ord(ch) - ord('a')] for ch in word)
            transforms.add(transform)

        return len(transforms)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p804.json').test_cases

        for case in cases:
            actual = Solution().uniqueMorseRepresentations(case.words)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
