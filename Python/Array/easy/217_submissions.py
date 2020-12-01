'''
217. 存在重复元素

给定一个整数数组，判断是否存在重复元素。

如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。



示例 1:

输入: [1,2,3,1]
输出: true

示例 2:

输入: [1,2,3,4]
输出: false

示例 3:

输入: [1,1,1,3,3,4,3,2,4,2]
输出: true

'''

from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums):
        '''
        @describe: 为每一个元素建立字典，记录其出现的次数，当出现次数超过一次时说明找到重复元素
        @param nums: List[int]
        @return: int
        '''
        dictRes = defaultdict(int)
        for num in nums:
            dictRes[num] += 1
            if dictRes[num] > 1:
                return True
        return False

class Solution2:
    def containsDuplicate(self, nums):
        '''
        @describe: 将list转化为无序不重复元素集，若元素数量减少则说明有重复元素
        @param nums: List[int]
        @return: int
        '''
        setRes = set(nums)
        return len(nums ) != len(setRes)

if __name__ == '__main__':
    nums = [1,1,1,3,3,4,3,2,4,2]
    s = Solution()
    print(s.containsDuplicate(nums))
