'''
485. 最大连续1的个数

给定一个二进制数组， 计算其中最大连续1的个数。

示例 1:

输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.

注意：

    输入的数组只包含 0 和1。
    输入数组的长度是正整数，且不超过 10,000。


'''

# 优于Solution2、Solution3
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        '''
        @describe: 双指针，i定义1的起始点，j定义1的结束点的下一个元素，len=j-1，寻找最大的len即为结果
        @param nums: 数组
        @return: 最大连续1的个数
        '''
        i = 0
        maxlen = 0
        # 遍历数组
        while i < len(nums):
            # 当元素为1时定义i为起始点
            while i < len(nums) and nums[i] != 1:
                i += 1
            # 不断遍历直至j对应元素不为1
            j = i
            while j < len(nums) and nums[j] == 1:
                j += 1
            maxlen = max(j - i, maxlen)
            i = j
        return maxlen


class Solution2:
    def findMaxConsecutiveOnes(self, nums):
        '''
        @describe: 双指针，i定义1的起始点，j定义1的结束点的下一个元素，len=j-1，寻找最大的len即为结果
        @param nums: 数组
        @return: 最大连续1的个数
        '''
        i = 0
        maxlen = 0
        # 遍历数组
        while i < len(nums):
            if nums[i] == 1:
                j = i + 1
                while j < len(nums) and nums[j] == 1:
                    j += 1
                maxlen = max(j - i, maxlen)
                i = j
            # 元素不为1则跳过
            else:
                i += 1
        return maxlen


class Solution3:
    def findMaxConsecutiveOnes(self, nums):
        '''
        @describe: 单指针遍历数组遇到1则加1，否则length复位，每次循环比较当前length和最大值
        @param nums: 数组
        @return: 最大连续1的个数
        '''
        length = 0
        maxlen = 0
        # 遍历数组
        for num in nums:
            if num == 1:
                length += 1
            else:
                maxlen = max(length, maxlen)
                length = 0
        return max(length, maxlen)

if __name__ == '__main__':
    nums = [1,1,0,1,1,1]
    s = Solution()
    print(s.findMaxConsecutiveOnes(nums))