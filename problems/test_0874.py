import unittest
import utils

directions = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
]


# O(len(commands)) time. O(len(obstacles)) space. Hash table.
class Solution:
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        result = 0
        position = (0, 0)
        direction = 1
        obstacles = {(x, y) for x, y in obstacles}

        for command in commands:
            if command == -2:
                direction = (direction + 1) % 4
            elif command == -1:
                direction = (direction - 1) % 4
            else:
                offset = directions[direction]

                for _ in range(command):
                    new_position = (position[0] + offset[0], position[1] + offset[1])
                    if new_position in obstacles:
                        break
                    position = new_position

                result = max(result, position[0] * position[0] + position[1] * position[1])

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().robotSim(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
