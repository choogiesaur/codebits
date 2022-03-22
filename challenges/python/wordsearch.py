# It works, quicker than 93% on LC
# But I have alot of repetitious code.
# Find a way to do all the boundary checks in one

# General gist:
# Iterate entire board, when you find a match with first char of word, start a search there
# Possible optimization: Also check for match with last char, and feed word backwards (match word from end to beginning)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])
        
        found = [ False ]
            
        def recurse(y, x, i):
            # print(y,x,i)
            
            if i == len(word):
                found[0] = True
                return
            
            if 0 < y and word[i] == board[y-1][x]:
                temp = board[y][x]
                board[y][x] = '#'
                recurse(y-1, x, i+1)
                board[y][x] = temp
                if found[0] == True:
                    return
            if y + 1 < rows and word[i] == board[y+1][x]:
                temp = board[y][x]
                board[y][x] = '#'
                recurse(y+1, x, i+1)
                board[y][x] = temp
                if found[0] == True:
                    return
            if 0 < x and word[i] == board[y][x-1]:
                temp = board[y][x]
                board[y][x] = '#'
                recurse(y, x-1, i+1)
                board[y][x] = temp
                if found[0] == True:
                    return
            if x + 1 < cols and word[i] == board[y][x+1]:
                temp = board[y][x]
                board[y][x] = '#'
                recurse(y, x+1, i+1)
                board[y][x] = temp
                if found[0] == True:
                    return
        
        for y in range(rows):
            for x in range(cols):
                if board[y][x] == word[0]:
                    temp = board[y][x]
                    board[y][x] = '#'
                    recurse(y,x,1)
                    board[y][x] = temp
                    if found[0] == True:
                        return True
                
        return False
