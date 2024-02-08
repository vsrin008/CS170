from typing import List, Set
from collections import deque

class ActivityM2:
    @staticmethod
    def find_edges(grid: List[List[str]]) -> List[Set[int]]:
        m = len(grid)
        n = len(grid[0]) 
        visited = set()  # Set to track visited cells
        edges_list = []  # List to hold edge sets of all islands

        # Check if cell is in the grid
        def in_bounds(x, y):
            return 0 <= x < m and 0 <= y < n

        # find neighbors of a cell
        def get_neighbors(x, y):
          neighbors = [] 
          for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]: 
            if in_bounds(x + dx, y + dy):
              neighbors.append((x + dx, y + dy))  # Add neighbor cell to the list
          return neighbors 


        # Check if cell is an edge of an island
        def is_edge(x, y):
            # A cell on the grid's boundary is automatically an edge cell.
            if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                return True
            # if neighboring cell is water, then cell is an edge
            for nx, ny in get_neighbors(x, y):
                if grid[nx][ny] == "0":
                    return True
            return False

        def bfs(start_x, start_y):
            q = deque([(start_x, start_y)])
            current_island_edges = set()
            while q:
                x, y = q.popleft()
                unique_number = x * n + y
                if unique_number not in visited:
                    visited.add(unique_number)
                    if is_edge(x, y):
                        current_island_edges.add(unique_number)
                    for nx, ny in get_neighbors(x, y):
                        if grid[nx][ny] == "1" and (nx * n + ny) not in visited:
                            q.append((nx, ny))
            return current_island_edges

        # run BFS on each unvisited cell
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i * n + j) not in visited:
                    edges_of_island = bfs(i, j)
                    if edges_of_island:  # if island has edges
                        edges_list.append(edges_of_island)
        return edges_list


if __name__ == "__main__":
  example = [['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1'] ]
  edges = ActivityM2.find_edges(example)
  print(edges)