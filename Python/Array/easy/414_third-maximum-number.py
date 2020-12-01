'''
414. 第三大的数

给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。

示例 1:

输入: [3, 2, 1]

输出: 1

解释: 第三大的数是 1.

示例 2:

输入: [1, 2]

输出: 2

解释: 第三大的数不存在, 所以返回最大的数 2 .

示例 3:

输入: [2, 2, 3, 1]

输出: 1

解释: 注意，要求返回第三大的数，是指第三大且唯一出现的数。
存在两个值为2的数，它们都排第二。

'''

class Solution:
    def thirdMax(self, nums):
        '''
        @describe: 遍历判断元素大小，选择Top3的元素
        @param nums:
        @return:
        '''
        first, second, third = [-float('inf')] * 3
        for num in nums:
            # 判断该元素是否与top3元素重合，重合则跳过，否则依次比较其与三个元素的大小
            if num == first or num == second or num == third:
                continue
            elif num > first:
                first, second, third = num, first, second
            elif num > second:
                second, third = num, second
            elif num > third:
                third = num
        return third if third != -float('inf') else first

class Solution2:
    def thirdMax(self, nums):
        '''
        @describe: 基于python的set及max函数寻找第三大元素
        @param nums: 数组
        @return: 第三大元素
        '''
        set_lst = set(nums)
        if len(set_lst) < 3:
            return max(set_lst)
        for i in range(2):
            maxnum = max(set_lst)
            set_lst.remove(maxnum)
        return max(set_lst)

if __name__ == '__main__':
    nums = [1,2,3]
    s = Solution()
    print(s.thirdMax(nums))