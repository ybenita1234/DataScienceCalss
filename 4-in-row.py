from graphics import *
#from playsound import playsound

import random

class Window:

    def __init__(self):
        self.win = GraphWin("Four in a Row Game", 504,572)
        self.win.setBackground('gray')
        self.circles = [] #the list of all circles i nthe board
        self.gameBoard = []
        self.row  = []    #the row circles of the chosen rows
        self.rowIndex = [0,0,0,0,0,0,0] #the last filled circle in a row

        #Players label on the screen
        self.player_1 = Text(Point(70 ,540), 'Player 1')
        self.player_2 = Text(Point(430,540), 'Player 2')
        self.gameStart = Text(Point(250 ,540), 'New Game')

        self.player_2.setTextColor('black')
        self.player_2.setStyle('italic')
        self.player_2.setSize(20)
        self.player_2.draw(self.win)

        self.player_1.setTextColor('black')
        self.player_1.setStyle('italic')
        self.player_1.setSize(20)
        self.player_1.draw(self.win)

        #the start game start label
        self.gameStart.setTextColor('green')
        self.gameStart.setStyle('italic')
        self.gameStart.setSize(20)
        self.gameStart.draw(self.win)

        for i in range(6):  # rows
            self.gameBoard.append([])
            for j in range(7):  # column
                self.gameBoard[i].append(0)

    def Init(self): #Init the board ofr new Game

        self.player_1.setTextColor('black')
        self.player_2.setTextColor('black')
        self.gameStart.setTextColor('yellow')
        self.rowIndex = [0, 0, 0, 0, 0, 0, 0]

        for i in range(6):  # rows
            for j in range(7):  # column
                self.circles[i][j].setFill('white')

        for i in range(6):  # rows
            for j in range(7):  # column
                self.gameBoard[i][j] = 0

    def drawGamePannel(self):
        int_x = 36
        int_y = 36
        x_step = 36
        y_step = 108

        for i in range(6): #rows
            self.circles.append([])
            for j in range(7): #column
                pt = Point(int_x*j*2+x_step,int_y*i*2+y_step)
                self.circles[i].append(Circle(pt,30))
                self.circles[i][j].setFill('white')
                self.circles[i][j].draw(self.win)

        for i in range(7):
            pt = Point(i*2*36+36, 36)
            self.row.append(Circle(pt, 20))
            self.row[i].setFill('green')
            self.row[i].draw(self.win)

    ### check if he palyer won ######
    def checkWin(self,index,player):

        y = index -1
        x = self.rowIndex[index-1]
        Found = False
        x1 = 5-x
        y1 = y
        c = 0
        ### check down column
        while c < 5 and x1 <= 5:
            if self.gameBoard[x1][y1] == player:
                c += 1
            x1 += 1
        if c == 4:
            return player

        ## check row right-left###
        c = 1
        x1 = x2 = 5 - x
        y1 = y2 = y

        y1 += 1
        while c < 5 and y1 < 7:
            if self.gameBoard[x1][y1] == player:
                c += 1
            y1 += 1

        if c == 4:
            return player

        y2 -= 1
        while c < 5 and y2 >= 0:
            if self.gameBoard[x2][y2] == player:
                c += 1
            y2 -= 1
        if c == 4:
            return player

        ## check for diagonal 1###
        c = 1
        x1 = x2 = 5 - x
        y1 = y2 = y
        x1 += 1
        y1 += 1

        while c < 5 and y1 <= 6 and x1 >= 0 and x1 <= 5:
            print(x1, y1)
            if self.gameBoard[x1][y1] == player:
                c += 1
                print(x1, y1, c, self.gameBoard[x1][y1], 'hh')
            y1 += 1
            x1 += 1

        if c == 4:
            return player
        x2 -= 1
        y2 -= 1
        print(x2, y2)

        while c < 5 and y2 >= 0 and x2 >= 0:
            if self.gameBoard[x2][y2] == player:
                c += 1
            print(x2, y2, c, self.gameBoard[x2][y2], 'kk')
            y2 -= 1
            x2 -= 1

        if c == 4:
            return player

        ## check for diagonal 2###
        c = 1
        x1 = x2 = 5 - x
        y1 = y2 = y
        x1 += 1
        y1 -= 1
        print(x2, y2)
        while c < 5 and y1 >= 0 and x1 >= 0 and x1 <= 5:
            print(x1, y1)
            if self.gameBoard[x1][y1] == player:
                c += 1
            print(x1, y1, c, self.gameBoard[x1][y1], 'rr')
            y1 -= 1
            x1 += 1

        if c == 4:
            return player
        x2 -= 1
        y2 += 1
        print(x2, y2)
        while c < 5 and y2 <= 6 and y >= 0 and x2 >= 0:
            if self.gameBoard[x2][y2] == player:
                c += 1
            print(x2, y2, c, self.gameBoard[x2][y2], 'oo')
            y2 += 1
            x2 -= 1

        if c == 4:
            return player

        return 0

    #add circle to the board
    def addCircle(self,color, rowNum):
        player = 0
        if(rowNum> 0 and rowNum < 8):
            if self.rowIndex[rowNum - 1] < 6:
                for i in range(0,5-self.rowIndex[rowNum-1]):
                    self.circles[i][rowNum-1].setFill(color)
                    time.sleep(0.1)
                    self.circles[i][rowNum - 1].setFill('white')
                self.circles[5 - self.rowIndex[rowNum-1]][rowNum - 1].setFill(color)
                if color == 'red':
                    self.gameBoard[5 - self.rowIndex[rowNum-1]][rowNum - 1] = 1
                    player = 1
                elif color == 'blue':
                    self.gameBoard[5 - self.rowIndex[rowNum - 1]][rowNum - 1] = 2
                    player = 2
                winner = self.checkWin(rowNum,player)
                self.rowIndex[rowNum - 1] = self.rowIndex[rowNum - 1] + 1

                if sum(self.rowIndex) == 42: #all circle are filled
                    return 1,winner
                else:
                    return 0,winner
        return 0,0

    def colorChange(self):
        x = y = 0
        while True:
            self.win.getMouse()
            self.circles[x][y].setOutline('black')
            self.circles[x][y].setFill('white')
            x = random.randint(0,5)
            y = random.randint(0,6)
            self.circles[x][y].setOutline('red')
            self.circles[x][y].setFill('blue')

