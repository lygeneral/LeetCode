'''
448. 找到所有数组中消失的数字

给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。

找到所有在 [1, n] 范围之间没有出现在数组中的数字。

您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

示例:

输入:
[4,3,2,7,8,2,3,1]

输出:
[5,6]


'''

class Solution:
    def findDisappearedNumbers(self, nums):
        '''
        @describe:  定义数组内元素为（下标+1），当存在某数字时其对应下标所在元素置为负数，即[4,3,2,7,8,2,3,1]转化为[-4,-3,-2,-7,8,2,-3,-1]
                    然后在其中寻找为正数的元素下标再加一则为缺失的元素[4+1, 5+1]
        @param nums:
        @return:
        '''
        for num in nums:
            num = abs(num)
            nums[num - 1] = abs(nums[num - 1]) * (-1)
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        return res

if __name__ == '__main__':
    nums = [4,3,2,7,8,2,3,1]
    s = Solution()
    print(s.findDisappearedNumbers(nums))
