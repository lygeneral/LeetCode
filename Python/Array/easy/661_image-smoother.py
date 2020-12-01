'''
661. 图片平滑器

包含整数的二维矩阵 M 表示一个图片的灰度。你需要设计一个平滑器来让每一个单元的灰度成为平均灰度 (向下舍入) ，平均灰度的计算是周围的8个单元和它本身的值求平均，如果周围的单元格不足八个，则尽可能多的利用它们。

示例 1:

输入:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
输出:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
解释:
对于点 (0,0), (0,2), (2,0), (2,2): 平均(3/4) = 平均(0.75) = 0
对于点 (0,1), (1,0), (1,2), (2,1): 平均(5/6) = 平均(0.83333333) = 0
对于点 (1,1): 平均(8/9) = 平均(0.88888889) = 0

注意:

    给定矩阵中的整数范围为 [0, 255]。
    矩阵的长和宽的范围均为 [1, 150]。


'''


class Solution:
    def imageSmoother(self, M):
        '''
        @describe: 遍历所有点，常规使用该点上下左右8个点进行处理，边界使用上下左右限处理
        @param M: 矩阵
        @return: 矩阵
        '''
        row = len(M)
        col = len(M[0])
        # 此处有雷，采用该方法进行初始化，切勿使用[xx]*xx的方式初始化
        res = [[1 for i in range(col)] for i in range(row)]
        for i in range(row * col):
            cur_row = i // col
            cur_col = i % col
            # 由当前坐标扩散至周围8个元素坐标
            x1, x2, y1, y2 = cur_col - 1, cur_col + 1, cur_row - 1, cur_row + 1
            if x1 < 0:
                x1 = 0
            if x2 >= col:
                x2 = col - 1
            if y1 < 0:
                y1 = 0
            if y2 >= row:
                y2 = row - 1
            sums = 0
            for i in range(y1, y2 + 1, 1):
                for j in range(x1, x2 + 1, 1):
                    sums += M[i][j]
            res[cur_row][cur_col] = int(sums / ((x2 - x1 + 1) * (y2 - y1 + 1)))
        return res

if __name__ == '__main__':
    M = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
    s = Solution()
    print(s.imageSmoother(M))