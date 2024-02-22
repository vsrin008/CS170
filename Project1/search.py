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
        start = find_start(grid)
        target = find_t(grid)

        if not start or not target:
            return -1, grid  # return if no start or target cell

        pq = [(0, start)]  # initialize priority queue
        visited = set(start)  
        order = {}  # track visitation order
        visit_count = 1 

        while pq:
            current_cost, (current_x, current_y) = heapq.heappop(pq) 

            if (current_x, current_y) == target:
                return 1, grid  # target found

            # if we reach an unvisited node
            if (current_x, current_y) not in visited:
                visited.add((current_x, current_y)) 
                if grid[current_x][current_y] == '0':
                    grid[current_x][current_y] = str(visit_count)
                    visit_count += 1

                # Explore neighbors
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nx, ny = current_x + dx, current_y + dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != '-1' and (nx, ny) not in visited:
                        heapq.heappush(pq, (current_cost + 1, (nx, ny)))  # push neighbor with new cost

        return -1, grid  # target not found


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

        # find s and t
        start = find_start(grid)
        target = find_t(grid)

        if not start or not target:
            return -1, grid

        pq = [(0 + manhattan(start, target), start, 0)]  # Initialize the priority queue with the start position, its g(n) = 0, and its f(n) = h(n) (Manhattan distance)
        visited = set() # Track visited nodes so we dont visit again
        f_costs = {start: 0}  # Cost from start to node
        visit_order = 1 #order for marking

        while pq:
            # pop the position with the lowest f(n) from the queue
            f_cost, current_pos, g_cost = heapq.heappop(pq) 
            x, y = current_pos

            if current_pos in visited: #skip if already visited 
                continue
            visited.add(current_pos)


            if grid[x][y] == '0':
                grid[x][y] = str(visit_order) #mark cell with visitation number
                visit_order += 1

            if current_pos == target: #target found
                return 1, grid
            

            # Explore neighbors
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # right, down, left, up
                nx, ny = x + dx, y + dy
                next_pos = (nx, ny)
                #check if neighbor is a valid cell
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != '-1' and next_pos not in visited:
                    # calculate g(n) for the neighbor and f(n) as sum of g(n) and h(n)
                    new_g_cost = g_cost + 1
                    new_f_cost = new_g_cost + manhattan(next_pos, target)
                    # if this path is better, update g(n) and add to queue
                    if next_pos not in f_costs or new_g_cost < f_costs[next_pos]:
                        f_costs[next_pos] = new_f_cost
                        heapq.heappush(pq, (new_f_cost, next_pos, new_g_cost))

        return -1, grid #target not found
    

    # Implement Greedy Search I am very close but I think there is an issue with direction that I cannot figure out
    @staticmethod
    def greedy_search(grid: List[List[str]]) -> Tuple[int, List[List[str]]]:
        start = find_start(grid)
        target = find_t(grid)

        if not start or not target:
            return -1, grid

        pq = [(manhattan(start, target), 0, start)]  #Initialize priority queue
        visited = set()
        visit_count = 1 

        while pq:
            _, _, current_pos = heapq.heappop(pq)
            x, y = current_pos

            if current_pos in visited:
                continue
            visited.add(current_pos)

            # Mark the cell after visiting
            if grid[x][y] == '0':
                grid[x][y] = str(visit_count)
                visit_count += 1
            elif current_pos == target:
                return 1, grid  # Target found

            # flag to check for a closer neighbor
            any_closer_neighbor = False

            # Explore neighbors
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                next_pos = (nx, ny)

                # check if next is valid
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != '-1' and next_pos not in visited:
                    next_heuristic = manhattan(next_pos, target)
                    if next_heuristic < manhattan(current_pos, target):
                        any_closer_neighbor = True
                        heapq.heappush(pq, (next_heuristic, visit_count, next_pos))

            # stop the search if we do not find a greedy option
            if not any_closer_neighbor:
                break

        return -1, grid  # target not found



if __name__ == "__main__":

    example = [
        ['0', '0', '0', '0'],
        ['0', '-1', '-1', 't'],
        ['s', '0', '-1', '0'],
        ['0', '0', '0', '-1']
    ]

    found, final_state = SearchAlgorithm.a_star_search(example)
    if found == 1:
        print("Target found!")
    else:
        print("Target not found.")

    for row in final_state:
        print(' '.join(row))
