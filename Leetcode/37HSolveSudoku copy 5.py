# # Input:
# board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
#                                                                                                                                                                                                       ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

# board = [[".", ".", "9", "7", "4", "8", ".", ".", "."],
#          ["7", ".", ".", ".", ".", ".", ".", ".", "."],
#          [".", "2", ".", "1", ".", "9", ".", ".", "."],
#          [".", ".", "7", ".", ".", ".", "2", "4", "."],
#          [".", "6", "4", ".", "1", ".", "5", "9", "."],
#          [".", "9", "8", ".", ".", ".", "3", ".", "."],
#          [".", ".", ".", "8", ".", "3", ".", "2", "."],
#          [".", ".", ".", ".", ".", ".", ".", ".", "6"],
#          [".", ".", ".", "2", "7", "5", "9", ".", "."]]

board = [[".", ".", ".", ".", ".", "1", ".", ".", "2"],
         [".", ".", "3", ".", ".", ".", ".", ".", "4"],
         [".", ".", ".", "5", ".", ".", ".", "6", "."],
         [".", "7", ".", ".", "3", ".", "8", ".", "."],
         ["3", ".", "5", ".", "9", ".", "1", ".", "7"],
         [".", ".", "4", ".", "6", ".", ".", "3", "."],
         [".", "1", ".", ".", ".", "8", ".", ".", "."],
         ["9", ".", ".", ".", ".", ".", "5", ".", "."],
         ["2", ".", ".", "7", ".", ".", ".", ".", "."]]

# board = [['.', '.', '9', '.', '.', '1', '.', '5', '2'],
#          ['.', '.', '3', '.', '.', '.', '.', '1', '4'],
#          ['.', '.', '1', '5', '.', '.', '.', '6', '8'],
#          ['1', '7', '2', '4', '3', '5', '8', '9', '6'],
#          ['3', '6', '5', '8', '9', '2', '1', '4', '7'],
#          ['8', '9', '4', '1', '6', '7', '2', '3', '5'],
#          ['.', '1', '7', '.', '.', '8', '6', '2', '.'],
#          ['9', '.', '8', '.', '.', '.', '5', '7', '.'],
#          ['2', '.', '6', '7', '.', '.', '4', '8', '.']]
# Answer
# ['6', '4', '9', '3', '8', '1', '7', '5', '2']
# ['5', '8', '3', '2', '7', '6', '9', '1', '4']
# ['7', '2', '1', '5', '4', '9', '3', '6', '8']
# ['1', '7', '2', '4', '3', '5', '8', '9', '6']
# ['3', '6', '5', '8', '9', '2', '1', '4', '7']
# ['8', '9', '4', '1', '6', '7', '2', '3', '5']
# ['4', '1', '7', '9', '5', '8', '6', '2', '3']
# ['9', '3', '8', '6', '2', '4', '5', '7', '1']
# ['2', '5', '6', '7', '1', '3', '4', '8', '9']

