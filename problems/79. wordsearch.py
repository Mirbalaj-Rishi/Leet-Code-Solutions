import copy 
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        first_letter = word[0]
        result = False 
        wordSet = set(word)
        for letter in wordSet: #check if all letters is in board
            letterIn = False
            for i in board:
                if letter in i:
                    letterIn = True
            if letterIn == False:
                return letterIn
        for i in range(len(board)):
            
                    
            for j in range(len(board[i])):
                if board[i][j] == first_letter:
                    myBoard = DFS(board, i,j,word)
                    result = myBoard.move()
                    if result == True:
                        break
            if result == True:
                break
        return result

        
class DFS:
    def __init__(self,board,root_outer, root_inner, word):
        self.board = board
        self.root_outer = root_outer
        self.root_inner = root_inner
        self.current_inner = root_inner
        self.current_outer = root_outer
        self.m = len(board)
        self.n = len(board[0])
        self.word = word
        self.stack = []
        self.word_index = 0
    def up(self):
        outer = self.current_outer
        outer -= 1
        if outer < 0:
            outer += 1
            return "no value"
        return self.board[outer][self.current_inner]
    
    def down(self):
        outer = self.current_outer
        outer += 1
        if outer >= self.m:
            outer -= 1
            return "no value"
        return self.board[outer][self.current_inner]
        
    def right(self):
        inner = self.current_inner
        inner += 1 
        if inner >= self.n:
            inner -= 1
            return "no value"
        return self.board[self.current_outer][inner]
    def left(self):
        inner = self.current_inner
        inner -= 1
        if inner < 0:
            inner += 1
            return "no value"
        return self.board[self.current_outer][inner]
    
    def search(self):
        self.word_index += 1
        
        # if self.word_index >= len(self.word)-1:
        #     return True
        # else:
        #     self.next_letter = self.word[self.word_index]
        if len(self.word) == 1:
            return True
        self.next_letter = self.word[self.word_index]
        up_val = self.up()
        down_val = self.down()
        left_val = self.left()
        right_val = self.right()
        #print("     next",self.next_letter,"up",up_val,"down",down_val,"left",left_val,"right",right_val)
        if self.next_letter == up_val:
            temp_inner =self.current_inner
            temp_outer = self.current_outer-1
            self.stack.append((temp_outer,temp_inner))
        if self.next_letter == down_val:
            temp_inner =self.current_inner
            temp_outer = self.current_outer+1
            self.stack.append((temp_outer,temp_inner))
        if self.next_letter == left_val:
            temp_inner =self.current_inner-1
            temp_outer = self.current_outer
            self.stack.append((temp_outer,temp_inner))
        if self.next_letter == right_val:
            temp_inner =self.current_inner+1
            temp_outer = self.current_outer
            self.stack.append((temp_outer,temp_inner))
        # if len(self.stack) > 0:
        #     if self.stack[-1][0] in self.prev_cords_outer and self.stack[-1][1] in self.prev_cords_inner:
        #         for i in range(len(self.prev_cords_outer)):
        #             out_ii = self.prev_cords_outer[i]
        #             in_ii = self.prev_cords_inner[i]
        #             print(in_ii," ",out_ii)
        #             if self.board[out_ii][in_ii] == self.stack[-1][0]:
        #                 self.stack.pop(-1) #so we dont go back where we came
        #                 break

        # if self.next_letter != up_val and self.next_letter != down_val and self.next_letter != left_val and self.next_letter != right_val:
        #     print("search false")
        #     return False
        
    def move(self):
        #print("-----------------------")
        
        
        search_val =  self.search()
        if search_val == True:
            #print("this works")
            return True
        # if len(self.word) <= 1:
            
        #     return True
        #print(self.word," letter",self.board[self.current_outer][self.current_inner]," outer", self.current_outer, " inner",self.current_inner, " stack", self.stack)
        for i in reversed(self.stack):
            listOfNewCords = i
            
            new_board = copy.deepcopy(self.board)
            new_board[self.current_outer][self.current_inner] = "no value"
            new_DFS = DFS(new_board,listOfNewCords[0], listOfNewCords[1], self.word[self.word_index:])
            #print(self.word[self.word_index:])
            if new_DFS.move() == True:
                return True
        
        return False
        
        