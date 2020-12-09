'''
31. 下一个排列

实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须 原地 修改，只允许使用额外常数空间。



示例 1：

输入：nums = [1,2,3]
输出：[1,3,2]

示例 2：

输入：nums = [3,2,1]
输出：[1,2,3]

示例 3：

输入：nums = [1,1,5]
输出：[1,5,1]

示例 4：

输入：nums = [1]
输出：[1]



提示：

    1 <= nums.length <= 100
    0 <= nums[i] <= 100


'''

class Solution:
    def nextPermutation(self, nums):
        '''
        @describe:  双指针，i从右端开始遍历，遍历之后的数据从小到大排列
                    若发现nums[i]右边有比其大的数则置换，找到下一个更大的排列，否则将nums[i]移动到最右端
        @param nums: 数组
        @return: NULL
        '''
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    tmp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = tmp
                    return
            t = nums[i]
            del nums[i]
            nums.append(t)

if __name__ == '__main__':
    nums = [1,1,5]
    s = Solution()
    s.nextPermutation(nums)
    print(nums)