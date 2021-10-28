#Tic Tac Toe - Duncan Tasker

import random

#current_turn 0 = X, 1 = O
# x value = -4
# o value = 5
# x - - = -4, x x - = -8, x x x = -12
# o - - = 5, o o - = 10, o o o = 15
# x o - = 1, x o o = 6, o x x = -3

def init():
    #initialize playspace with blanks, 
    playspace = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    move_count = ["x", 0]
    last_move = []
    global PLAYER_SIGN
    sign_is_valid = False
    while sign_is_valid == False:
        PLAYER_SIGN = input("Would you like to play Xs or Os? (x/o) :: ")
        if PLAYER_SIGN == "x" or PLAYER_SIGN == "o":
            sign_is_valid = True
        else:
            print("Please enter either an x or an o.")
    print()
    drawplayspace(playspace)
    if PLAYER_SIGN == "x":
        playerinput(move_count, playspace)
    elif PLAYER_SIGN == "o":
        computermove(move_count, playspace, last_move)
    
def drawplayspace(playspace):
    currentrow = []
    print()
    print("  1   2   3")
    for y in range(3):
        #translate numbers in playspace array into x and o moves on the board using currentrow as temp storage
        for x in range(3):
            if playspace[y][x] == -4:
                currentrow.insert(x, "x")
            elif playspace[y][x] == 5:
                currentrow.insert(x, "o")
            else:
                currentrow.insert(x, "-")
        #print the row contents and a line of dashes to separate the rows
        print(y+1, currentrow[0], "|", currentrow[1], "|", currentrow[2])
        if y < 2:
            for i in range(11):
                if i < 10:
                    print("-",end="")
                else:
                    print("-")
        
def playerinput(move_count, playspace):
    userx = int(input("Enter the column number of your move :: ")) - 1
    usery = int(input("Enter the row number of your move :: ")) - 1
    
    if (userx > 2 or userx < 0) or (usery > 2 or usery < 0):
        print("Please enter number between 1-3 for column and row")
        playerinput(move_count, playspace)
    if playspace[usery][userx] != 0:
        print("Space is taken, please chose free space.")
        playerinput(move_count, playspace)
        
    plotmove(userx, usery, move_count, playspace)
    
def plotmove(x, y, move_count, playspace):
    last_move = [x, y]
    if move_count[0] == "x":
        playspace[y][x] = -4
        move_count[0] = "o"
    elif move_count[0] == "o":
        playspace[y][x] = 5
        move_count[0] = "x"
    move_count[1] += 1
    drawplayspace(playspace)
    wincheck(playspace)
    
    if (move_count[0] == "x" and PLAYER_SIGN == "x") or (move_count[0] == "o" and PLAYER_SIGN == "o"):
        playerinput(move_count, playspace)
    elif (move_count[0] == "x" and PLAYER_SIGN == "o") or (move_count[0] == "o" and PLAYER_SIGN == "x"):
        computermove(move_count, playspace, last_move)
        

def wincheck(playspace):
    #iterate through each row to check for wins, then each columns, then each diagonal, if all spaces are taken declare draw
    for y in range(3):
        section_total = 0
        for x in range(3):
            section_total += playspace[y][x]
        if section_total == -12 or section_total == 15:
            if section_total == -12:
                winstate("x", "horizontally")
            else:
                winstate("o", "horizontally")  
       
    for x in range(3):
        section_total = 0 
        for y in range(3):
            section_total += playspace[y][x]
        if section_total == -12 or section_total == 15:
            if section_total == -12:
                winstate("x", "vertically")
            else:
                winstate("o", "vertically")

    section_total = 0
    for x in range(3):
        section_total += playspace[x][x]
    if section_total == -12 or section_total == 15:
        if section_total == -12:
            winstate("x", "diagonally")
        else:
            winstate("o", "diagonally")
    
    section_total = 0
    y = 0
    for x in reversed(range(3)):
        section_total += playspace[x][y]
        y += 1
    if section_total == -12 or section_total == 15:
        if section_total == -12:
            winstate("x", "diagonally")
        else:
            winstate("o", "diagonally")
            
    is_row_full = 0
    for y in range(3):
        if playspace[y].count(0) == 0:
            is_row_full += 1
    if is_row_full == 3:
        winstate("draw", "-")

def winstate(sign_win, win_form):
    #print winning side and direction of win or declare draw
    if sign_win == "draw":
        print("Game is a draw")
    else:
        print(sign_win, "has won with a line", win_form)
        
    writescoreboard(sign_win)
    
    is_valid = False
    while is_valid == False:
        replay_input = input("Would you like to play again? (y/n) :: ")
        if replay_input == "y" or replay_input == "n":
            is_valid = True
        else:
            print("Please enter either 'y' for yes or 'n' for no")
    if replay_input == "y":
        init()
    else:
        exit()
    
def last_moveintent(playspace, last_move):
    #tests to see if the last move made was to block a win, return true (yes) or false (no)
    sums = [0,0,0,0]
    for x in range(3):
        sums[0] += playspace[x][last_move[0]]
        sums[1] += playspace[last_move[1]][x]
        
    if last_move == [0, 0] or last_move == [2, 2] or last_move == [1, 1]:
        for x in range(3):
            sums[2] += playspace[x][x]
        
    elif last_move == [2, 0] or last_move == [0, 2] or last_move == [1, 1]:
        y = 0
        for x in reversed(range(3)):
            sums[3] += playspace[x][y]
            y += 1
    
    correction_amount = playspace[last_move[1]][last_move[0]]
    correction = lambda a: a - correction_amount
    corrected_sums = list(map(correction, sums))
    
    if playspace[last_move[1]][last_move[0]] == -4:
        for x in corrected_sums:
            if x == 10:
                return True
    elif playspace[last_move[1]][last_move[0]] == 5:
        for x in corrected_sums:
            if x == -8:
                return True
    return False
    
