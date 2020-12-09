'''
16. 最接近的三数之和

给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。



示例：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。



提示：

    3 <= nums.length <= 10^3
    -10^3 <= nums[i] <= 10^3
    -10^4 <= target <= 10^4

'''

class Solution:
    def threeSumCloset(self, nums, target):
        '''
        @describe: 排序+双指针
        @param nums: 数组
        @param target: targe目标值
        @return: 三值和
        '''
        nums = sorted(nums)
        res = sum(nums[:3])
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                t = nums[i] + nums[j] + nums[k]
                if t == target:
                    return target
                elif t > target:
                    k -= 1
                else:
                    j += 1
                if abs(res - target) > abs(t - target):
                    res = t
        return res

if __name__ == '__main__':
    nums = [-1,2,1,-4]
    target = 2
    s = Solution()
    print(s.threeSumCloset(nums, target))