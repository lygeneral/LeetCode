'''
78. 子集

给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]


'''


class Solution:
    def subsets(self, nums):
        '''
        @describe: 回溯，从第一个元素迭代至最后一个元素
        @param nums: 数组
        @return: 子集
        '''
        res = []
        res.append([])
        def backTrack(index, tmp, nums):
            if index == len(nums):
                return
            for i in range(index, len(nums)):
                res.append(tmp + [nums[i]])
                backTrack(i + 1, tmp + [nums[i]], nums)
        backTrack(0, [], nums)
        return res

if __name__ == '__main__':
    nums = [1,2,3]
    s = Solution()
    print(s.subsets(nums))