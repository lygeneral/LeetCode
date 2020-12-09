'''
18. 四数之和

给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]


'''

class Solution:
    def foruSum(self, nums, target):
        '''
        @describe: 排序+两层遍历+双指针
        @param nums: 数组
        @param target: 目标值
        @return: 四元组
        '''
        nums.sort()
        i = 0
        res = []
        while i < len(nums):
            for j in range(i + 1, len(nums)):
                m = j + 1
                n = len(nums) - 1
                while m < n:
                    t = nums[i] + nums[j] + nums[m] + nums[n]
                    if t == target:
                        tmp = [nums[i],nums[j],nums[m],nums[n]]
                        # 排除重复四元组
                        if tmp not in res:
                            res.append(tmp)
                        m += 1
                        n -= 1
                    elif t < target:
                        m += 1
                    else:
                        n -= 1
            i += 1
        return res

if __name__ == '__main__':
    nums = [1,2,3,4]
    target = 4
    s = Solution()
    print(s.foruSum(nums,target))