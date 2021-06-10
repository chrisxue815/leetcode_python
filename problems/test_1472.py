import unittest

import utils


# O(n) space. Array.
class BrowserHistory:

    # O(1) time. O(1) space.
    def __init__(self, homepage: str):
        self.urls = [homepage]
        self.index = 0

    # O(1) time. O(1) space.
    def visit(self, url: str) -> None:
        self.index += 1
        del self.urls[self.index:]
        self.urls.append(url)

    # O(1) time. O(1) space.
    def back(self, steps: int) -> str:
        self.index = max(0, self.index - steps)
        return self.urls[self.index]

    # O(1) time. O(1) space.
    def forward(self, steps: int) -> str:
        self.index = min(len(self.urls) - 1, self.index + steps)
        return self.urls[self.index]


class Test(unittest.TestCase):
    def test(self):
        utils.test_invocations(self, __file__, BrowserHistory)


if __name__ == '__main__':
    unittest.main()
