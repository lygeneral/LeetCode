'''
665. 非递减数列

给你一个长度为 n 的整数数组，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。

我们是这样定义一个非递减数列的： 对于数组中所有的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。



示例 1:

输入: nums = [4,2,3]
输出: true
解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。

示例 2:

输入: nums = [4,2,1]
输出: false
解释: 你不能在只改变一个元素的情况下将其变为非递减数列。



说明：

    1 <= n <= 10 ^ 4
    - 10 ^ 5 <= nums[i] <= 10 ^ 5

'''

class Solution:
    def checkPossibility(self, nums):
        '''
        @describe:  对于[1,4,2,1]，对于2<4的情况，即i=2时nums[i] < nums[i-1]
                    1.将nums[i]即2放大为nums[i-1]即4，并保证nums[i+1]的数不能比4小，即nums[i+1]>=nums[i-1]
                    2.将nums[i-1]即4缩小为nums[i]即2，并保证nums[i-2]的数不能比2大，即nums[i-2]<=nums[i-1]
                    若1和2均不能实现则说明无法将数组调整为非递减数组
        @param nums: 数组
        @return: 是否可以在只改变一个元素的情况下将其变为非递减数列
        '''
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i -1] > nums[i]:
                cnt += 1
                if i - 2 >= 0 and i + 1 < len(nums):
                    if nums[i - 2] > nums[i] and nums[i - 1] > nums[i+1]:
                        return False
            if cnt > 1:
                return False
        return True

if __name__ == '__main__':
    nums = [4,2,3]
    s = Solution()
    print(s.checkPossibility(nums))
