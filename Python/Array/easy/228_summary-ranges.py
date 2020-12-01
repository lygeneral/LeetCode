'''
228. 汇总区间

给定一个无重复元素的有序整数数组 nums 。

返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表。也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于 nums 的数字 x 。

列表中的每个区间范围 [a,b] 应该按如下格式输出：

    "a->b" ，如果 a != b
    "a" ，如果 a == b



示例 1：

输入：nums = [0,1,2,4,5,7]
输出：["0->2","4->5","7"]
解释：区间范围是：
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

示例 2：

输入：nums = [0,2,3,4,6,8,9]
输出：["0","2->4","6","8->9"]
解释：区间范围是：
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

示例 3：

输入：nums = []
输出：[]

示例 4：

输入：nums = [-1]
输出：["-1"]

示例 5：

输入：nums = [0]
输出：["0"]



提示：

    0 <= nums.length <= 20
    -231 <= nums[i] <= 231 - 1
    nums 中的所有值都 互不相同

'''

class Solution:
    def summaryRanges(self, nums):
        '''
        @describe: 遇到连续元素不断向后移动，框定连续元素的区域范围
        @param nums: List[int]
        @return: int
        '''
        res = []
        # 初始化left和right指针为起点
        left = 0
        right = 0
        while right < len(nums):
            # 当不溢出且下一个元素是连续的时，right不断向后移动，框定该区域
            while (right + 1) < len(nums) and (nums[right + 1] - nums[right]) == 1:
                right += 1
            if left == right:
                res.append(str(nums[left]))
            else:
                res.append(str(nums[left]) + '->' + str(nums[right]))
            # 完成上一区域数据的写入，将left和right均再向后移动
            right += 1
            left = right
        return res

class Solution2:
    def summaryRanges(self, nums):
        '''
        @describe: 遍历寻找非连续元素，将当前区域和后一个区域分割，当遍历到最后一个元素时特殊处理
        @param nums: List[int]
        @return: int
        '''
        res = []
        # 初始化left和right指针为起点
        left = 0
        right = 0
        for i in range(len(nums)):
            # 情况1：如果遍历的元素是最后一个时将该区域的元素写入res
            # 情况2：不是最后一个元素且后一个与前一个元素不连续时，分割区域将上一个区域的数据写入res，并后移left
            if i == len(nums) - 1 or (nums[i + 1] - nums[i]) != 1:
                if left == right:
                    res.append(str(nums[left]))
                else:
                    res.append(str(nums[left]) + '->' + str(nums[right]))
                left = i + 1
            # 无论后一个元素是否与前一个元素连续，均后移right
            right = i + 1
        return res

if __name__ == '__main__':
    nums = [1,4,6]
    s = Solution()
    print(s.summaryRanges(nums))

