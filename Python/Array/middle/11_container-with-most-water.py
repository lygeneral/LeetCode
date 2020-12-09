'''
11. 盛最多水的容器

给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器。



示例 1：

输入：[1,8,6,2,5,4,8,3,7]
输出：49
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

示例 2：

输入：height = [1,1]
输出：1

示例 3：

输入：height = [4,3,2,1,4]
输出：16

示例 4：

输入：height = [1,2,1]
输出：2



提示：

    n = height.length
    2 <= n <= 3 * 104
    0 <= height[i] <= 3 * 104


'''


class Solution:
    def maxArea(self, height):
        '''
        @describe: 双指针，i和j位于容器两端，height小的为短板，只有在短板变长时水槽面积才增大，因此向内移动height小的
        @param height: 数组
        @return: 最大水槽面积
        '''
        i = 0
        j = len(height) - 1
        maxv = 0
        while i < j:
            v = min(height[i], height[j]) * (j - i)
            maxv = max(maxv, v)
            if height[i] < height[j]:
                i += 1
                while height[i] < height[i - 1]:
                    i += 1
            else:
                j -= 1
                while height[j] < height[j + 1]:
                    j -= 1
        return maxv

if __name__ == '__main__':
    height = [4,3,2,1,4]
    s = Solution()
    print(s.maxArea(height))