#  A simple Tic-Tac-Toe game
# Players 'X' and 'O' take turn inputing their position on the command line using numbers 1-9
# 1 | 2 | 3
# ---------
# 4 | 5 | 6
# ---------
# 7 | 8 | 9
#


board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}


def markBoard(position, mark):
    position = int(position)
    board[position] = mark

"""
In this function we need to draw the updated board along with values
"""

def printBoard():

    tempBoard = {
        1: '1', 2: '2', 3: '3',
        4: '4', 5: '5', 6: '6',
        7: '7', 8: '8', 9: '9'
    }

    for k in board.keys():
        if board[k] == ' ':
            tempBoard[k] = tempBoard[k]
        else:
            tempBoard[k] = board[k]

    print(tempBoard[1] + ' | ' + tempBoard[2] + ' | ' + tempBoard[3])
    print("---------")
    print(tempBoard[4] + ' | ' + tempBoard[5] + ' | ' + tempBoard[6])
    print("---------")
    print(tempBoard[7] + ' | ' + tempBoard[8] + ' | ' + tempBoard[9] + "\n")


def validateMove(position):
    try:
        position = int(position)

        if position >= 1 and position <= 9 and board[position] == ' ':
            return True
        else:
            return False
    except ValueError:
        return False


winCombinations = [
    # Horizontal
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    # Vertical
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    # Diagonal
    [1, 5, 9],
    [3, 5, 7]

]

def checkWin(player):
    for combo in winCombinations:
        if board[combo[0]] == player and board[combo[1]] == player and board[combo[2]] == player:
            return True
    return False


def checkFull():
    for i in board:
        if board[i] == ' ':
            return False
    return True


def restartGame():

    print('Do you want to play again? (y/n)')

    restart = input()

    global gameEnded
    global board


    while(restart):

        if restart.lower() == 'y':
            board = {
                1: ' ', 2: ' ', 3: ' ',
                4: ' ', 5: ' ', 6: ' ',
                7: ' ', 8: ' ', 9: ' '
            }
            gameEnded = False
            break
        elif restart.lower() == 'n':
            print("Thanks for playing!!!")
            gameEnded = True
            break
        else:
            print('Invalid Input!!! \nDo you want to play again? (y/n)')
            restart = input()


#########################################################
## Copy all your code/fucntions in Part 1 to above lines
## (Without Test Cases)
#########################################################

gameEnded = False
currentTurnPlayer = 'X'

# entry point of the whole program
print('Game started: \n\n' +
    ' 1 | 2 | 3 \n' +
    ' --------- \n' +
    ' 4 | 5 | 6 \n' +
    ' --------- \n' +
    ' 7 | 8 | 9 \n')

# TODO: Complete the game play logic below
# You could reference the following flow
# 1. Ask for user input and validate the input
# 2. Update the board
# 3. Check win or tie situation
# 4. Switch User

while not gameEnded:

        move = input(currentTurnPlayer + "'s turn, input: ")
        validateMove(move)
        
        while not validateMove(move):
            print('Oops, your input either occupied or out of bound!!! Please try again')
            move = input(currentTurnPlayer + "'s turn, input: ")

        markBoard(move, currentTurnPlayer)
        printBoard()

        if checkWin(currentTurnPlayer):
            print("The winner is " + currentTurnPlayer)
            restartGame()
        elif checkFull():
            print("It's a tie!")
            restartGame()
        else:
            if currentTurnPlayer == 'X':
                currentTurnPlayer = 'O'
            else:
                currentTurnPlayer = 'X'
        


# Bonus Point: Implement the feature for the user to restart the game after a tie or game over