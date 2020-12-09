'''
54. 螺旋矩阵

给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]

示例 2:

输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]


'''

# 较Solution2把top, bottom, left, right列出来了，代码更清晰
class Solution:
    def spiralOrder(self, matrix):
        '''
        @desribe: 依次左至右、上至下、右至左、下至上循环
        @param matrix: 矩阵
        @return: 螺旋输出所有元素
        '''
        m = len(matrix)
        n = len(matrix[0])
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        res = []
        while left <= right and top <= bottom :
            # 左->右
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            # 上->下
            for row in range(top + 1, bottom):
                res.append(matrix[row][right])
            # 右-->左
            for col in range(right, left - 1, -1):
                if top != bottom:
                    res.append(matrix[bottom][col])
            # 下->上
            for row in range(bottom - 1, top, -1):
                if left != right:
                    res.append(matrix[row][left])
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return res


class Solution2:
    def spiralOrder(self, matrix):
        '''
        @desribe: 依次左至右、上至下、右至左、下至上循环
        @param matrix: 矩阵
        @return: 螺旋输出所有元素
        '''
        m = len(matrix)
        n = len(matrix[0])
        cnt = (min(m,n) + 1)//2
        res = []
        for i in range(cnt):
            # 左->右
            for j in range(i, n - i):
                res.append(matrix[i][j])
            # 上->下
            for j in range(i + 1, m - i - 1):
                res.append(matrix[j][n - i - 1])
            # 右->左
            for j in range(n - i - 1, i - 1, -1):
                # 右->左那一行不与左->右那一行重叠
                if i != m - i - 1:
                    res.append(matrix[m - i - 1][j])
            # 下->上
            for j in range(m - i - 2, i, -1):
                # 下->上那一列不与上->下那一列重叠
                if i != n - i - 1:
                    res.append(matrix[j][i])
        return res

if __name__ == '__main':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    s = Solution()
    print(s.spiralOrder(matrix))