class Game:

    def __init__(self,board):
        name = "four in a line"
        self.win = board.win
        self.board = board
        self.circles = []

    def waitForStart(self):
        # start the game
        while True:
            p = self.win.getMouse()
            # new game was pressed
            if p.getX() < 320 and p.getX() > 180 and p.getY() > 525 and p.getY() < 555:
                self.board.gameStart.setTextColor('yellow')
                break

    def chooseRow(self):
        rowChosen = 0
        #wait for choosing a line
        while rowChosen == 0 :
            p = self.win.getMouse()
            rowChosen = 0

            if p.getX() < 56  and p.getX() > 16  and p.getY() > 16  and p.getY() < 56 :
                #self.board.row[0].setTextColor('yelow')
                rowChosen = 1

            if p.getX() < 128  and p.getX() > 88  and p.getY() > 16  and p.getY() < 56 :
                #self.board.row[0].setTextColor('yelow')
                rowChosen = 2

            if p.getX() < 200  and p.getX() > 160  and p.getY() > 16  and p.getY() < 56 :
                #self.board.row[0].setTextColor('yelow')
                rowChosen = 3

            if p.getX() < 272  and p.getX() > 232  and p.getY() > 16  and p.getY() < 56 :
                #self.board.row[0].setTextColor('yelow')
                rowChosen = 4
            if p.getX() < 344 and p.getX() > 304 and p.getY() > 16 and p.getY() < 56:
                # self.board.row[0].setTextColor('yelow')
                rowChosen = 5

            if p.getX() < 410 and p.getX() > 370 and p.getY() > 16 and p.getY() < 56:
                # self.board.row[0].setTextColor('yelow')
                rowChosen = 6

            if p.getX() < 488 and p.getX() > 448 and p.getY() > 16 and p.getY() < 56:
                # self.board.row[0].setTextColor('yelow')
                rowChosen = 7
            # Check for new Game request
            if p.getX() < 320 and p.getX() > 180 and p.getY() > 525 and p.getY() < 555:
                self.board.gameStart.setTextColor('yellow')
                time.sleep(0.2)
                self.board.gameStart.setTextColor('green')
                rowChosen = 100

        return rowChosen

    # add circle in a row
    def addCircle(self,player,row):
        winner = 0
        if player == 'player_1':
            winner = self.board.addCircle('red',row)
        elif player == 'player_2':
            winner = self.board.addCircle('blue', row)

        return winner

    #Main Game Loop
    def play(self):

        winner = 0
        gameDone = 0

        while True:
            # Player 1
            self.board.player_2.setTextColor('black')
            self.board.player_1.setTextColor('red')
            x = self.chooseRow()
            if x == 100:
                print("start new Game")
                gameDone = 2
                break
            else:
                gameDone, winner = self.addCircle('player_1',x)
                if winner:  # gave over
                    break
                #print(winner, '***')
            #Player 2

            self.board.player_1.setTextColor('black')
            self.board.player_2.setTextColor('blue')
            x = self.chooseRow()
            if x == 100:
                print("start new Game")
                gameDone = 2
                break
            else:
                gameDone, winner = self.addCircle('player_2',x)
                if winner:  # gave over
                    break

        return gameDone, winner

def main():

    gameDone = 0
    winner   = 0
    #playsound('~/Glass.aiff')

    gameBoard = Window()
    game      = Game(gameBoard)
    gameBoard.drawGamePannel()

    gameOver = Text(Point(250, 250), '')
    gameOver.setTextColor('Black')
    gameOver.setSize(30)
    gameOver.draw(gameBoard.win)

    while True:
        gameBoard.gameStart.setTextColor('green')
        if gameDone != 2:
            game.waitForStart() #wait until user push start game
        gameBoard.Init()
        gameOver.setText('')
        gameDone, winner = game.play()

        if gameDone == 1 and  winner == 0: #no winner
            gameOver.setText('Game Over')
        elif winner == 1:
            gameOver.setText('Palyer 1 Won')
        elif winner == 2:
            gameOver.setText('Palyer 2 Won')
        elif gameDone == 2: #start new game
            continue

main()