# ['.', '.', '9', '7', '4', '8', '.', '.', '.']
# ['7', '.', '.', '6', '.', '2', '.', '.', '.']
# ['.', '2', '.', '1', '.', '9', '.', '.', '.']
# ['.', '.', '7', '9', '8', '6', '2', '4', '1']
# ['2', '6', '4', '3', '1', '7', '5', '9', '8']
# ['1', '9', '8', '5', '2', '4', '3', '6', '7']
# ['.', '.', '.', '8', '6', '3', '.', '2', '.']
# ['.', '.', '.', '4', '9', '1', '.', '.', '6']
# ['.', '.', '.', '2', '7', '5', '9', '.', '.']

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

    # masterEmptyVal = None

    def func(self, board):
        possible = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
        emptyVal = {}

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

        def mapTriples(num, group, map):
            if num not in map:
                triples = findTriples(group)
                if len(triples) > 0:
                    map[num] = triples
                else:
                    map[num] = None

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
            return triples

        def eliminateByTriples(key, group, triples, emptyVal):
            if len(group) > 3:
                for tri in triples:
                    if not emptyVal[key].issubset(tri):
                        newCandidates = emptyVal[key] - tri
                        if newCandidates != emptyVal[key]:
                            group.remove(emptyVal[key])
                            emptyVal[key] = newCandidates
                            group.append(newCandidates)

        def eliminationByRowColumnSquare():
            square_values = [set() for _ in range(9)]
            for row in range(9):
                row_values = set()
                col_values = set()

                for col in range(9):
                    if board[row][col] != '.':
                        row_values.add(board[row][col])
                        square_values[int(getSquare(row, col))].add(
                            board[row][col])
                    if board[col][row] != '.':
                        col_values.add(board[col][row])
                        square_values[int(getSquare(col, row))].add(
                            board[col][row])
                # print(square_values)

                # Eliminate values by row and columns and squares

                for col in range(9):
                    key = f'{row}{col}'
                    square_no = int(getSquare(row, col))
                    if board[row][col] == '.':
                        if key in emptyVal:
                            emptyVal[key] = emptyVal[key] - \
                                row_values - square_values[square_no]
                        else:
                            emptyVal.setdefault(
                                key, possible - row_values - square_values[square_no])

                    key = f'{col}{row}'
                    square_no = int(getSquare(col, row))
                    if board[col][row] == '.':
                        if key in emptyVal:
                            emptyVal[key] = emptyVal[f'{col}{row}'] - \
                                col_values - square_values[square_no]
                        else:
                            emptyVal.setdefault(
                                key, possible - col_values - square_values[square_no])

        def AssignIfUnique():
            startKeyList = list(emptyVal.keys())

            # Get unique - only looks at rows
            # square_values = [set() for _ in range(9)]

            row_count = [{'1': 0, '2': 0, '3': 0, '4': 0, '5': 0,
                          '6': 0, '7': 0, '8': 0, '9': 0} for _ in range(9)]
            col_count = [{'1': 0, '2': 0, '3': 0, '4': 0, '5': 0,
                          '6': 0, '7': 0, '8': 0, '9': 0} for _ in range(9)]
            sqr_count = [{'1': 0, '2': 0, '3': 0, '4': 0, '5': 0,
                          '6': 0, '7': 0, '8': 0, '9': 0} for _ in range(9)]

            for key in startKeyList:
                row = int(key[0])
                col = int(key[1])
                squareNo = int(getSquare(int(row), int(col)))

                for candidate in emptyVal[key]:
                    row_count[row][candidate] += 1
                    col_count[col][candidate] += 1
                    sqr_count[squareNo][candidate] += 1

            print("Row counts")
            for i in range(9):
                pickedRow = row_count[i]
                pickedCol = col_count[i]
                pickedSqr = sqr_count[i]

                for i in range(1, 10, 1):
                    if pickedRow[str(i)] == 1:
                        for col in range(9):
                            if f"{i}{col}" in emptyVal and str(i) in emptyVal[f"{i}{col}"]:
                                board[int(i)][int(col)] = str(i)
                                del emptyVal[f"{i}{col}"]
                                startKeyList.remove(f"{i}{col}")

            # Definitely refactor needed - below looks digusting!
            # for row in row_count:
            #     for candi in row_count[row]:
            #         if row_count[row][candi] == 1:
            #             # print(row_no, candi)
            #             for i in startKeyList:
            #                 if i[0] == row:
            #                     if candi in emptyVal[i]:
            #                         board[int(i[0])][int(i[1])] = candi
            #                         del emptyVal[i]
            #                         startKeyList.remove(i)
            # for col in col_count:
            #     for candi in col_count[col]:
            #         if col_count[col][candi] == 1:
            #             # print(row_no, candi)
            #             for i in startKeyList:
            #                 if i[0] == col:
            #                     if candi in emptyVal[i]:
            #                         board[int(i[0])][int(i[1])] = candi
            #                         del emptyVal[i]
            #                         startKeyList.remove(i)

            # if row_count[row_no][candi] == 2:
            #     print(row_no, candi, row_count[row_no])

        def EliminateByTriples():
            startKeyList = list(emptyVal)
            row_group = {}
            col_group = {}
            square_group = {}

            for key in startKeyList:
                row_group.setdefault(key[0], []).append(emptyVal[key])
                col_group.setdefault(key[1], []).append(emptyVal[key])

                squareNo = getSquare(int(key[0]), int(key[1]))
                square_group.setdefault(squareNo, []).append(emptyVal[key])

            triplesRow = {}
            triplesCol = {}
            triplesSquare = {}

            for key in startKeyList:
                row = key[0]
                col = key[1]
                squareNo = getSquare(int(row), int(col))
                mapTriples(row, row_group[row], triplesRow)
                mapTriples(col, col_group[col], triplesCol)
                mapTriples(squareNo, square_group[squareNo], triplesSquare)

                if triplesRow[row] is not None:
                    eliminateByTriples(
                        key, row_group[row], triplesRow[row], emptyVal)
                if triplesCol[col] is not None:
                    eliminateByTriples(
                        key, col_group[col], triplesCol[col], emptyVal)
                if triplesSquare[squareNo] is not None:
                    eliminateByTriples(
                        key, square_group[squareNo], triplesSquare[squareNo], emptyVal)

                if len(emptyVal[key]) == 1:
                    board[int(row)][int(col)] = emptyVal[key].pop()
                    del emptyVal[key]
                    startKeyList.remove(key)

        def isBoardValid():
            for row in board:
                if set(row) != possible:
                    return False
            return True

        def printboard():
            for i in board:
                print(i)

        def printEmpty():
            for i in emptyVal:
                print(i, emptyVal[i])

        def AssignToBoard():
            for key in list(emptyVal):
                if len(emptyVal[key]) == 1:
                    board[int(key[0])][int(key[1])] = emptyVal[key].pop()
                    del emptyVal[key]

            print(board)

        def RunElimination():
            EmptyItemsBefore = 0
            EmptyItemsAfter = 99
            timesRun = 0
            while EmptyItemsBefore != EmptyItemsAfter and EmptyItemsAfter > 0:
                EmptyItemsBefore = len(list(emptyVal))
                eliminationByRowColumnSquare()
                EliminateByTriples()
                # AssignIfUnique() # Not working
                AssignToBoard()
                EmptyItemsAfter = len(emptyVal)
                timesRun += 1
            print("timesRun", timesRun)
            return board

        # def pickValue():
        #     for key in emptyVal:
        #         for candidate in emptyVal[key]:
            # print(candidate)

        def start():
            RunElimination()
            # printEmpty()
            # printboard()

            if not isBoardValid():
                originalBoard = board.copy()

                # pickValue()

                RunElimination()
        start()
        # printboard()
        # printEmpty()

    def start(self, board, emptyVal):
        self.func()


sln = Solution()
board = sln.func(board)
