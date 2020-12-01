'''
643. 子数组最大平均数 I

给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。

示例 1:

输入: [1,12,-5,-6,50,3], k = 4
输出: 12.75
解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75



注意:

    1 <= k <= n <= 30,000。
    所给数据范围 [-10,000，10,000]。


'''

class Solution:
    def findMaxAverage(self, nums, k):
        tmp = nums[:k]
        sums = sum(tmp)
        maxsum = sums
        for i in range(k, len(nums)):
            sums = sums - tmp[0] + nums[i]
            del tmp[0]
            tmp.append(nums[i])
            if sums > maxsum:
                maxsum = sums
        return maxsum/k


if __name__ == '__main__':
    nums = [0,4,0,3,2]
    k = 1
    s = Solution()
    print(s.findMaxAverage(nums,k))