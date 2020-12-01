'''
268. 丢失的数字

给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。



进阶：

    你能否实现线性时间复杂度、仅使用额外常数空间的算法解决此问题?



示例 1：

输入：nums = [3,0,1]
输出：2
解释：n = 3，因为有 3 个数字，所以所有的数字都在范围 [0,3] 内。2 是丢失的数字，因为它没有出现在 nums 中。

示例 2：

输入：nums = [0,1]
输出：2
解释：n = 2，因为有 2 个数字，所以所有的数字都在范围 [0,2] 内。2 是丢失的数字，因为它没有出现在 nums 中。

示例 3：

输入：nums = [9,6,4,2,3,5,7,0,1]
输出：8
解释：n = 9，因为有 9 个数字，所以所有的数字都在范围 [0,9] 内。8 是丢失的数字，因为它没有出现在 nums 中。

示例 4：

输入：nums = [0]
输出：1
解释：n = 1，因为有 1 个数字，所以所有的数字都在范围 [0,1] 内。1 是丢失的数字，因为它没有出现在 nums 中。



提示：

    n == nums.length
    1 <= n <= 104
    0 <= nums[i] <= n
    nums 中的所有数字都 独一无二

'''

class Solution:
    def missingNumber(self, nums):
        '''
        @describe: 先从小到大排序，然后遍历数组，当首元素不为0时缺0，当该元素与上一个元素之差不为1时，说明中间缺数（num[i]-1），否则缺最后一个数（num[i - 1]+1
        @param nums: 数组
        @return: 缺失的数
        '''
        nums.sort()
        if nums[0] != 0:
            return 0
        i = 1
        while i < len(nums):
            if nums[i] - nums[i - 1] != 1:
                return nums[i] - 1
            i += 1
        return nums[i - 1] + 1


class Solution2:
    def missingNumber(self, nums):
        '''
        @describe: 基于等差数列求和公式求和与当前数组和的差即为缺失的数
        @param nums: 数组
        @return: 缺失的数
        '''
        n = len(nums)
        return int(n * (n + 1) / 2 -sum(nums))

if __name__ == '__main__':
    nums = [0, 1]
    s = Solution()
    print(s.missingNumber((nums)))