# # Input:
# board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
#                                                                                                                                                                                                       ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

# board = [[".", ".", "9", "7", "4", "8", ".", ".", "."], ["7", ".", ".", ".", ".", ".", ".", ".", "."], [".", "2", ".", "1", ".", "9", ".", ".", "."], [".", ".", "7", ".", ".", ".", "2", "4", "."], [".", "6", "4", ".",
#                                                                                                                                                                                                       "1", ".", "5", "9", "."], [".", "9", "8", ".", ".", ".", "3", ".", "."], [".", ".", ".", "8", ".", "3", ".", "2", "."], [".", ".", ".", ".", ".", ".", ".", ".", "6"], [".", ".", ".", "2", "7", "5", "9", ".", "."]]

board = [[".", ".", ".", ".", ".", "1", ".", ".", "2"],
         [".", ".", "3", ".", ".", ".", ".", ".", "4"],
         [".", ".", ".", "5", ".", ".", ".", "6", "."],
         [".", "7", ".", ".", "3", ".", "8", ".", "."],
         ["3", ".", "5", ".", "9", ".", "1", ".", "7"],
         [".", ".", "4", ".", "6", ".", ".", "3", "."],
         [".", "1", ".", ".", ".", "8", ".", ".", "."],
         ["9", ".", ".", ".", ".", ".", "5", ".", "."],
         ["2", ".", ".", "7", ".", ".", ".", ".", "."]]
# Correct with triples removed by row and column
# ['.', '.', '9', '.', '.', '1', '.', '5', '2']
# ['.', '.', '3', '.', '.', '.', '.', '1', '4']
# ['.', '.', '1', '5', '.', '.', '.', '6', '8']
# ['1', '7', '2', '4', '3', '5', '8', '9', '6']
# ['3', '6', '5', '8', '9', '2', '1', '4', '7']
# ['8', '9', '4', '1', '6', '7', '2', '3', '5']
# ['.', '1', '7', '.', '.', '8', '6', '2', '.']
# ['9', '.', '8', '.', '.', '.', '5', '7', '.']
# ['2', '.', '6', '7', '.', '.', '4', '8', '.']

# Incorrect with triples
# ['4', '8', '9', '6', '7', '1', '3', '5', '2'],
# ['6', '5', '3', '.', '8', '.', '9', '1', '4'],
# ['7', '.', '2', '5', '8', '3', '.', '6', '1'],
# ['1', '7', '.', '4', '3', '5', '8', '9', '6'],
# ['3', '6', '5', '8', '9', '2', '1', '4', '7'],
# ['8', '9', '4', '1', '6', '7', '2', '3', '5'],
# ['5', '1', '6', '3', '2', '8', '4', '.', '9'],
# ['9', '4', '8', '2', '1', '6', '5', '7', '3'],
# ['2', '3', '1', '7', '5', '9', '6', '8', '.']]

# board = [['.', '.', '9', '.', '.', '1', '.', '5', '2'],
#          ['.', '.', '3', '.', '.', '.', '.', '1', '4'],
#          ['.', '.', '1', '5', '.', '.', '.', '6', '8'],
#          ['1', '7', '2', '4', '3', '5', '8', '9', '6'],
#          ['3', '6', '5', '8', '9', '2', '1', '4', '7'],
#          ['8', '9', '4', '1', '6', '7', '2', '3', '5'],
#          ['.', '1', '7', '.', '.', '8', '6', '2', '.'],
#          ['9', '.', '8', '.', '.', '.', '5', '7', '.'],
#          ['2', '.', '6', '7', '.', '.', '4', '8', '.']]

# board = [[".", ".", "9", "7", "4", "8", ".", ".", "."],
#          ["7", ".", ".", ".", ".", ".", ".", ".", "."],
#          [".", "2", ".", "1", ".", "9", ".", ".", "."],
#          [".", ".", "7", ".", ".", ".", "2", "4", "."],
#          [".", "6", "4", ".", "1", ".", "5", "9", "."],
#          [".", "9", "8", ".", ".", ".", "3", ".", "."],
#          [".", ".", ".", "8", ".", "3", ".", "2", "."],
#          [".", ".", ".", ".", ".", ".", ".", ".", "6"],
#          [".", ".", ".", "2", "7", "5", "9", ".", "."]]

