from typing import List, Tuple

class SearchAlgorithm:

    # Implement Uniform search
    @staticmethod
    def uniform_search(grid: List[List[str]]) -> Tuple[int, List[List[str]]]:
        # Your code here
        pass

    # Implement Depth First Search
    @staticmethod
    def dfs(grid: List[List[str]]) -> Tuple[int, List[List[str]]]:
        # Your code here
        pass
    
    # Implement Breadth First Search
    @staticmethod
    def bfs(grid: List[List[str]]) -> Tuple[int, List[List[str]]]:
        # Your code here
        pass
    
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
