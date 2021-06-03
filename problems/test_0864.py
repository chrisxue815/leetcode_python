import collections
import heapq
import unittest
from typing import List

import utils

neighbors = (
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
)


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        num_keys = 0
        positions = {}
        starting_point = None
        next_cells = {}

        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == '.' or cell == '#':
                    continue
                if cell == '@':
                    starting_point = (r, c)
                else:
                    positions[cell] = (r, c)
                    if cell.islower():
                        num_keys += 1

        def bfs(initial_r, initial_c):
            next_cells[grid[initial_r][initial_c]] = distance = {}
            visited = set()
            visited.add((initial_r, initial_c))
            q = collections.deque()
            q.append((initial_r, initial_c, 0))
            while q:
                curr_r, curr_c, d = q.popleft()
                for dr, dc in neighbors:
                    r = curr_r + dr
                    c = curr_c + dc
                    if not (0 <= r < rows and 0 <= c < cols):
                        continue
                    if (r, c) in visited:
                        continue
                    visited.add((r, c))
                    cell = grid[r][c]
                    if cell == '#':
                        continue
                    if cell == '.' or cell == '@':
                        q.append((r, c, d + 1))
                    else:
                        distance[cell] = d + 1

        bfs(*starting_point)
        for r, c in positions.values():
            bfs(r, c)

        state_graph = {('@', 0): 0}
        q = [(0, starting_point, 0)]

        while q:
            dist, (r, c), state = heapq.heappop(q)
            if state == (1 << num_keys) - 1:
                return dist
            cell = grid[r][c]
            for nxt, nxt_dist in next_cells[cell].items():
                new_state = state
                if nxt.islower():
                    new_state |= 1 << (ord(nxt) - ord('a'))
                elif new_state & 1 << (ord(nxt) - ord('A')) == 0:
                    continue

                node = (nxt, new_state)
                new_dist = dist + nxt_dist
                if node not in state_graph or state_graph[node] > new_dist:
                    state_graph[node] = new_dist
                    heapq.heappush(q, (new_dist, positions[nxt], new_state))

        return -1


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
