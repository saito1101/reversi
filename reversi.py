import tkinter as tk

none = 0
black = 1
white = 2
outside = -1
clkx = 0
clky = 0
clk = 1
size = 8

board = [
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, 0, 0, 0, 0, 0, 0, 0, 0, -1],
    [-1, 0, 0, 0, 0, 0, 0, 0, 0, -1],
    [-1, 0, 0, 0, 0, 0, 0, 0, 0, -1],
    [-1, 0, 0, 0, 2, 1, 0, 0, 0, -1],
    [-1, 0, 0, 0, 1, 2, 0, 0, 0, -1],
    [-1, 0, 0, 0, 0, 0, 0, 0, 0, -1],
    [-1, 0, 0, 0, 0, 0, 0, 0, 0, -1],
    [-1, 0, 0, 0, 0, 0, 0, 0, 0, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    ]

window = tk.Tk()
window.geometry("1024x850")
window.resizable(False, False)
window.title("reversi")

canvas = tk.Canvas(window, width=804, height=804, bg="green")
canvas.place(x=25, y=25)

def display():
    for i in range(size+1):
        x = 100*i +4
        y = 100*i +4
        canvas.create_line(x, 4, x, 804, fill="black", width=2)
        canvas.create_line(4, y, 804, y, fill="black", width=2)
display()

def piece():
    for r in range(1, size+1):
        for c in range(1, size+1):
            X = (c-1)*100 +4
            Y = (r-1)*100 +4
            if board[r][c] == black:
                canvas.create_oval(X+10, Y+10, X+90, Y+90, fill="black", width=0)
            elif board[r][c] == white:
                canvas.create_oval(X+10, Y+10, X+90, Y+90, fill="white", width=0)
piece()

def event(r, c, color):
    for y in range(-1, 2):
        for x in range(-1, 2):
            searchr = r
            searchc = c
            n = 0
            while True:
                searchr += y
                searchc += x
                if board[searchr][searchc] <= 0:
                    print(board[searchr][searchc])
                    break
                elif board[searchr][searchc] == 3-color:
                    n += 1
                elif board[searchr][searchc] == color:
                    for i in range(n):
                        searchr -= y
                        searchc -= x
                        board[searchr][searchc] = color

def click(c):
    global clkx, clky, clk
    clkx = int((c.x -25 +4)/100) +1
    clky = int((c.y -25 +4)/100) +1
    print(clkx)
    print(clky)
    if clk%2 == 0:
        board[clky][clkx] = white
        piece()
        event(clky, clkx, white)
    else:
        board[clky][clkx] = black
        piece()
        event(clky, clkx, black)
    # print(board)
    clk += 1
canvas.bind("<Button>", click)


window.mainloop()
