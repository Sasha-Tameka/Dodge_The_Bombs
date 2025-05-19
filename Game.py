import tkinter
import random

# Track whether the game is over, the score, and how many squares to clear
gameOver = False
score = 0
squaresToClear = 0

# Create the game board
bombfield = []
def create_bombfield():
    global squaresToClear
    
    for row in range(1, 10):
        rowList = []
        for column in range(1, 10):
            if random.randint(1, 100) < 20:
                rowList.append(1)  # 1 means there's a bomb
            else:
                rowList.append(0)
                squaresToClear += 1
        bombfield.append(rowList)
    printfield(bombfield)
    #return bombfield

# Print the board in the console
def printfield(bombfield):
    for rowList in bombfield:
        print(rowList)

# Layout the game window (placeholder for now)
def layout_window(window):
    label = tkinter.Label(window, text="Bomb Dodger Game")
    label.pack()

# Start the game
def play_bombdodger():
    bombfield = create_bombfield()
    window = tkinter.Tk()
    layout_window(window)
    window.mainloop()



#window layout
def layout_window(window):
    for rowNumber, rowList in enumerate(bombfield):
        for columnNumber, columnEntry in enumerate(rowList):
            if random.randint(1,100)<25:
                square = tkinter.Label(window, text="    ", bg="darkgreen")
            elif random.randint(1,100)>75:
                square = tkinter.Label(window, text="    ", bg="seagreen")
            else:
                square = tkinter.Label(window, text="    ", bg="green")
            square.grid(row=rowNumber, column=columnNumber)
            square.bind("<Button-1>", on_click)
            
#click function
def on_click(event):
    global score
    global gameOver
    global squaresToClear
    
    square = event.widget
    row = int(square.grid_info()["row"])
    column = int(square.grid_info()["column"])
    currentText = square.cget("text")
    
    if bombfield[row][column] == 1:
        gameOver= True
        square.config(bg = "red")
        print("Game Over! You hit a bomb!")
        print("Your score was:", score)
    elif currentText == "    ":
        square.config(bg = "brown")
        totalBombs = 0
        
        if row < 9:
            if bombfield[row+1][column] == 1:
                totalBombs += 1
        if row > 0:
            if bombfield[row-1][column] == 1:
                totalBombs += 1
        if column > 0:
            if bombfield[row][column-1] == 1:
                totalBombs += 1
        if column < 9:
            if bombfield[row][column-1] == 1:
                totalBombs += 1
        if row > 0 and column > 0:
            if bombfield[row-1][column-1] == 1:
                totalBombs += 1
        if row < 9 and column < 9:
            if bombfield[row+1][column+1] == 1:
                totalBombs += 1
        if row < 9 and column > 0:
            if bombfield[row+1][column-1] == 1:
                totalBombs += 1
        if row > 0 and column < 9:
            if bombfield[row-1][column+1] == 1:
                totalBombs += 1
                
        square.config(text = " " + str(totalBombs) + " ")
        score += 1
        squaresToClear -= 1
        
        if squaresToClear == 0:
            gameOver = True
            print("Well done! You cleared the board!")
            print("Your score was:", score)

# Run the game
play_bombdodger()