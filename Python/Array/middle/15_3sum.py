'''
15. 三数之和

给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。



示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

通过次数373,027
提交次数1,237,156

'''

class Solution:
    def threeSum(self, nums):
        '''
        @describe: 排序+双指针，排序后第一层遍历i，然后j和k双指针
        @param nums: 数组
        @return: 元组
        '''
        nums.sort()
        res = []
        i = 0
        while i < len(nums):
            # i跳过重复数字，例如[0,0]
            while i > 0 and i < len(nums) and nums[i - 1] == nums[i]:
                i += 1
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if 0 == nums[i] + nums[j] + nums[k]:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    # i之后出现多个重复的数字则跳过，例如[-2,0,0,2,2]
                    while j < len(nums) and nums[j] == nums[j - 1]:
                        j += 1
                    while k > 0 and nums[k] == nums[k + 1]:
                        k -= 1
                elif 0 > nums[i] + nums[j] + nums[k]:
                    j += 1
                else:
                    k -= 1
            i += 1
        return res

if __name__ == '__main__':
    nums = [-2,0,0,0,-1,-1,1,1,2,2]
    s = Solution()
    print(s.threeSum(nums))