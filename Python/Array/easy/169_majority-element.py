'''
169. 多数元素

给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。



示例 1:

输入: [3,2,3]
输出: 3

示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2

'''

# dict vs collections.defaultdict vs collections.OrderdDict
# defaultdict在找不到key时返回默认值，int返回0
# OrderDict有序字典，按插入顺序排序
from collections import defaultdict, OrderedDict

class Solution:
    def majorityElement(self, nums):
        '''
        @describe: 为每一个元素建立字典，记录其出现的次数，当出现次数超过一半时说明找到多数元素
        @param nums: List[int]
        @return: int
        '''
        dict_lst = defaultdict(int)
        for num in nums:
            dict_lst[num] += 1
            if dict_lst[num] >= int((len(nums) + 1)/2):
                return num
        return 0

class Solution2:
    def majorityElement(self, nums):
        '''
        @describe: 在有序数组处于中间的元素即多数元素
        @param nums: List[int]
        @return: int
        '''
        nums.sort()
        return nums[int(len(nums)/2)]

if __name__ == '__main__':
    nums = [6,5,5]
    s = Solution()
    print(s.majorityElement(nums))