class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        cols = [0]*n
        rows = [0]*n
        boxes = [0]*n

        for i in range(n):
            for j in range(n):
                num = board[i][j]
                if num == '.':
                    continue
                mask = 1 << (int(num)-1)
                box = 3*(i//3)+(j//3)
                if (rows[i] & mask) or (cols[j] & mask) or (boxes[box] & mask):
                    return False
                rows[i] |= mask
                cols[j] |= mask
                boxes[box] |= mask    
        return True