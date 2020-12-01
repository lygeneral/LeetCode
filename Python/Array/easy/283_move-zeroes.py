'''
283. 移动零

给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]

说明:

    必须在原数组上操作，不能拷贝额外的数组。
    尽量减少操作次数。

'''

class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums) - 1
        while i <= j:
            # 找到0则后移并将j指针前移
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
                j -= 1
            else:
                i += 1

if __name__ == '__main__':
    nums = [0,1,2]
    s = Solution()
    s.moveZeroes(nums)
    print(nums)