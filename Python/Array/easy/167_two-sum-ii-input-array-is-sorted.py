'''
167. 两数之和 II - 输入有序数组

给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

    返回的下标值（index1 和 index2）不是从零开始的。
    你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。

示例:

输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。


'''

class Solution:
    def twoSum(self, numbers, target):
        '''
        @describe:  双指针，由于有序数组，使用i从左至右，j从右至左遍历
                    指定i时j向左移动直至找到dest或numbers[j]<dest，然后i向右移动，不断循环此步骤
        @param numbers: List[int]
        @param target: int
        @return: List[int]
        '''
        j = len(numbers) - 1
        for i in range(len(numbers)):
            dest = target - numbers[i]
            while j > i:
                if dest == numbers[j]:
                    return [i + 1, j + 1]
                elif dest < numbers[j]:
                    j -= 1
                else:
                    break
        return []

class Solution2:
    def twoSum(self, numbers, target):
        '''
        @describe: 遍历计算target-numbers[0]后的数字，由于是有序数组，可采用二分查找法寻找
        @param numbers: List[int]
        @param target: int
        @return: List[int]
        '''
        for i in range(len(numbers)):
            dest = target - numbers[i]
            left= i + 1
            right = len(numbers) - 1
            # 考虑到可能找不到dest的情况，将最终结果锁定到middle即left=right的情况
            while left <= right:
                middle = int(left + (right - left) / 2)
                if numbers[middle] == dest:
                    return [i + 1, middle + 1]
                elif numbers[middle] < dest:
                    left = middle + 1
                else:
                    right = middle - 1
        return []


if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9
    s=Solution()
    print(s.twoSum(numbers, target))