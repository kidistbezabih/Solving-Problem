class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ln = len(board)
        for i in range(ln):
            colLis = []
            for j in range(ln):
                colLis.append(board[j][i])
            intCount = 0
            for i in colLis:
                if (i.isnumeric()):
                  intCount += 1
            if(len(set(colLis)) - 1 != intCount ):
              return False

        for i in range(ln):
          countRow = 0
          for j in range(ln):
            if( board[i][j].isnumeric()):
              countRow += 1
          if(len(set(board[i])) -1 != countRow):
            return False
        
        blocks = []
        for i in range(0, 9, 3):
          for j in range(0, 9, 3):
            blocks.append(board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3])
        for i in range(9):
          count = 0
          for j in range(9):
            if( blocks[i][j].isnumeric()):
              count += 1
              print(blocks[i][j])
          if (count != len(set(blocks[i])) - 1):
            return False
        return True
            
        

