'''
605. 种花问题

假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数 n 。能否在不打破种植规则的情况下种入 n 朵花？能则返回True，不能则返回False。

示例 1:

输入: flowerbed = [1,0,0,0,1], n = 1
输出: True

示例 2:

输入: flowerbed = [1,0,0,0,1], n = 2
输出: False

注意:

    数组内已种好的花不会违反种植规则。
    输入的数组长度范围为 [1, 20000]。
    n 是非负整数，且不会超过输入数组的大小。

'''


# 优于Solution2，但思路一样，只是对元素两边扩展，将判断语句适用于单元素的原数组和原数组中第一个和最后一个元素
class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        '''
        @describe: 遍历，判断该位置的元素为0且相邻元素为0时该位置可以种花，则n=n-1
        @param flowerbed: 数组
        @param n: n朵花
        @return: 是否能种n朵花
        '''
        # 对数组前后做扩展处理
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
        return n <= 0

class Solution2:
    def canPlaceFlowers(self, flowerbed, n):
        '''
        @describe: 遍历，判断该位置的元素为0且相邻元素为0时该位置可以种花，则n=n-1
        @param flowerbed: 数组
        @param n: n朵花
        @return: 是否能种n朵花
        '''
        # 仅有一个元素时特殊处理
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                n -= 1
            return n <= 0
        for i in range(len(flowerbed)):
            # 第一个位置仅需判断两个元素
            if i == 0:
                if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
            # 最后一个位置仅需判断两个元素
            elif i == len(flowerbed) - 1:
                if flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
            # 中间的位置需判断三个元素
            else:
                if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
        return n <= 0

if __name__ == '__main__':
    flowerbed = [1,0,0,0,1]
    s = Solution()
    print(s.canPlaceFlowers(flowerbed,1))