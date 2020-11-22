'''
867.转置矩阵

给定一个矩阵 A， 返回 A 的转置矩阵。

矩阵的转置是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。



示例 1：

输入：[[1,2,3],[4,5,6],[7,8,9]]
输出：[[1,4,7],[2,5,8],[3,6,9]]

示例 2：

输入：[[1,2,3],[4,5,6]]
输出：[[1,4],[2,5],[3,6]]



提示：

    1 <= A.length <= 1000
    1 <= A[0].length <= 1000

'''


class Solution:
    def transpose(self, A):
        '''
        @describe: 按列->行的顺序遍历矩阵，把每一列组成list变成行，然后添加进list，完成行列转换
        @param A: List[List[int]]
        @return: List[List[int]]
        '''
        res = []
        for j in range(len(A[0])):
            tmp = []
            for i in range(len(A)):
                tmp.append(A[i][j])
            res.append(tmp)
        return res

if __name__ == '__main__':
    A = [[1,2,3],[4,5,6]]
    s = Solution()
    print(s.transpose(A))

