'''
1.两数之和

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。



示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

'''

class Solution1:
    def twoSum(self, nums, target):
        '''
        @describe: 暴力遍历破解，计算两数之和
        @param nums: List[int]
        @param target: int
        @return: List[int]
        '''
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                sum = nums[i] + nums[j]
                if(sum == target):
                    return [i, j]
        return []

class Solution2:
    def twoSum(self, nums, target):
        '''
        @describe: 暴力遍历破解，计算两数之和
        @param nums: List[int]
        @param target: int
        @return: List[int]
        '''
        for i in range(len(nums)):
            tmp = target - nums[i]
            lst = nums[i + 1:]
            if tmp in lst:
                return [i, j]
        return []