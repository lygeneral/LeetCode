'''
48. 旋转图像

给定一个 n × n 的二维矩阵表示一个图像。

将图像顺时针旋转 90 度。

说明：

你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

示例 1:

给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

示例 2:

给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]


'''


class Solution:
    def rotate(self, matrix):
        '''
        @describe: 遍历旋转图像90度
        @param matrix: 矩阵
        @return: NULL
        '''
        # 从外到内一圈又一圈的遍历，一共有int(len(matrix)/2)层
        for i in range(int(len(matrix)/2)):
            length = len(matrix) - 2 * i
            end = i + length - 1
            # 内圈遍历
            for j in range(0, length - 1):
                index = i + j
                # 左上角的元素
                tmp = matrix[i][index]
                # 左上角的元素 = 左下角的元素
                matrix[i][index] = matrix[end - j][i]
                # 左下角的元素 = 右下角的元素
                matrix[end - j][i] = matrix[end][end - j]
                # 右下角的元素 = 右上角的元素
                matrix[end][end - j] = matrix[index][end]
                # 右上角的元素 = 左上角的元素
                matrix[index][end] = tmp

if __name__ == '__main__':
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    s = Solution()
    s.rotate(matrix)
    print(matrix)