# after triples elim
# board = [['4', '8', '9', '6', '7', '1', '3', '5', '2'],
#          ['6', '5', '3', '.', '8', '.', '9', '1', '4'],
#          ['7', '.', '2', '5', '8', '3', '.', '6', '1'],
#          ['1', '7', '.', '4', '3', '5', '8', '9', '6'],
#          ['3', '6', '5', '8', '9', '2', '1', '4', '7'],
#          ['8', '9', '4', '1', '6', '7', '2', '3', '5'],
#          ['5', '1', '6', '3', '2', '8', '4', '.', '9'],
#          ['9', '4', '8', '2', '1', '6', '5', '7', '3'],
#          ['2', '.', '.', '7', '5', '9', '6', '8', '.']]

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
    '''Finds triples on the emptyVal dict group by row, column or square
    and returns a list of triples on that group'''

    def func(self, board):
        def getSquare(rowInt, colInt):
            if 0 <= rowInt <= 2 and 0 <= colInt <= 2:
                return '0'
            elif 0 <= rowInt <= 2 and 3 <= colInt <= 5:
                return '1'
            elif 0 <= rowInt <= 2 and 6 <= colInt <= 8:
                return '2'
            elif 3 <= rowInt <= 5 and 0 <= colInt <= 2:
                return '3'
            elif 3 <= rowInt <= 5 and 3 <= colInt <= 5:
                return '4'
            elif 3 <= rowInt <= 5 and 6 <= colInt <= 8:
                return '5'
            elif 6 <= rowInt <= 8 and 0 <= colInt <= 2:
                return '6'
            elif 6 <= rowInt <= 8 and 3 <= colInt <= 5:
                return '7'
            elif 6 <= rowInt <= 8 and 6 <= colInt <= 8:
                return '8'

        def findTriples(lis_group):
            only_three = []
            only_two = []
            triples = []

            for i in lis_group:
                if len(i) == 3:
                    only_three.append(i)
                if len(i) == 2:
                    only_two.append(i)

            temp = []
            for i in only_three:
                if i in temp:
                    temp.append(i)
                else:
                    temp = [i]

                for two in only_two:
                    if two.issubset(i):
                        temp.append(two)
                if len(temp) >= 3:
                    triples.append(temp[0])

            # cleanup list group
            # for triple in triples:
            #     for i in range(len(lis_group)):
            #         if not lis_group[i].issubset(triple):
            #             lis_group[i] = lis_group[i] - triple

            return triples

        def eliminateByTriples(group_no, key, group, triples):
            if group_no in group and len(group[group_no]) > 3:
                if group_no not in triples:
                    triple = findTriples(group[group_no])
                if len(triple) == 0:
                    triples[group_no] = None
                else:
                    triples[group_no] = triple

                    for tri in triples[group_no]:
                        if not emptyVal[key].issubset(tri):
                            emptyVal[key] = emptyVal[key] - tri

        possible = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

        emptyVal = {}

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    emptyVal.setdefault(f'{i}{j}', possible.copy())

        startKeyList = list(emptyVal.keys())
        outerInitLen = 0
        outerLoopLen = 99

        endKeyListLength = 0
        while bool(startKeyList) and outerInitLen != outerLoopLen:
            outerInitLen = len(startKeyList)
            # Process of elimination
            initLen = 99
            endKeyListLength = 0

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
            '''
            # Get unique - only looks at rows
            initLen = 99
            endKeyListLength = 0

            while bool(startKeyList) and initLen != endKeyListLength:
                initLen = len(startKeyList)
                row_count = {}

                for i in startKeyList:
                    row_no = i[0]

                    if row_no not in row_count:
                        row_count[row_no] = {}

                    for candidate in emptyVal[i]:
                        if candidate not in row_count[row_no]:
                            row_count[row_no][candidate] = 1
                        else:
                            row_count[row_no][candidate] = row_count[row_no][candidate] + 1

                for row_no in row_count:
                    for candi in row_count[row_no]:
                        if row_count[row_no][candi] == 1:
                            # print(row_no, candi)
                            for i in startKeyList:
                                if i[0] == row_no:
                                    if candi in emptyVal[i]:
                                        board[int(i[0])][int(i[1])] = candi
                                        del emptyVal[i]
                                        startKeyList.remove(i)

                        # if row_count[row_no][candi] == 2:
                        #     print(row_no, candi, row_count[row_no])

                endKeyListLength = len(startKeyList)
            '''
            # Eliminate by triples
            row_group = {}
            col_group = {}
            square_group = {}

            for key in startKeyList:
                if key[0] not in row_group:
                    row_group[key[0]] = []
                row_group[key[0]].append(emptyVal[key])

                if key[1] not in col_group:
                    col_group[key[1]] = []
                col_group[key[1]].append(emptyVal[key])
                rowInt = int(key[0])
                colInt = int(key[1])

                # get square value and put into sqaure group
                squareNo = getSquare(rowInt, colInt)
                square_group.setdefault(squareNo, []).append(emptyVal[key])

            for key in startKeyList:
                row = key[0]
                col = key[1]

                eliminateByTriples(row, key, row_group, {})
                eliminateByTriples(col, key, col_group, {})
                eliminateByTriples(
                    getSquare(int(row), int(col)), key, col_group, {})

            outerLoopLen = len(startKeyList)
        # for i in square_group:
        #     print(i, square_group[i])

        # Test
        for i in emptyVal:
            print(i, emptyVal[i])

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
for i in myAns:
    print(i)


