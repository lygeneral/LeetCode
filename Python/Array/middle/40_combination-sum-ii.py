'''
40. 组合总和 II

给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

    所有数字（包括目标数）都是正整数。
    解集不能包含重复的组合。

示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]


'''



class Solution:
    def combinationSum(self, candidates, target):
        '''
        @describe: 回溯法，迭代中写明返回条件，并在迭代过程中将组合写入res
        @param candidates: 数组
        @param target: 目标值
        @return: 组合
        '''
        res =[]
        tmplist = []
        candidates.sort()
        def backTrack(start, candidates, target, tmplist):
            # 满足该条件返回
            if target == 0:
                res.append(tmplist)
                return
            elif target < 0:
                return
            # 遍历迭代，将每一种可能都进行迭代
            for i in range(start, len(candidates)):
                # 不让相同的元素遍历多次
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                backTrack(i + 1, candidates, target - candidates[i], tmplist + [candidates[i]])

        backTrack(0, candidates, target, tmplist)
        return res

if __name__ == '__main__':
    candidates = [2,7,6,3,5,1]
    target = 9
    s = Solution()
    print(s.combinationSum(candidates, target))