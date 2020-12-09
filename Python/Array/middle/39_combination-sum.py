'''
39. 组合总和

给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

    所有数字（包括 target）都是正整数。
    解集不能包含重复的组合。

示例 1：

输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]

示例 2：

输入：candidates = [2,3,5], target = 8,
所求解集为：
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]



提示：

    1 <= candidates.length <= 30
    1 <= candidates[i] <= 200
    candidate 中的每个元素都是独一无二的。
    1 <= target <= 500


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
        def backTrack(start, candidates, target, tmplist):
            # 满足该条件返回，找到目标组合
            if target == 0:
                res.append(tmplist)
                return
            # target<0时说明该组合失败，直接返回
            elif target < 0:
                return
            # 遍历迭代，将每一种可能都进行迭代
            for i in range(start, len(candidates)):
                backTrack(i, candidates, target - candidates[i], tmplist + [candidates[i]])

        backTrack(0, candidates, target, tmplist)
        return res

# 较Solution3增加index
class Solution2:
    def combinationSum(self, candidates, target):
        '''
        @describe: 回溯法，迭代中写明返回条件，并在迭代过程中将组合写入res
        @param candidates: 数组
        @param target: 目标值
        @return: 组合
        '''
        res =[]
        tmplist = []
        def backTrack(start, candidates, target, tmplist):
            # 满足该条件返回
            if target == 0:
                res.append(tmplist)
                return
            # 遍历迭代，将每一种可能都进行迭代
            for i in range(start, len(candidates)):
                # 说明该情况不满足条件则跳过这种情况继续下一个元素，即i+=1
                if target - candidates[i] < 0:
                    continue
                backTrack(i, candidates, target - candidates[i], tmplist + [candidates[i]])

        backTrack(0, candidates, target, tmplist)
        return res

class Solution2:
    def combinationSum(self, candidates, target):
        '''
        @describe: 回溯法，迭代中写明返回条件，并在迭代过程中将组合写入res
        @param candidates: 数组
        @param target: 目标值
        @return: 组合
        '''
        res =[]
        tmplist = []
        def backTrack(candidates, target, tmplist):
            # 满足该条件返回
            if target == 0:
                res.append(tmplist)
                return
            # 遍历迭代，将每一种可能都进行迭代
            for i in range(len(candidates)):
                # 说明该情况不满足条件则跳过这种情况继续下一个元素，即i+=1
                if target - candidates[i] < 0:
                    continue
                backTrack(candidates, target - candidates[i], tmplist + [candidates[i]])

        backTrack(candidates, target, tmplist)
        return res

if __name__ == '__main__':
    candidates = [2,7,6,3,5,1]
    target = 9
    s = Solution()
    print(s.combinationSum(candidates, target))
