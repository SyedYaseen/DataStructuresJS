# square_values = []
# for _ in range(9):
#     square_values.append(set())
# square_values = [set()] * 9
# print(square_values)
# map = [[], []]

# if len(map[0]) != 0:
#     print("Here")

# candidate = [{'1', '2', '3'}]
# if {'1', '2', '3'} not in candidate:
#     print("here")

# a = b = c = None
# a = 2
# print(a)
# print(b)
# def test():
#     for row in range(9):
#         print(row)
#         for col in range(9):
#             if col == 3:
#                 print(col)
#                 return


# test()
# c = None


# def a():
#     c = 4
board = [["5", "3", "4", "6", "7", "8", "9", "1", "2"],
         ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
         ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
         ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
         ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
         ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
         ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
         ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
         ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]

# board = [['7', '8', '9', '3', '8', '1', '7', '5', '2'],
#          ['7', '8', '3', '9', '2', '9', '9', '1', '4'],
#          ['4', '4', '1', '5', '4', '9', '9', '6', '8'],
#          ['1', '7', '2', '4', '3', '5', '8', '9', '6'],
#          ['3', '6', '5', '8', '9', '2', '1', '4', '7'],
#          ['8', '9', '4', '1', '6', '7', '2', '3', '5'],
#          ['5', '1', '7', '9', '5', '8', '6', '2', '9'],
#          ['9', '3', '8', '3', '4', '6', '5', '7', '3'],
#          ['2', '5', '6', '7', '5', '9', '4', '8', '9']]


# class Soln():

#     isValid = False

#     def boardIsValid(self, board):
#         for row in range(9):
#             unique = set()
#             for col in range(9):
#                 if board[row][col] == '.' or type(board[row][col]) == set:

#                     return False
#                 elif type(board[row][col]) != set:
#                     if board[row][col] not in unique:
#                         unique.add(board[row][col])
#                     else:
#                         print("Here")
#                         return False
#         self.isValid = True
#         return True


# sln = Soln()

# print("func", sln.boardIsValid(board))
# print("IsValid", sln.isValid)
print(bool({}))
