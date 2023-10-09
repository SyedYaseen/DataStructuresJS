# # Input:
# board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
#                                                                                                                                                                                                       ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

board = [[".", ".", "9", "7", "4", "8", ".", ".", "."], ["7", ".", ".", ".", ".", ".", ".", ".", "."], [".", "2", ".", "1", ".", "9", ".", ".", "."], [".", ".", "7", ".", ".", ".", "2", "4", "."], [".", "6", "4", ".",
                                                                                                                                                                                                      "1", ".", "5", "9", "."], [".", "9", "8", ".", ".", ".", "3", ".", "."], [".", ".", ".", "8", ".", "3", ".", "2", "."], [".", ".", ".", ".", ".", ".", ".", ".", "6"], [".", ".", ".", "2", "7", "5", "9", ".", "."]]

# board = [[".", ".", "9", "7", "4", "8", ".", ".", "."],
#          ["7", ".", ".", ".", ".", ".", ".", ".", "."],
#          [".", "2", ".", "1", ".", "9", ".", ".", "."],
#          [".", ".", "7", ".", ".", ".", "2", "4", "."],
#          [".", "6", "4", ".", "1", ".", "5", "9", "."],
#          [".", "9", "8", ".", ".", ".", "3", ".", "."],
#          [".", ".", ".", "8", ".", "3", ".", "2", "."],
#          [".", ".", ".", ".", ".", ".", ".", ".", "6"],
#          [".", ".", ".", "2", "7", "5", "9", ".", "."]]


# board = [[".", ".", "9", "7", "4", "8", ".", ".", "."],
#          ["7", ".", ".", ".", ".", ".", ".", ".", "."],
#          [".", "2", ".", "1", ".", "9", ".", ".", "."],
#          [".", ".", "7", ".", ".", ".", "2", "4", "."],
#          [".", "6", "4", ".", "1", ".", "5", "9", "."],
#          [".", "9", "8", ".", ".", ".", "3", ".", "."],
#          [".", ".", ".", "8", ".", "3", ".", "2", "."],
#          [".", ".", ".", ".", ".", ".", ".", ".", "6"],
#          [".", ".", ".", "2", "7", "5", "9", ".", "."]]


# [["5","3",".", ".","7",".", ".",".","."]
# ,["6",".",".", "1","9","5", ".",".","."]
# ,[".","9","8", ".",".",".", ".","6","."]

# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]


# correctAns = [["5", "3", "4", "6", "7", "8", "9", "1", "2"],
#               ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
#               ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
#               ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
#               ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
#               ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
#               ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
#               ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
#               ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]


class Solution(object):

    def func(self, board):
        possible = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

        emptyVal = {}

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    emptyVal.setdefault(f'{i}{j}', possible.copy())

        startKeyList = list(emptyVal.keys())
        initLen = 99
        endKeyListLength = 0

        # Process of elimination
        while bool(startKeyList) and initLen != endKeyListLength:
            initLen = len(startKeyList)
            for key in startKeyList:
                row = int(key[0])
                col = int(key[1])

                for i in range(9):
                    if board[i][col] != '.':
                        emptyVal[f'{row}{col}'].discard(board[i][col])

                    if board[row][i] != '.':
                        emptyVal[f'{row}{col}'].discard(board[row][i])

                if len(emptyVal[f'{row}{col}']) == 1:
                    board[row][col] = emptyVal[f'{row}{col}'].pop()
                    del emptyVal[f'{row}{col}']
                    startKeyList.remove(f'{row}{col}')
                    continue

                # find which grid key belongs to
                x = (row//3) * 3
                y = (col//3) * 3

                for i in range(x, x + 3, 1):
                    for j in range(y, y + 3, 1):
                        if board[i][j] != '.':
                            emptyVal[f'{row}{col}'].discard(board[i][j])

                if len(emptyVal[f'{row}{col}']) == 1:
                    board[row][col] = emptyVal[f'{row}{col}'].pop()
                    del emptyVal[f'{row}{col}']
                    startKeyList.remove(f'{row}{col}')

            endKeyListLength = len(startKeyList)

        row_group = {}
        col_group = {}
        sub_group = {}

        subtract_from_row = {}
        subtract_from_col = {}
        
        min_candidates = 2
        for key in startKeyList:
            print()
            print(key, emptyVal[key])
            if len(emptyVal[key]) == min_candidates:
                if key[0] not in row_group:
                    row_group[key[0]] = []
                    row_group[key[0]].append(emptyVal[key])
                else:
                    if emptyVal[key] in row_group[key[0]]:
                        print("This is true", emptyVal[key])
                    row_group[key[0]].append(emptyVal[key])

                if key[1] not in col_group:
                    col_group[key[1]] = []
                    col_group[key[1]].append(emptyVal[key])
                else:
                    if emptyVal[key] in col_group[key[1]]:
                        print("This is true", emptyVal[key])
                    col_group[key[1]].append(emptyVal[key])

            # row_group[key[0]] = emptyVal[key]

            # if len(emptyVal[key]) == 2:
            #     row = int(key[0])
            #     col = int(key[1])

            # for i in startKeyList:
            #     print("Starts with", i[0])
            #     print("ends with", i[1])
            # if i[0] == row:
            #     row_group[i[0]] = startKeyList[i]

            # print(key, emptyVal[key])
        print(row_group)
        # for i in row_group:
        #     print(i)
        # print()
        # for i in col_group:
        #     print(i)
        print(col_group)
        # print(emptyVal)

        # for key in emptyVal:
        #     print(key, emptyVal[key])
        # for i in board:
        #     print(i)

        return board

    def func2(self, board):
        possible = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

        emptyVal = {}

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    emptyVal.setdefault(f'{i}{j}', possible.copy())

        startKeyList = list(emptyVal.keys())
        initLen = 99
        endKeyListLength = 0

        # Process of elimination
        while bool(startKeyList) and initLen != endKeyListLength:
            initLen = len(startKeyList)
            for key in startKeyList:
                row = int(key[0])
                col = int(key[1])

                for i in range(9):
                    if board[i][col] != '.':
                        emptyVal[f'{row}{col}'].discard(board[i][col])

                    if board[row][i] != '.':
                        emptyVal[f'{row}{col}'].discard(board[row][i])

                if len(emptyVal[f'{row}{col}']) == 1:
                    board[row][col] = emptyVal[f'{row}{col}'].pop()
                    del emptyVal[f'{row}{col}']
                    startKeyList.remove(f'{row}{col}')
                    continue

                # find which grid key belongs to
                x = (row//3) * 3
                y = (col//3) * 3

                for i in range(x, x + 3, 1):
                    for j in range(y, y + 3, 1):
                        if board[i][j] != '.':
                            emptyVal[f'{row}{col}'].discard(board[i][j])

                if len(emptyVal[f'{row}{col}']) == 1:
                    board[row][col] = emptyVal[f'{row}{col}'].pop()
                    del emptyVal[f'{row}{col}']
                    startKeyList.remove(f'{row}{col}')

            endKeyListLength = len(startKeyList)

        for key in emptyVal:
            print(key, emptyVal[key])
        for i in board:
            print(i)

        return board


sln = Solution()
myAns = sln.func(board)
# print(myAns)
# print(correctAns == myAns)

# possible = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# a = {'12': possible.copy(), '13': possible.copy()}
# print(a['12'].pop())
# print(a['12'])
# print(a['13'])

# a = {'1', '3'}
# b = {'3', '1'}
# print(len(a))
