'''
75. 颜色分类

给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。



进阶：

    你可以不使用代码库中的排序函数来解决这道题吗？
    你能想出一个仅使用常数空间的一趟扫描算法吗？



示例 1：

输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]

示例 2：

输入：nums = [2,0,1]
输出：[0,1,2]

示例 3：

输入：nums = [0]
输出：[0]

示例 4：

输入：nums = [1]
输出：[1]



提示：

    n == nums.length
    1 <= n <= 300
    nums[i] 为 0、1 或 2


'''

class Solution:
    def sortColors(self, nums):
        '''
        @describe: 单指针，先遍历一次将0前置，然后遍历一次将2后置
        @param nums: 数组
        @return: NULL
        '''
        cur = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i], nums[cur] = nums[cur], nums[i]
                cur += 1
        cur = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 2:
                nums[i], nums[cur] = nums[cur], nums[i]
                cur -= 1

class Solution2:
    def sortColors(self, nums):
        '''
        @describe:  双指针，i <= cur <= j，当cur为2时将cur换到后面去，当为0时换到前面去，保证cur遍历过后cur前一个数非0即1
                    若cur前一个数为1由于i未动，在之后遇到0时可以进行置换，将0换到前面去，1换到后面来
        @param nums: 数组
        @return: NULL
        '''
        i = 0
        cur = 0
        j = len(nums) - 1
        while cur <= j:
            if nums[cur] == 0:
                nums[i], nums[cur] = nums[cur], nums[i]
                i += 1
                cur += 1
            elif nums[cur] == 2:
                nums[j], nums[cur] = nums[cur], nums[j]
                j -= 1
            else:
                cur += 1

if __name__ == '__main__':
    nums = [2,0,2,1,1,0]
    s = Solution()
    s.sortColors(nums)
    print(nums)
