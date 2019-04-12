import unittest

import utils


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr = self.root

        for ch in word:
            child = curr.get(ch)
            if not child:
                curr[ch] = child = {}
            curr = child

        curr['#'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """

        def search(curr, start):
            for i in range(start, len(word)):
                ch = word[i]
                if ch == '.':
                    for k, v in curr.items():
                        if k != '#' and search(v, i + 1):
                            return True
                    return False
                else:
                    child = curr.get(ch)
                    if not child:
                        return False
                    curr = child
            return curr.get('#', False)

        return search(self.root, 0)


class Test(unittest.TestCase):
    def test(self):
        cls = WordDictionary
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            obj = None

            for func, parameters, expected in zip(case.functions, case.args, case.expected):
                if func == cls.__name__:
                    obj = cls(*parameters)
                else:
                    actual = getattr(obj, func)(*parameters)
                    self.assertEqual(expected, actual, msg=case.args)


if __name__ == '__main__':
    unittest.main()
