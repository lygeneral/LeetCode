'''
64. 最小路径和

给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。



示例 1：

输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。

示例 2：

输入：grid = [[1,2,3],[4,5,6]]
输出：12



提示：

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 200
    0 <= grid[i][j] <= 100


'''

class Solution:
    def minPathSum(self, grid):
        '''
        @describe: 动态规划，dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]，空间复杂度O(n)
        @param grid: 路径
        @return: 最短路径
        '''
        m = len(grid)
        n = len(grid[0])
        # 初始化为第一行累加
        dp = [sum(grid[0][:i + 1]) for i in range(n)]
        for i in range(1, m):
            dp[0] = dp[0] + grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
        return dp[-1]

class Solution2:
    def minPathSum(self, grid):
        '''
        @describe: 动态规划，dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + dp[i][j]
        @param grid: 路径
        @return: 最短路径
        '''
        # 可在原数组上修改
        dp = grid
        m = len(grid)
        n = len(grid[0])
        for col in range(1, n):
            dp[0][col] = dp[0][col] + dp[0][col - 1]
        for row in range(1, m):
            dp[row][0] = dp[row][0] + dp[row - 1][0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + dp[i][j]
        return dp[m - 1][n - 1]


class Solution3:
    def minPathSum(self, grid):
        '''
        @describe: 回溯，容易超出时间限制
        @param grid: 路径
        @return: 最短路径
        '''
        res = []
        def backTrack(row, col, m, n, grid, pathSum):
            if row == m or col == n:
                return
            if row == m - 1 and col == n - 1:
                res.append(pathSum + grid[row][col])
                return
            backTrack(row + 1, col, m, n, grid, pathSum + grid[row][col])
            backTrack(row, col + 1, m, n, grid, pathSum + grid[row][col])
        m = len(grid)
        n = len(grid[0])
        backTrack(0, 0, m, n, grid, 0)
        return res

if __name__ == '__main__':
    grid = [[1,1,1],[1,1,1]]
    s = Solution()
    print(s.minPathSum(grid))
