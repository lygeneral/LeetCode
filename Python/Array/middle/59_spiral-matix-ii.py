'''
59. 螺旋矩阵 II

给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]


'''

class Solution:
    def generateMatrix(self,n):
        '''
        @describe: 内外循环遍历
        @param n: 矩阵shape
        @return: 矩阵
        '''
        res = [[0 for i in range(n)] for i in range(n)]
        num = 1
        left, right = 0, n - 1
        top, bottom = 0, n - 1
        while left <= right and top <= bottom:
            for col in range(left, right + 1):
                res[top][col] = num
                num += 1
            for row in range(top + 1, bottom):
                res[row][right] = num
                num += 1
            if top != bottom:
                for col in range(right, left - 1, -1):
                    res[bottom][col] = num
                    num += 1
            if left != right:
                for row in range(bottom - 1, top, -1):
                    res[row][left] = num
                    num += 1
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return res

if __name__ == '__main__':
    n = 3
    s = Solution()
    print(s.generateMatrix(n))
