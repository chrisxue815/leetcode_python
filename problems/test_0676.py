import collections
import unittest
import utils


# O(n) time. O(n * len(word)) space. Hash table.
class MagicDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = None

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        self.dict = collections.defaultdict(collections.Counter)

        for word in dict:
            words = self.dict[len(word)]
            words[word] += 1

            for i in xrange(len(word)):
                words[word[:i] + '_' + word[i + 1:]] += 1

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        words = self.dict.get(len(word), None)
        if not words:
            return False

        for i in xrange(len(word)):
            count = words[word[:i] + '_' + word[i + 1:]]
            if count > 1 or count == 1 and word not in words:
                return True

        return False


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases
        magic_dict = MagicDictionary()

        for case in cases:
            magic_dict.buildDict(case.args.dict)

            for search in case.args.searches:
                actual = magic_dict.search(search.word)
                self.assertEqual(search.expected, actual)


if __name__ == '__main__':
    unittest.main()