def aiwinningmovecheck(check_amount, playspace):
    #checks for situations where one side can win, side checked is determined by check_amount
    for y in range(3):
        section_total = 0
        for x in range(3):
            section_total += playspace[y][x]
        if section_total == check_amount:
            for x in range(3):
                if playspace[y][x] == 0:
                    return x, y
            
    for x in range(3):
        section_total = 0 
        for y in range(3):
            section_total += playspace[y][x]
        if section_total == check_amount:
            for y in range(3):
                if playspace[y][x] == 0:
                    return x, y

    section_total = 0
    for x in range(3):
        section_total += playspace[x][x]
    if section_total == check_amount:
        for x in range(3):
            if playspace[x][x] == 0:
                return x, x

    section_total = 0
    y = 0
    for x in reversed(range(3)):
        section_total += playspace[x][y]
        y += 1
    if section_total == check_amount:
        y = 0
        for x in reversed(range(3)):
            if playspace[x][y] == 0:
                return y, x
            y += 1

    return 100,100

def randommove(last_move, playspace):
    #plots random move in corners unless all 4 are taken, then pick random free edge
    corners = [[0,0],[0,2],[2,0],[2,2]]
    edges = [[0,1],[1,0],[1,2],[2,1]]
    is_valid = False
    
    corners_full = True
    for i in corners:
        if playspace[i[1]][i[0]] == 0:
            corners_full = False
    
    if corners_full == False:
        while(is_valid == False):
            rand_corner = corners[random.randint(0,3)]
            if playspace[rand_corner[1]][rand_corner[0]] == 0:
                is_valid = True
        return rand_corner[0], rand_corner[1]
    else:
        while(is_valid == False):
            rand_edge = edges[random.randint(0,3)]
            if playspace[rand_edge[1]][rand_edge[0]] == 0:
                is_valid = True
        return rand_edge[0], rand_edge[1]
            
def computermove(move_count, playspace, last_move):
    #check for ai winning moves, check for player winning moves, if last move was to block a win choose random space,
    #if opponant goes edge choose opposite edge, if opponant went corner choose opposite corner, else choose random space
    if PLAYER_SIGN == "x":
        computer_amount = 10
        player_amount = -8
    elif PLAYER_SIGN == "o":
        computer_amount = -8
        player_amount = 10
    print("Computer Move...")
    if move_count[1] == 0:
        plotmove(0, 0, move_count, playspace)
    
        
    #check for winning moves
    ai_move = aiwinningmovecheck(computer_amount, playspace)
    if ai_move[0] != 100:
        #print("secured win")
        plotmove(ai_move[0], ai_move[1], move_count, playspace)
    
    #check for oppanant winning moves
    ai_move = aiwinningmovecheck(player_amount, playspace)
    if ai_move[0] != 100:
        #print("blocked win")
        plotmove(ai_move[0], ai_move[1], move_count, playspace)
        
    #if last move was to block win, go in random place
    if move_count[1] > 1:
        last_intent = last_moveintent(playspace, last_move)
        if last_intent:
            ai_move = randommove(last_move, playspace)
            plotmove(ai_move[0], ai_move[1], move_count, playspace)
    
    #take center space, elif oppanant went corner take opposite corner, if opponant went edge take opposite edge, if neither is possible take
    if playspace[1][1] == 0:
        #print("center move")
        plotmove(1,1, move_count, playspace)
    elif playspace[((last_move[1] * -1) + 2)][((last_move[0] * -1) + 2)] == 0:
        #print("opposite move")
        plotmove((last_move[0] * -1) + 2, (last_move[1] * -1) + 2, move_count, playspace)
    else:
        #print("random move")
        move = randommove(last_move, playspace)
        plotmove(move[0], move[1], move_count, playspace)
        
def writescoreboard(sign_win):
    file = open("scoreboard.csv", "r")
    contents = file.readlines()
    scores = contents[1].strip("\n").split(",")
    
    if sign_win == 'x':
        scores[0] = int(scores[0]) + 1
    elif sign_win == 'o':
        scores[1] = int(scores[1]) + 1
    elif sign_win == 'draw':
        scores[4] = int(scores[4]) + 1
        
    if PLAYER_SIGN == sign_win:
        scores[2] = int(scores[2]) + 1
    elif PLAYER_SIGN != sign_win and sign_win != 'draw':
        scores[3] = int(scores[3]) + 1
    file.close()
    
    print("X has won", scores[0], "times, O has won", scores[1], "times, the Player has won", scores[2], "times, the Computer has won", scores[3], "times, and there have been", scores[4], "draws")
    
    file = open("scoreboard.csv", "w")
    file.write("X wins, O wins, Player wins, Computer Wins, Draw\n")
    for i in range(len(scores)):
        if i < 4:
            file.write(str(scores[i])+',')
        else:
            file.write(str(scores[i]))

def main():
    #most in depth method, calls the init method
    init()
main()