# print(correctAns == myAns)

# Find triples


def findTriples(lis_group):
    only_three = []
    only_two = []
    triples = []

    for i in lis_group:
        if len(i) == 3:
            only_three.append(i)
        if len(i) == 2:
            only_two.append(i)

    temp = []
    for i in only_three:
        if i in temp:
            temp.append(i)
        else:
            temp = [i]

        for two in only_two:
            if two.issubset(i):
                temp.append(two)
        if len(temp) >= 3:
            triples.append(temp[0])

    # for triple in triples:
    #     for i in range(len(lis_group)):
    #         if not lis_group[i].issubset(triple):
    #             lis_group[i] = lis_group[i] - triple
    # print(lis_group)

    return triples


a = [{'7', '3', '9'},
     {'2', '9'},
     {'7', '9'},
     {'3', '7', '9'},
     {'2', '3', '4', '6', '7', '9'},
     {'3', '4', '6', '9'}]

b = [{'2', '3', '6'},
     {'1', '2', '4'},
     {'4', '3', '6'},
     {'1', '3'},
     {'4', '3'}]

c = [{'7', '3', '9'},
     {'7', '9'},
     {'3', '7'},
     {'2', '9'},
     {'2', '3', '4', '6', '7', '9'},
     {'3', '4', '6', '9'}]

c = [{'7', '3', '9'},
     {'7', '9'},
     {'3', '7'},
     {'1', '2'},
     {'2', '3'},
     {'1', '2', '3'}]


# print(findTriples(a))

# Subtract code

# else:
#     if emptyVal[key] in row_group[key[0]]:
#         subtract_from_row[key[0]] = []
#         subtract_from_row[key[0]].append(emptyVal[key])

#     if len(emptyVal[key]) == 2:
#         row_group[key[0]].append(emptyVal[key])

# for key in subtract_from_row:

#     print("THis", key, subtract_from_row[key])

# if key[1] not in col_group:
#     col_group[key[1]] = []
#     col_group[key[1]].append(emptyVal[key])
# else:
#     if emptyVal[key] in col_group[key[1]]:
#         print("This is true", emptyVal[key])
#     col_group[key[1]].append(emptyVal[key])

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
# print("Sub from row", subtract_from_row)
# for i in row_group:
#     print(i)
# print()
# for i in col_group:
#     print(i)
# print(col_group)
# print(emptyVal)

# for key in emptyVal:
#     print(key, emptyVal[key])
# for i in board:
#     print(i)
# rowInt = 0
# colInt = 3
# match rowInt, colInt:
#     case num if 0 <= rowInt <= 2 and 0 <= colInt <= 2:
#         print('0')
#     case num if 0 <= rowInt <= 2 and 3 <= colInt <= 5:
#         print('1', num)
