from typing import List, Tuple
from itertools import product

class ActivityM3:
    @staticmethod
    def valid_state(state, rows, cols):
        for i in range(rows):
            for j in range(cols):
                if state[i][j] == 1:  # talking
                    # check adjacent cells
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < rows and 0 <= ny < cols and state[nx][ny] == 1:
                            return False
        return True

    @staticmethod
    def find_whisperers(grid: List[List[int]]) -> Tuple[int, List[List[int]]]:
        rows, cols = len(grid), len(grid[0])
        max_sum = 0
        best_state = None

        for state in product(*[product([0, 1], repeat=cols) for _ in range(rows)]):
            state_matrix = [list(row) for row in state]
            if ActivityM3.valid_state(state_matrix, rows, cols):
                current_sum = sum(grid[i][j] * state_matrix[i][j] for i in range(rows) for j in range(cols))
                if current_sum > max_sum:
                    max_sum = current_sum
                    best_state = state_matrix

        return max_sum, best_state

if __name__ == "__main__":
    example = [[1,2,4],[1,2,1]]
    score, result = ActivityM3.find_whisperers(example)
    print(score, result)
