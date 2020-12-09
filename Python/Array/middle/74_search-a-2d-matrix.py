'''
74. 搜索二维矩阵

编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

    每行中的整数从左到右按升序排列。
    每行的第一个整数大于前一行的最后一个整数。



示例 1：

输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
输出：true

示例 2：

输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
输出：false

示例 3：

输入：matrix = [], target = 0
输出：false



提示：

    m == matrix.length
    n == matrix[i].length
    0 <= m, n <= 100
    -104 <= matrix[i][j], target <= 104


'''

class Solution:
    def searchMatrix(self, matrix, target):
        '''
        @describe: 全量元素二分查找
        @param matrix: 矩阵
        @param target: 目标值
        @return: 是否找到目标值
        '''
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m = len(matrix)
        n = len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            mid = int(l + (r - l)/2)
            # 行mid//n，列mid%n
            if target == matrix[mid//n][mid%n]:
                return True
            elif target > matrix[mid//n][mid%n]:
                l = mid + 1
            else:
                r = mid - 1
        return False

class Solution2:
    def searchMatrix(self, matrix, target):
        '''
        @describe: 先二分查找行，再二分查找列，加速寻找
        @param matrix: 矩阵
        @param target: 目标值
        @return: 是否找到目标值
        '''
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m = len(matrix)
        n = len(matrix[0])
        t, b = 0, m - 1
        # 查找行时找不到target时只要让最后的t=b即可，由于mid可能是t那一行，因此将mid = int(t + (b - t + 1)/2)，在t=1,b=2时mid=2
        while t < b:
            mid = int(t + (b - t + 1)/2)
            if target == matrix[mid][0]:
                return True
            elif target > matrix[mid][0]:
                t = mid
            else:
                b = mid - 1
        l, r = 0, n - 1
        # 查找时要让所有值都要找一遍，l<=r，即l=r时需要再寻找一次mid所在的元素是否等于target
        while l <= r:
            mid = int(l + (r - l)/2)
            if target == matrix[t][mid]:
                return True
            elif target > matrix[t][mid]:
                l = mid + 1
            else:
                r = mid - 1
        return False

class Solution3:
    def searchMatrix(self, matrix, target):
        '''
        @describe: 先找行，再找列，加速寻找
        @param matrix: 矩阵
        @param target: 目标值
        @return: 是否找到目标值
        '''
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            if target <= matrix[i][-1]:
                break
        for j in range(n):
            if target == matrix[i][j]:
                return True
        return False

if __name__ == '__main__':
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    target = 3
    s = Solution()
    print(s.setZeroes(matrix, target))