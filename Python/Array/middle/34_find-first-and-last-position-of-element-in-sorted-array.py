'''
34. 在排序数组中查找元素的第一个和最后一个位置

给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

进阶：

    你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？



示例 1：

输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]

示例 2：

输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]

示例 3：

输入：nums = [], target = 0
输出：[-1,-1]



提示：

    0 <= nums.length <= 105
    -109 <= nums[i] <= 109
    nums 是一个非递减数组
    -109 <= target <= 109


'''

# 将Solution2寻找边界的过程前置
class Solution:
    def searchRange(self, nums, target):
        '''
        @describe: 二分法寻找目标值，然后基于找到的目标值向两侧寻找边界，时间复杂度O(logn)
        @param nums: 数组
        @param target: 目标值
        @return: 边界
        '''
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = int(left + (right - left)/2)
            if nums[middle] == target:
                left, right = middle, middle
                while left >= 0 and nums[left] == nums[middle]:
                    left -= 1
                while right < len(nums) and nums[right] == nums[middle]:
                    right += 1
                break
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        # 若找到边界则left必定小于right
        if left < right:
            return [left + 1, right - 1]
        return [-1, -1]



class Solution2:
    def searchRange(self, nums, target):
        '''
        @describe: 二分法寻找目标值，然后基于找到的目标值向两侧寻找边界，时间复杂度O(logn)
        @param nums: 数组
        @param target: 目标值
        @return: 边界
        '''
        if len(nums) == 0:
            return [-1, -1]
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = int(left + (right - left)/2)
            if nums[middle] == target:
                break
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        i, j = middle, middle
        while i >= 0 and nums[i] == target:
            i -= 1
        while j < len(nums) and nums[j] == target:
            j += 1
        if i == j:
            return [-1, -1]
        return [i + 1, j - 1]

if __name__ == '__main__':
    nums = []
    target = 0
    s = Solution()
    print(s.searchRange(nums, target))