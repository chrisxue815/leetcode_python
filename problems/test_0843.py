import collections
import random

import unittest
from typing import List

WORD_LENGTH = 6


def get_num_matches(a, b):
    return sum(1 for i in range(WORD_LENGTH) if a[i] == b[i])


# O(n^2) time. O(n^2) space. Minimax.
class Solution:
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        graph = collections.defaultdict(lambda: [[] for _ in range(WORD_LENGTH + 1)])

        for i, a in enumerate(wordlist):
            for j in range(i + 1, len(wordlist)):
                b = wordlist[j]
                num_matches = get_num_matches(a, b)
                graph[a][num_matches].append(b)
                graph[b][num_matches].append(a)

        candidates = set(wordlist)

        while True:
            word = min(candidates, key=lambda candidate: len(graph[candidate][0]))
            num_matches = master.guess(word)

            if num_matches == WORD_LENGTH:
                return
            candidates.intersection_update(graph[word][num_matches])


def random_word():
    return ''.join(chr(random.randint(ord('a'), ord('z'))) for _ in range(WORD_LENGTH))


class Master:
    def __init__(self):
        self.ok = False
        self.attempts = 0
        self.wordlist = [random_word() for _ in range(100)]
        self.secret_word = random.choice(self.wordlist)

    def guess(self, word):
        """
        :type word: str
        :rtype int
        """
        self.attempts += 1
        num_matches = get_num_matches(self.secret_word, word)
        if num_matches == WORD_LENGTH:
            self.ok = True
        return num_matches


class Test(unittest.TestCase):
    def test(self):
        for _ in range(10):
            master = Master()
            solution = Solution()
            solution.findSecretWord(master.wordlist, master)
            self.assertEqual(True, master.ok)
            self.assertLessEqual(master.attempts, 10)


if __name__ == '__main__':
    unittest.main()
