'''
33. 搜索旋转排序数组

给你一个整数数组 nums ，和一个整数 target 。

该整数数组原本是按升序排列，但输入时在预先未知的某个点上进行了旋转。（例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] ）。

请你在数组中搜索 target ，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。


示例 1：

输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4

示例 2：

输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1

示例 3：

输入：nums = [1], target = 0
输出：-1



提示：

    1 <= nums.length <= 5000
    -10^4 <= nums[i] <= 10^4
    nums 中的每个值都 独一无二
    nums 肯定会在某个点上旋转
    -10^4 <= target <= 10^4


'''

class Solution:
    def search(self, nums, target):
        '''
        @describe: 二分法
        @param nums: 查询数组
        @param target: 目标值
        @return: 索引
        '''
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = int(left + (right - left)/2)
            if nums[middle] == target:
                return middle
            # middle处于左半段
            if nums[middle] >= nums[left]:
                # 判断target处于左半段还是右半段
                if target >= nums[left] and target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            # middle处于右半段
            else:
                # 判断target处于左半段还是右半段
                if target > nums[middle] and target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
        return -1

class Solution2:
    def search(self, nums, target):
        '''
        @describe: 直接遍历寻找目标值
        @param nums: 查询数组
        @param target: 目标值
        @return: 索引
        '''
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1

if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    s = Solution()
    print(s.search(nums, target))