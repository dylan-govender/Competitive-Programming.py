class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        # M, N = len(grid), len(grid[0])

        # dp = {(M-1, N-1):1}

        # def dfs(r, c):
        #     if r == M or c == N or grid[r][c]:
        #         return 0
        #     if (r, c) in dp:
        #         return dp[(r, c)]
        #     dp[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
        #     return dp[(r, c)]

        # return dfs(0, 0)

        # TRUE DP

        M, N = len(grid), len(grid[0])
        dp = [0] * N
        dp[N-1] = 1
        for r in range(M-1, -1, -1):
            for c in range(N-1, -1, -1):
                if grid[r][c] == 1: # blocked
                    dp[c] = 0
                elif c < N - 1:
                    dp[c] = dp[c] + dp[c + 1]
                
        return dp[0]