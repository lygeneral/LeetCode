'''
35.搜索插入位置

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2

示例 2:

输入: [1,3,5,6], 2
输出: 1

示例 3:

输入: [1,3,5,6], 7
输出: 4

示例 4:

输入: [1,3,5,6], 0
输出: 0

'''

class Solution:
    def searchInsert(self, nums, target):
        '''
        @describe: 二分法，注意left<=right的等号对应left的范围
        '''
        left = 0
        right = len(nums) - 1
        while left <= right:
            # int向下取整，比如int(2.1)=2 int(2.9)=2
            # 在left<right情况下mid<right，left边界为[0,right]
            # 在left<=right情况下left=right时可能出现left=right+1的情况，left边界为[0,right+1]
            middle = int(left + (right - left) / 2) #mid的标准写法
            if nums[middle] ==  target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return left

class Solution2:
    def searchInsert(self, nums, target):
        '''
        @describe: 遍历查找
        '''
        for i in range(len(nums)):
            if target <= nums[i]:
                return i
        return len(nums)

if __name__ == '__main__':
    nums = [1,3]
    target = 7
    s = Solution()
    print(s.searchInsert(nums, target))

