'''
119. 杨辉三角 II

给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。

在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 3
输出: [1,3,3,1]

'''

class Solution:
    def getRow(self, rowIndex):
        '''
        @describe: 下一行 = [0 上一行] + [上一行 0]，即[1,3,3,1]=[0,1,2,1]+[1,2,1,0]
        @param rowIndex: int，从0开始第rowIndex行有rowIndex+1个元素
        @return: List[int]
        '''
        res = [1]
        for i in range(1, rowIndex + 1):
            left = res.copy()
            left.insert(0,0)
            right = res.copy()
            right.append(0)
            res = [a + b for a, b in zip(left, right)]
        return res


class Solution2:
    def getRow(self, rowIndex):
        '''
        @describe: 基于动态规划，从rowIndex=2那一行开始迭代
        @param rowIndex: int，从0开始第rowIndex行有rowIndex+1个元素
        @return: List[int]
        '''
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]

        vector = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            # 从第二行开始动态规划，第二行共三个元素，第一个和第三个均为0，第二个为上一行第二个和前一个元素之和
            for j in range(i - 1, 0, -1):
                vector[j] = vector[j] + vector[j - 1]
        return vector

if __name__ == '__main__':
    rowIndex = 3
    s=Solution()
    print(s.getRow((rowIndex)))