class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board:
            return False

        rows = []

        #bug with columns = [[]]*9 discovered early
        #[[]]*9 returns 9 references to the same array, better to fill it with a for loop
        #later in code .append() is used, which mutates the list itself, appending to all columns
        columns = [[] for _ in range(9)]
        squares = [[] for _ in range(9)]

        square_index = 0
        square_index_offset = 0

        for i in range(9):
            row = board[i]
            rows.append(row)
            for x in range(9):
                columns[x].append(row[x])
                squares[square_index+square_index_offset].append(row[x])
                if (x + 1) % 3 == 0:
                    square_index = (square_index+1) % 3
            if (i+1) % 3 == 0:
                square_index_offset+=3

        # for unit in rows + columns + squares:
        #     if not self.hasDuplicate(unit):
        #         res = True
        
        return not any(self.hasDuplicate(unit) for unit in rows + columns + squares)

    def hasDuplicate(self, nums: List[str]) -> bool:
            hasDuplicate = False    
            seen = set()
            duplicate_set = set()
            for num in nums:
                if num == '.':
                    pass
                elif num in seen:
                    duplicate_set.add(num)
                else:
                    seen.add(num)
            if len(duplicate_set) > 0:
                hasDuplicate = True
            return hasDuplicate


# board = [["1","2",".",".","3",".",".",".","."],
#          ["4",".",".","5",".",".",".",".","."],
#          [".","9","1",".",".",".",".",".","3"],
#          ["5",".",".",".","6",".",".",".","4"],
#          [".",".",".","8",".","3",".",".","5"],
#          ["7",".",".",".","2",".",".",".","6"],
#          [".",".",".",".",".",".","2",".","."],
#          [".",".",".","4","1","9",".",".","8"],
#          [".",".",".",".","8",".",".","7","9"]]


# board = [["1","2",".",".","3",".",".",".","."],
#         ["4",".",".","5",".",".",".",".","."],
#         [".","9","8",".",".",".",".",".","3"],
#         ["5",".",".",".","6",".",".",".","4"],
#         [".",".",".","8",".","3",".",".","5"],
#         ["7",".",".",".","2",".",".",".","6"],
#         [".",".",".",".",".",".","2",".","."],
#         [".",".",".","4","1","9",".",".","8"],
#         [".",".",".",".","8",".",".","7","9"]]

# sol = Solution()
# res = sol.isValidSudoku(board)
# print(res)