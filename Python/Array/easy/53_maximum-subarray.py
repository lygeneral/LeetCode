'''
53.最大子序和

给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

'''

class Solution:
    def maxSubArray(self, nums):
        '''
        @describe:  遍历数组，在数组前统计元素sum大于0时继续统计，否则另起炉灶，以该元素为起点计算sum
                    计算sum后将sum与之前记录的max比较取最大
        '''
        sum_tmp = 0
        res = nums[0]
        for num in nums:
            if sum_tmp > 0:
                sum_tmp += num
            else:
                sum_tmp = num
            res = max(res, sum_tmp)
        return res

if __name__ == '__main__':
    nums = [-2,-1,-3,-4,-1,-2,-1,-5,-4]
    s=Solution()
    print(s.maxSubArray(nums))