'''
118. 杨辉三角

给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。

在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

'''

class Solution:
    def generate(self, numRows):
        '''
        @describe: 动态规划，先初始化全1的数组，然后从第三行开始动态叠加
        @param numRows: int
        @return: List[List[int]]
        '''
        dp = [[1] * (i + 1) for i in range(numRows)]
        n = 2
        while n < numRows:
            for i in range(1, len(dp[n - 1])):
                dp[n][i] = dp[n - 1][i - 1] + dp[n - 1][i]
            n += 1
        return dp

class Solution2:
    def generate(self, numRows):
        '''
        @describe: 按列->行遍历方式，每行左一和右一为1，下一行每一个元素依次等于上一行两个元素之和
        @param numRows: int
        @return: List[List[int]]
        '''
        res = [[1]]
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        for i in range(1, numRows):
            tmp = [1]   #首位是1
            for j in range(len(res[i - 1]) - 1):
                tmp.append(res[i - 1][j] + res[i - 1][j + 1])
            tmp.append(1)
            res.append(tmp)
        return res

if __name__ == '__main__':
    numRows = 10
    s=Solution()
    print(s.generate((numRows)))