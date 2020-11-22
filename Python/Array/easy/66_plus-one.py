'''
66. 加一

给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

 

示例 1：

输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。

示例 2：

输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。

示例 3：

输入：digits = [0]
输出：[1]


提示：

    1 <= digits.length <= 100
    0 <= digits[i] <= 9

'''

class Solution:
    def plusOne(self, digits):
        '''
        @describe: 由后向前遍历数组，出现9则置0并进位，否则加1即可
        '''
        for i in range(len(digits), 0, -1):
            if(digits[i - 1] == 9):
                digits[i - 1] = 0
                if i == 1:
                    # 首位出现9的情况，需要进位，增加一位1
                    digits = [1] + digits
                continue
            else:
                digits[i - 1] += 1
                break
        return digits
    
if __name__ == '__main__':
    digits = [4,3,2,1]
    s = Solution()
    print(s.plusOne(digits))


