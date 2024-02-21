from typing import List, Tuple
from collections import deque
import heapq


def manhattan(point1, point2):
    return abs(point2[0] - point1[0]) + abs(point2[1] - point1[1])
    
def find_start(grid):
    s= None
    for i in range (len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 's':
                s= (i,j)
    return s

def find_t(grid):
    t= None
    for i in range (len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 't':
                t= (i,j)
    return t


class SearchAlgorithm:

    # Implement Uniform search
    @staticmethod
    def uniform_search(grid: List[List[str]]) -> Tuple[int, List[List[str]]]:
        pass


    # Implement Depth First Search
    @staticmethod
    def dfs(grid: List[List[str]]) -> Tuple[int, List[List[str]]]:
        s = find_start(grid)
        t = find_t(grid)

        if s is None or t is None:
            return -1, grid  # return if there is no start or target

        #initialize stack, visited, and count
        stack = [s]
        visited = set()
        count = 1 

        #Right, Down, Left, Up
        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while stack:
            cur_x, cur_y = stack.pop()
            if (cur_x, cur_y) not in visited:
                visited.add((cur_x, cur_y))
                # Mark cell after visiting if it is a 0
                if grid[cur_x][cur_y] == '0':
                    grid[cur_x][cur_y] = str(count)
                    count += 1
                elif (cur_x, cur_y) == t:
                    return 1, grid  # Found target

                # Explore neighbors 
                for dx, dy in neighbors:  
                    nx, ny = cur_x + dx, cur_y + dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in visited and grid[nx][ny] != '-1':
                        stack.append((nx, ny))

        return -1, grid  # Target could not be found
    

    # Implement Breadth First Search
    @staticmethod
    def bfs(grid: List[List[str]]) -> Tuple[int, List[List[str]]]:
        # Your code here
        # Directions: Right, Down, Left, Up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Find the starting point (s) and initialize the queue
        start = find_start(grid)
        
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
        s = find_start(grid)
        t = find_t(grid)

        if s is None or t is None:
            return -1, grid  # If either start or target is not found

        # initialize priority queue, visited list, and counting order
        pq = [(manhattan(s, t), s)]
        visited = set()
        count = 1  # Start counting from 1 for visited cells

        while pq:
            _, current_pos = heapq.heappop(pq)
            x, y = current_pos

            if current_pos in visited:
                continue
            visited.add(current_pos)

            # mark cell after visiting
            if grid[x][y] == '0':
                grid[x][y] = str(count)
                count += 1  

            
            if current_pos == t:
                return 1, grid  # target found

            # explore neighbors
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # Directions: Right, Down, Left, Up
                nx, ny = x + dx, y + dy
                next_pos = (nx, ny)
                
                # check next position
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != '-1' and next_pos not in visited:
                    heapq.heappush(pq, (manhattan(next_pos, t), next_pos))

        return -1, grid  # no target found

    
    # Implement A* Search
    @staticmethod
    def a_star_search(grid: List[List[str]]) -> Tuple[int, List[List[str]]]:
        # Your code here
        pass
    

    # Implement Greedy Search
    @staticmethod
    def greedy_search(grid: List[List[str]]) -> Tuple[int, List[List[str]]]:
        s= find_start(grid)
        t= find_t(grid)



if __name__ == "__main__":

    example = [
        ['0', '0', '0', '0'],
        ['0', '-1', '-1', 't'],
        ['s', '0', '-1', '0'],
        ['0', '0', '0', '-1']
    ]

    found, final_state = SearchAlgorithm.best_first_search(example)
    if found == 1:
        print("Target found!")
    else:
        print("Target not found.")

    for row in final_state:
        print(' '.join(row))
