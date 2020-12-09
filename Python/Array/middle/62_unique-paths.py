'''
62. 不同路径

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？

例如，上图是一个7 x 3 的网格。有多少可能的路径？



示例 1:

输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右

示例 2:

输入: m = 7, n = 3
输出: 28



提示：

    1 <= m, n <= 100
    题目数据保证答案小于等于 2 * 10 ^ 9


'''
# 较SOlution2, SOlution3优化空间复杂度
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        @describe: 动态规划，空间复杂度O(m)
        @param m: 列数
        @param n: 行数
        @return: 路径条数
        '''
        dp = [1 for i in range(m)]
        for i in range(n - 1):
            for j in range(1, m):
                dp[j] = dp[j - 1] + dp[j]
        return dp[-1]

class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        @describe: 动态规划，空间复杂度O(nxm)
        @param m: 列数
        @param n: 行数
        @return: 路径条数
        '''
        dp = [[0 for i in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                # 第一列和第一行的值设为1
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[n - 1][m - 1]

class Solution3:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        @describe:  动态规划，将nxm的矩阵扩展至(n-1)x(m+1)并令dp[0][1]或dp[1][0]让第一列和第一行在迭代后变为1，空间复杂度O(nxm)
        @param m: 列数
        @param n: 行数
        @return: 路径条数
        '''
        dp = [[0 for i in range(m + 1)] for i in range(n + 1)]
        dp[0][1] = 1
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[n][m]

# 当m和n较大时容易超时
class Solution4:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        @describe: 回溯，满足条件跳出，否则不断迭代
        @param m: 列数
        @param n: 行数
        @return: 路径条数
        '''
        def backTrack(row, col, m, n):
            sums = 0
            if row == n and col == m:
                return 1
            if row < n:
                sums += backTrack(row + 1, col, m, n)
            if col < m:
                sums += backTrack(row, col + 1, m, n)
            return sums
        return backTrack(1, 1, m, n)

if __name__ ==  '__main__':
    s = Solution()
    print(s.uniquePaths(3, 2))