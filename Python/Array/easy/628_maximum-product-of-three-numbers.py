'''
628. 三个数的最大乘积

给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

示例 1:

输入: [1,2,3]
输出: 6

示例 2:

输入: [1,2,3,4]
输出: 24

注意:

    给定的整型数组长度范围是[3,104]，数组中所有的元素范围是[-1000, 1000]。
    输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。


'''


class Solution:
    def maximumProduct(self, nums):
        '''
        @describe: 遍历，最大值可能出现在top3的乘积；但如果有两个以上负数时，一正*两负也可能是最大值，因此最大值可能是max1*min1*min2
        @param nums: 数组
        @return: 三个数的最大乘积
        '''
        max1, max2, max3 = [-float('inf')] * 3
        min1, min2 = [float('inf')] * 2
        for num in nums:
            if num > max1:
                max1, max2, max3 = num, max1, max2
            elif num > max2:
                max2, max3 = num, max2
            elif num > max3:
                max3 = num
            if num < min1:
                min1, min2 = num, min1
            elif num < min2:
                min2 = num
        return max(max1 * max2 * max3, max1 * min1 * min2)

class Solution2:
    def maximumProduct(self, nums):
        '''
        @describe: 先排序后，基于正负几种情况计算三个元素乘积取最大值
        @param nums: 数组
        @return: 三个数的最大乘积
        '''
        nums = sorted(nums, reverse = True)
        # 排序后nums从大到小排列
        # [正,正,...,正,正/负]（全正或仅有一个负数）,[负,负,负,负,...]（全负，三个元素相乘最大值只能是负数）=>max为nums[0]*nums[1]*nums[2]
        # [正,正,正,负,...,负,负]（三个及以上正数，两个以上负数）=>max为nums[0]*nums[1]*nums[2]或nums[0]*nums[-1]*nums[-2]
        # [正,正/负,负,...,负,负]（两个或一个正数，两个以上负数）=>max为nums[0]*nums[-1]*nums[-2]
        return max(nums[0]*nums[1]*nums[2], nums[0]*nums[-1]*nums[-2])



if __name__ == '__main__':
    nums = [1,2,4,2]
    s =Solution()
    print(s.maximumProduct(nums))