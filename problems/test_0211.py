import unittest

import utils


class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        curr = self.root

        for ch in word:
            child = curr.get(ch)
            if not child:
                curr[ch] = child = {}
            curr = child

        curr['#'] = True

    def search(self, word: str) -> bool:

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
        utils.test_invocations(self, __file__, WordDictionary)


if __name__ == '__main__':
    unittest.main()
