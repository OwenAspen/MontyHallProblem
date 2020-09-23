print('**********Tic Tac Toe!**********')
#Tic Tac Toe.
#This fuction takes a list of lists as input, and prints the game board.
def tictacboard(GB):
    for x in range(1,4):
        print(' ---'*3,)
        for y in range(1,4):
            print('|', end = '')
            if GB[x][y] == 'x':
                print(' x ',end = '')
            if GB[x][y] == 'o':
                print(' o ',end = '')
            if GB[x][y] == 0:
                print('   ',end = '')
        print('|')
    print(' ---'*3,)
#This function checks the list of lists that represents the game to see if anyone has won.
def win_test(GB):
    #test horizontal
    for i in range(1,4):
        if GB[i][1] =='x' and GB[i][2] == 'x' and GB[i][3] == 'x' or GB[i][1] =='o' and GB[i][2] == 'o' and GB[i][3] == 'o':
            return True
    #test vertical
    for i in range(1,4):
        if GB[1][i] =='x' and GB[2][i] == 'x' and GB[3][i] == 'x' or GB[1][i] =='o' and GB[2][i] == 'o' and GB[3][i] == 'o':
            return True
    #test diagonal
    if GB[1][1] == 'x' and GB[2][2] == 'x' and GB[3][3] == 'x' or GB[1][1] == 'o' and GB[2][2] == 'o' and GB[3][3] == 'o':
        return True
    if GB[1][3] == 'x' and GB[2][2] == 'x' and GB[3][1] == 'x' or GB[1][3] == 'o' and GB[2][2] == 'o' and GB[3][1] == 'o':
        return True
    else:
        return False
#This function tests for a tie.
def tie_test(GB):
    ZC = 0
    for i in range(1,4):
        for j in range(1,4):
            if GB[i][j] == 0:
                ZC += 1
    if ZC == 0:
        return True
    else:
        return False
GameCount = 0
#main game loop (asks if you want to play again and resets the board if you do)
while True:
    if GameCount > 0:
        PA = input('Play again? (y/n): ')
        if PA == 'n':
            print(f'You played {GameCount} Games.')
            break
    GB = [  ['Place_holder_list'],
            ['PH',0,0,0],
            ['PH',0,0,0],
            ['PH',0,0,0]]
    GC = True
    while GC == True:
    #Going through this loop represents a single game.
        P1C = True
        P2C = True
        #This loop handles player 1 input
        while P1C == True:
            P1 = input('Player 1 enter your move (x,y): ')
            if int(P1[0]) < 1 or int(P1[0]) > 3 or int(P1[2]) < 1 or int(P1[2]) > 3:
                print('Enter numbers between 1 and 3')
            if GB[int(P1[0])][int(P1[2])] != 0:
                print('This space is already taken!')
            else:
                P1C = False
                GB[int(P1[0])][int(P1[2])] = 'x'
            tictacboard(GB)
            if win_test(GB) == True:
                print('Player 1 wins!')
                GameCount += 1
                P2C = False
                GC = False
            if tie_test(GB) == True:
                print('Tie!')
                GameCount += 1
                P2C = False
                GC = False
        #This loop handles player 2 input
        while P2C == True:
            P2 = input('Player 2 enter your move (x,y): ')
            if int(P2[0]) < 1 or int(P2[0]) > 3 or int(P2[2]) < 1 or int(P2[2]) > 3:
                print('Enter numbers between 1 and 3')
            if GB[int(P2[0])][int(P2[2])] != 0:
                print('This space is already taken!')
            else:
                P2C = False
                GB[int(P2[0])][int(P2[2])] = 'o'
            tictacboard(GB)
            if win_test(GB) == True:
                print('Player 2 wins!')
                GameCount += 1
                GC = False
            if tie_test(GB) == True:
                print('Tie!')
                GameCount += 1
                GC = False
