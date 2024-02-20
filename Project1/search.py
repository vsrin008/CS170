from typing import List, Tuple
from collections import deque


class SearchAlgorithm:

    # Implement Uniform search
    @staticmethod
    def uniform_search(grid: List[List[str]]) -> Tuple[int, List[List[str]]]:
        # Your code here
        pass

    # Implement Depth First Search
    @staticmethod
    def dfs(grid: List[List[str]]) -> Tuple[int, List[List[str]]]:
        # Directions: Right, Down, Left, Up (adjust if needed to match expected traversal pattern)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Find the starting point 's'
        start = None
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 's':
                    start = (i, j)
                    break
            if start:
                break

        if not start:
            return -1, grid  # Return if no start found

        stack = [start]  # Stack for DFS
        visited = set([start])  # Track visited cells
        visit_order = 1  # Track the order of visitation

        while stack:
            x, y = stack.pop()

            # If not the starting cell, mark the visitation order
            if (x, y) != start:
                grid[x][y] = str(visit_order)
                visit_order += 1

            # Check if we've found the target
            if grid[x][y] == 't':
                return 1, grid

            # Temporarily store neighbors to add in reverse order
            temp_neighbors = []
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in visited and grid[nx][ny] != '-1':
                    temp_neighbors.append((nx, ny))
                    visited.add((nx, ny))  # Mark neighbor as visited

            # Add neighbors to stack in reverse order to ensure correct traversal
            for neighbor in reversed(temp_neighbors):
                stack.append(neighbor)

        return -1, grid  # Return if target is not found
    
    # Implement Breadth First Search
    @staticmethod
    def bfs(grid: List[List[str]]) -> Tuple[int, List[List[str]]]:
        # Your code here
        # Directions: Right, Down, Left, Up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Find the starting point (s) and initialize the queue
        start = None
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 's':
                    start = (i, j)
                    break
            if start:
                break
        
        # Early return if start is not found
        if start is None:
            return -1, grid
        
        queue = deque([start])  # Queue only stores positions
        visited = set([start])  # Track visited cells
        order = 1  # Order of visitation
        
        while queue:
            x, y = queue.popleft()
            
            # Explore neighbors
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in visited and grid[nx][ny] in ['0', 't']:
                    if grid[nx][ny] == '0':  # Mark the cell with visitation order
                        grid[nx][ny] = str(order)
                        order += 1
                    elif grid[nx][ny] == 't':  # If target is found, stop the search
                        return 1, grid
                    visited.add((nx, ny))
                    queue.append((nx, ny))
                    
        # If we exit the loop without finding the target
        return -1, grid
    
    # Implement Best First Search
    @staticmethod
    def best_first_search(grid: List[List[str]]) -> Tuple[int, List[List[str]]]:
        # Your code here
        pass
    
    # Implement A* Search
    @staticmethod
    def a_star_search(grid: List[List[str]]) -> Tuple[int, List[List[str]]]:
        # Your code here
        pass
    
    # Implement Greedy Search
    @staticmethod
    def greedy_search(grid: List[List[str]]) -> Tuple[int, List[List[str]]]:
        # Your code here
        pass

if __name__ == "__main__":

    example = [
        ['0', '0', '0', '0'],
        ['0', '-1', '-1', 't'],
        ['s', '0', '-1', '0'],
        ['0', '0', '0', '-1']
    ]

    found, final_state = SearchAlgorithm.dfs(example)
    if found == 1:
        print("Target found!")
    else:
        print("Target not found.")

    for row in final_state:
        print(' '.join(row))
