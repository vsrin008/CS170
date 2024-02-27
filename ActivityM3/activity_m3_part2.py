from typing import List, Tuple

class ActivityM3:
    @staticmethod
    def find_whisperers_1d(row: List[int]) -> Tuple[int, List[int]]:
        n = len(row)
        if n == 0:  
            return 0, []
        elif n == 1:  # Handle single element input
            return row[0], [1]

        dp = [0] * n  # Dynamic programming table for max urgency sum
        choice = [0] * n  # To track choices (1 for talking, 0 for not talking)
        
        # Base cases
        dp[0] = row[0]
        choice[0] = 1
        if row[1] > row[0]:
            dp[1] = row[1]
            choice[1] = 1
        else:
            dp[1] = row[0]

        # Fill dp table and make choices
        for i in range(2, n):
            if dp[i-2] + row[i] > dp[i-1]:
                dp[i] = dp[i-2] + row[i]
                choice[i] = 1
            else:
                dp[i] = dp[i-1]

        # Reconstruct choices
        result = [0] * n
        i = n-1
        while i >= 0:
            if choice[i] == 1:
                result[i] = 1
                i -= 2  # Skip the previous student as we can't select adjacent students
            else:
                i -= 1

        return dp[-1], result

if __name__ == "__main__":
    example = [1, 2, 4]
    score, result = ActivityM3.find_whisperers_1d(example)
    print(score, result)
