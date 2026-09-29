class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        board_m = len(board)
        board_n = len(board[0])
        top_check = "O" in board[0]
        bottom_check = "O" in board[-1]
        if top_check == True or bottom_check == True:
            for i in range(len(board[0])):
                if board[0][i] == "O":
                    #board[0][i] == "Q"
                    board = self.breathFirstSearch(board, [[0,i]],board_m,board_n)
                if board[-1][i] == "O":
                    #board[-1][i] == "Q"
                    board = self.breathFirstSearch(board, [[board_m-1,i]],board_m,board_n)
                


        
      
        

        
        for i in range(1,len(board[:-1])):
            print(i, " ", board[i][-1])
            
            l_C = "O" in board[i][0]
            
            if l_C == True:
                #board[i][0] = "Q"
                board = self.breathFirstSearch(board, [[i,0]],board_m,board_n)

            
            r_C = "O" in board[i][-1]
            if r_C == True:
                #board[i][-1] = "Q"
                
                board = self.breathFirstSearch(board, [[i,board_n-1]],board_m,board_n)
   
        print(board)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "Q":
                    board[i][j] = "O"
        
        
    def breathFirstSearch(self,board, queue, m, n):
        loc = queue.pop(0)
        current_value = board[loc[0]][loc[1]]
        if current_value == "O":
            board[loc[0]][loc[1]] = "Q"
        elif current_value == "X":
            return board
        
        directions = [
            [loc[0]-1, loc[1]],
            [loc[0], loc[1] -1 ],
            [loc[0], loc[1] + 1],
            [loc[0]+1, loc[1]],
        ]
     
        for dire in directions:
            if (dire[0] < m and dire[0] >= 0) and ( dire[1] < n and dire[1] >= 0):
                current_dire = board[dire[0]][dire[1]]
                if current_dire == "O":
                    #only add to queue if its an O so we dont loop over muitple things
                    board[dire[0]][dire[1]] = "Q"
                    queue.append(dire)

        if len(queue) == 0:
            return board
        else:
            return self.breathFirstSearch(board, queue, m, n)

        