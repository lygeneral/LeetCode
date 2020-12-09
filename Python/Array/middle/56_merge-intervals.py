'''
56. 合并区间

给出一个区间的集合，请合并所有重叠的区间。



示例 1:

输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例 2:

输入: intervals = [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

注意：输入类型已于2019年4月15日更改。 请重置默认代码定义以获取新方法签名。



提示：

    intervals[i][0] <= intervals[i][1]


'''

class Solution:
    def merge(self, intervals):
        '''
        @describe: 先按intervals[0]排序，遍历合并区间，找到分割点，有点动态规划的感觉
        @param intervals: 二维数组
        @return: 合并后的区间
        '''
        intervals = sorted(intervals, key=lambda x:x[0])
        res = []
        i = 1
        while i < len(intervals):
            if intervals[i][0] <= intervals[i - 1][1]:
                top = max(intervals[i][1], intervals[i-1][1])
                intervals[i] = [intervals[i - 1][0], top]
            else:
                res.append(intervals[i - 1])
            i += 1
        res.append(intervals[i - 1])
        return res

if __name__ == '__main__':
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    s = Solution()
    print(s.merge(intervals))