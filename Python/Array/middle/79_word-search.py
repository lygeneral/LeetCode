'''
79. 单词搜索

给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。



示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false



提示：

    board 和 word 中只包含大写和小写英文字母。
    1 <= board.length <= 200
    1 <= board[i].length <= 200
    1 <= word.length <= 10^3


'''

class Solution:
    def exist(self, board, word):
        visisted = [[0 for i in range(len(board[0]))] for i in range(len(board))]
        def backTrack(i, j , cur, board, word, visisted):
            '''
            @describe: 遍历寻找第一个字符，并开始回溯迭代
            @param i: 指针
            @param j: 指针
            @param cur: 字符串指针
            @param board: 矩阵
            @param word: 字符串
            @param visisted: 是否访问过标志矩阵
            @return:
            '''
            if cur == len(word):
                return True
            if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or visisted[i][j] == 1 or board[i][j] != word[cur]:
                return False
            cur += 1
            visisted[i][j] = 1
            flg = backTrack(i - 1, j, cur, board, word, visisted)  or backTrack(i, j - 1, cur, board, word, visisted) or backTrack(i + 1, j, cur, board, word, visisted) or backTrack(i, j + 1, cur, board, word, visisted)
            visisted[i][j] = 0
            return flg
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backTrack(i, j , 0, board, word, visisted):
                    return True
        return False

if __name__ == '__main__':
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    s = Solution()
    print(s.exist(board, word))