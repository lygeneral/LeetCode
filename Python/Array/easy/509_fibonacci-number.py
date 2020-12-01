'''
509. 斐波那契数

斐波那契数，通常用 F(n) 表示，形成的序列称为斐波那契数列。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.

给定 N，计算 F(N)。



示例 1：

输入：2
输出：1
解释：F(2) = F(1) + F(0) = 1 + 0 = 1.

示例 2：

输入：3
输出：2
解释：F(3) = F(2) + F(1) = 1 + 1 = 2.

示例 3：

输入：4
输出：3
解释：F(4) = F(3) + F(2) = 2 + 1 = 3.



提示：

    0 ≤ N ≤ 30

'''



# 优于Solution2、Solution3
class Solution:
    def fib(self, N):
        '''
        @describe: 定义F(N-2)为f1，F(N-1)为f2，F(N) = F(N - 1) + F(N - 2)迭代更新后，f2=f1+f2，f1=f2
        @param N: 数组
        @return: f(N)即更新后的f2
        '''
        if N <= 1:
            return N
        f1, f2 = 0, 1
        for i in range(2, N + 1):
            f1, f2 = f2, f1 + f2
        return f2

class Solution2:
    def fib(self, N):
        '''
        @describe: 动态规划，F(N) = F(N - 1) + F(N - 2)计算数组中新的元素
        @param N: 数组
        @return: f(N)即array中最新的元素
        '''
        if N <= 1:
            return N
        array = [0, 1]
        for i in range(2, N + 1):
            tmp = array[-1] + array[-2]
            array.append(tmp)
        return array[-1]

class Solution3:
    def fib(self, N):
        '''
        @describe: 递归，耗时长
        @param N: 数组
        @return: f(N)即array中最新的元素
        '''
        # 类中递归函数前需增加self
        return N if N < 2 else self.fib(N-1) + self.fib(N-2)

if __name__ == '__main__':
    N = 2
    s = Solution()
    print(s.fib(N))