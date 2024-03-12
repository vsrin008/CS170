from typing import List, Tuple
from collections import deque
import heapq

def find_start(grid: List[List[str]]) -> Tuple[int, int]:
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value == 's':
                return (i, j)
    return (-1, -1)  # Not found

def find_t(grid: List[List[str]]) -> Tuple[int, int]:
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value == 't':
                return (i, j)
    return (-1, -1)  # Not found

def manhattan(point1: Tuple[int, int], point2: Tuple[int, int]) -> int:
    return abs(point2[0] - point1[0]) + abs(point2[1] - point1[1])



class SearchAlgorithm:

    # Implement Uniform search
    @staticmethod
    def uniform_search(grid: List[List[str]]) -> List[Tuple[int, int]]:
        start = find_start(grid)
        target = find_t(grid)

        if start == (-1, -1) or target == (-1, -1):
            return []  # No s or t

        pq = [(0, start, None)]  # (cost, current_node, parent_node)
        visited = set()
        parent_map = {}  # reconstruct path

        while pq:
            current_cost, current, parent = heapq.heappop(pq)
            if current in visited:
                continue

            visited.add(current)
            parent_map[current] = parent

            if current == target:
                # Reconstruct path from target to start
                path = []
                while current is not None:
                    path.append(current)
                    current = parent_map[current]
                return path[::-1]

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = current[0] + dx, current[1] + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != '-1' and (nx, ny) not in visited:
                    heapq.heappush(pq, (current_cost + 1, (nx, ny), current))

        return []  # target not found

    # Implement Depth First Search
    @staticmethod
    def dfs(grid: List[List[str]]) -> List[Tuple[int, int]]:
        start = find_start(grid)
        t = find_t(grid)

        if start == (-1, -1) or t == (-1, -1):
            return []  # s or t not found

        stack = [(start, None)]  # parent in stack
        visited = set()
        parent_map = {}

        # Right, Down, Left, Up 
        neighbors = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        while stack:
            (cur_x, cur_y), parent = stack.pop()
            if (cur_x, cur_y) not in visited:
                visited.add((cur_x, cur_y))
                parent_map[(cur_x, cur_y)] = parent

                if (cur_x, cur_y) == t:
                    # Reconstruct path
                    path = []
                    current = (cur_x, cur_y)
                    while current is not None:
                        path.append(current)
                        current = parent_map[current]
                    return path[::-1]  # Reverse path

                # add to stack in reverse order because of stack
                for dx, dy in reversed(neighbors):
                    nx, ny = cur_x + dx, cur_y + dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in visited and grid[nx][ny] != '-1':
                        stack.append(((nx, ny), (cur_x, cur_y)))

        return []  # target not found
    
    # Implement Breadth First Search
    @staticmethod
    def bfs(grid: List[List[str]]) -> List[Tuple[int, int]]:
        start = find_start(grid)
        if start == (-1, -1):
            return []  #no start found

        # Directions: Up, Right, Down, Left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        queue = deque([start])
        visited = set([start])
        parent = {start: None}  # for path reconstruction

        while queue:
            current = queue.popleft()

            if grid[current[0]][current[1]] == 't':
                # target found, reconstruct path
                path = []
                while current is not None:
                    path.append(current)
                    current = parent[current]
                return path[::-1]  # Reverse path to start->target

            for dx, dy in directions:
                nx, ny = current[0] + dx, current[1] + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in visited and grid[nx][ny] != '-1':
                    visited.add((nx, ny))
                    queue.append((nx, ny))
                    parent[(nx, ny)] = current

        return []  # Target not found
    
    # Implement Best First Search
    @staticmethod
    def best_first_search(grid: List[List[str]]) -> List[Tuple[int, int]]:
        start = find_start(grid)
        target = find_t(grid)

        if start == (-1, -1) or target == (-1, -1):
            return []  # s or t not found

        pq = [(manhattan(start, target), start)]
        visited = set()
        parent = {start: None}

        while pq:
            _, current = heapq.heappop(pq)
            if current in visited:
                continue
            visited.add(current)

            if current == target:
                # target found, build path
                path = []
                while current:
                    path.append(current)
                    current = parent[current]
                return path[::-1]

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = current[0] + dx, current[1] + dy
                next_pos = (nx, ny)
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != '-1' and next_pos not in visited:
                    heapq.heappush(pq, (manhattan(next_pos, target), next_pos))
                    if next_pos not in parent:  # only set parent if not alr visited or set
                        parent[next_pos] = current

        return []  # no target found
    
    # Implement A* Search
    @staticmethod
    def a_star_search(grid: List[List[str]]) -> List[Tuple[int, int]]:
        start = find_start(grid)
        target = find_t(grid)

        if start == (-1, -1) or target == (-1, -1):
            return []  # s or t not found

        pq = [(0 + manhattan(start, target), 0, start)]  # (f_cost, g_cost, position)
        visited = set()
        parent = {start: None}
        g_costs = {start: 0}

        while pq:
            f_cost, g_cost, current = heapq.heappop(pq)

            if current in visited:
                continue
            visited.add(current)

            if current == target:
                # Target found, reconstruct  path
                path = []
                while current:
                    path.append(current)
                    current = parent[current]
                return path[::-1]

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = current[0] + dx, current[1] + dy
                next_pos = (nx, ny)
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != '-1':
                    new_g_cost = g_cost + 1
                    new_f_cost = new_g_cost + manhattan(next_pos, target)
                    if next_pos not in g_costs or new_g_cost < g_costs[next_pos]:
                        g_costs[next_pos] = new_g_cost
                        heapq.heappush(pq, (new_f_cost, new_g_cost, next_pos))
                        parent[next_pos] = current

        return []  # target not found
    
    # Implement Greedy Search
    @staticmethod
    def greedy_search(grid: List[List[str]]) -> List[Tuple[int, int]]:
        start = find_start(grid)
        target = find_t(grid)

        if not start or not target:
            return []  # Start or target not found

        pq = [(manhattan(start, target), start)]
        visited = set()
        parent = {start: None}

        while pq:
            current_heuristic, current_pos = heapq.heappop(pq)

            if current_pos == target:
                # Target found, reconstruct the path
                path = []
                while current_pos:
                    path.append(current_pos)
                    current_pos = parent[current_pos]
                return path[::-1]

            if current_pos in visited:
                continue
            visited.add(current_pos)

            for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:  # Prioritize horizontal movement first
                nx, ny = current_pos[0] + dx, current_pos[1] + dy
                next_pos = (nx, ny)
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != '-1' and next_pos not in visited:
                    heapq.heappush(pq, (manhattan(next_pos, target), next_pos))
                    if next_pos not in parent:  # Update parent if this path is better
                        parent[next_pos] = current_pos

        return []  # Target not found or no greedy choice available


if __name__ == "__main__":

    example = [
        ['0','-1','0','0'],
        ['0','0','0','0'],
        ['0','-1','0','0'],
        ['s','0','t','0'],
    ]
    print(SearchAlgorithm.greedy_search(example))

