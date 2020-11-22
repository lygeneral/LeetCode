'''
88. 合并两个有序数组

给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

 

说明：

    初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
    你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

 

示例：

输入：
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出：[1,2,2,3,5,6]

 

提示：

    -10^9 <= nums1[i], nums2[i] <= 10^9
    nums1.length == m + n
    nums2.length == n


'''


class Solution:
    def merge(self, nums1, m, nums2, n):
        '''
        @describe: list切片
        '''
        nums1[m:] = nums2[:n]
        nums1.sort()


class Solution2:
    def merge(self, nums1, m, nums2, n):
        '''
        @describe: 三个指针，其中两个指向m和n元素，一个指向合并结果的数组，逆向比较并合并结果
                   m所有元素与n合并后，n未完成合并，则直接将n中剩余元素覆盖至结果数组中
        '''
        mIndex = m - 1
        nIndex = n - 1
        for showIndex in range(m + n, 0, -1):
            if mIndex < 0 or nIndex < 0:
                break
            if nums1[mIndex] >= nums2[nIndex]:
                nums1[showIndex - 1] = nums1[mIndex]
                mIndex -= 1
            else:
                nums1[showIndex - 1] = nums2[nIndex]
                nIndex -= 1
        if nIndex >= 0:
            for i in range(nIndex + 1):
                nums1[i] = nums2[i]

if __name__ == '__main__':
    nums1 = [0]
    m = 0
    nums2= [1]
    n = 1
    s=Solution()
    s.merge(nums1,m,nums2,n)
    print(nums1)