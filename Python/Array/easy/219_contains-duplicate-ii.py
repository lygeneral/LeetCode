'''
219. 存在重复元素 II

给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。



示例 1:

输入: nums = [1,2,3,1], k = 3
输出: true

示例 2:

输入: nums = [1,0,1,1], k = 1
输出: true

示例 3:

输入: nums = [1,2,3,1,2,3], k = 2
输出: false

'''

class Solution:
    def containsDuplicate(self, nums, k):
        '''
        @describe: 为每一个元素建立字典（以元素为key，其索引为value），当本次索引-上次索引<=k时找到重复元素
        @param nums: List[int]
        @return: int
        '''
        dict_nums = dict()
        for i in range(len(nums)):
            num = nums[i]
            if num in dict_nums and (i - dict_nums[num]) <= k:
                return True
            dict_nums[num] = i
        return False


if __name__ == '__main__':
    nums = [1,0,1,1]
    k = 1
    s = Solution()
    print(s.containsDuplicate(nums, k))