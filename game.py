print("This is a Tic Tac Toe game.\nPlayer 1 is x, player 2 is o.\nCorrect input looks like: x, y i.e. 1,2, where x is number of column and y is number of row.")

table = [" "]*9


def printtable(table=[]):
    print("_______")
    print("|{}-{}-{}|".format(table[0], table[1], table[2]))
    print("|{}-{}-{}|".format(table[3], table[4], table[5]))
    print("|{}-{}-{}|".format(table[6], table[7], table[8]))
    print(u"\u203E"*7)


def inputchecker(move):
    if not len(move) == 3:
        print("Input incorrect. Make sure to put in in following form: 1,2 and try again.")
        return False
    if not move[1] == ",":
        print("Input incorrect. Try again.")
        return False
    if not (move[0] == "1" or move[0] == "2" or move[0] == "3"):
        print("Input incorrect. Try again.")
        return False
    if not (move[2] == "1" or move[2] == "2" or move[2] == "3"):
        print("Input incorrect. Try again.")
        return False
    return True


def tableassignment(move, player):
    move = move.split(",")
    move = list(map(lambda number: int(number), move))
    if not table[((move[0]-1)*3+move[1])-1] == " ":
        print("This place on the table is already taken. Try again.")
        return False
    table[(move[0]-1)*3+move[1]-1] = player
    return True


def checkwinner():
    def whichplayer(symbol):
        if symbol == "x":
            return "1"
        else:
            return "2"

    if table[0] == table[1] == table[2] and not table[0] == " ":
        print("Player {} won.".format(whichplayer(table[0])))
        return True
    if table[3] == table[4] == table[5] and not table[3] == " ":
        print("Player {} won.".format(whichplayer(table[3])))
        return True
    if table[6] == table[7] == table[8] and not table[6] == " ":
        print("Player {} won.".format(whichplayer(table[6])))
        return True
    if table[0] == table[3] == table[6] and not table[0] == " ":
        print("Player {} won.".format(whichplayer(table[0])))
        return True
    if table[1] == table[4] == table[7] and not table[1] == " ":
        print("Player {} won.".format(whichplayer(table[1])))
        return True
    if table[2] == table[5] == table[8] and not table[2] == " ":
        print("Player {} won.".format(whichplayer(table[2])))
        return True
    if table[0] == table[4] == table[8] and not table[0] == " ":
        print("Player {} won.".format(whichplayer(table[0])))
        return True
    if table[2] == table[4] == table[6] and not table[2] == " ":
        print("Player {} won.".format(whichplayer(table[2])))
        return True
    return False


def isfull():
    for element in table:
        if element == " ":
            return False
    return True


iswon = False
lastplayer = 2

while not iswon:
    if lastplayer == 1:
        move = input("Type input for player 2: ")
        if not inputchecker(move):
            continue
        lastplayer = 2
        if not tableassignment(move, "o"):
            continue
        if checkwinner() == True:
            iswon = True

    elif lastplayer == 2:
        move = input("Type input for player 1: ")
        if not inputchecker(move):
            continue
        lastplayer = 1
        if not tableassignment(move, "x"):
            continue
        if checkwinner() == True:
            iswon = True

    printtable(table)
    if isfull() and not iswon:
        print("Draw!")
        break
