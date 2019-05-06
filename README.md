### Four in a Row - Game -- in Python ###

This python App execute the game 4 in a rwo between two live players.It uses the graphics.py package for displaying graphics on the screen. 

#### Running the App
Execute the command on the command line: python python-project.py

#### Game operation:

1. Push the "New Game" button to start
2. Player 1 should choose the column to insert the coin, by clicking the green circle above the desired column.
3. Then Player one should do the same.
4. The game continues until one of things happen:
	* The board is filled and there is no winner
	* Either player 1 or player 2 were able to get a row of 4 continues coins with the same color. (blue or red)
5. The App identified a winner, mention it on the screen and wait for a start of a new game.
6. The App have the option to start a new game at any point, by pushing the "New Game" button.
7. The App count the number of wins of every player and present it on the screen.

#### Code Structure:

The code is composed of a main function and 2 main classes:

* Class Window: responsible for the graphic presentation
* Class Game: using the Window class for operating the game logic.

#### Class Methods:
**Class Window:**

***def __init__(self):*** init the object and create the presentation board that includes 7 columns and 6 rows with empty circles. The board presentation and state is saved in the object.

***def Init(self)*** Initialize the view and the parameters when a new game is requested.

***def drawGamePannel(self):*** draw the game board based on the presentation state.

***def checkWin(self,index,player):*** This is the main method in App. It includes the logic for checking if player won in the last operation. It gets the player number and the index of the last chose column. Using the board status, check if there are 4 continues coins with the player 1 color (red or blue) in a row. 

***def addCircle(self,color, rowNum):*** insert a coin with color "color" to column "rowNum" on the board. Update the board state accordingly.

**Class Game:**

***def __init__(self,board):*** get the Window object as the presentation board for the game and initialize parameters.  

***def waitForStart(self):*** continue to get mouse click location until the user click the "New Game" button.

***def chooseRow(self):*** check if the user clicked on a column and if yes return the index of the column.

***def addCircle(self,player,row):*** If the user chose a valid column insert a coin with the right color to the chose column.

***def play(self):*** This is the game loop which does the following:

1. Wait for user mouse click: a new column or new game.
2. Insert a coin to the chose column or start a new game.
3. Repeat the process for player 1 and then 2 continually until there is a winner or the board is filled.
4. Return the winner or game over status.

***main() Method***

In the main the App creates the objects and runs an infinite loop of games until the user closes the window.

![](https://drive.google.com/file/d/12znwqQn6wSxA-vwdGs22qOv4TKeKz_ew/view?usp=sharing
