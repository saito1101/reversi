import tkinter as tk

black = 1
white = 2
clkx = 0
clky = 0
clk = 4
cell = 0
unable = []
label = ""
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
window.geometry("1300x850")
window.resizable(False, False)
window.title("reversi")

canvas = tk.Canvas(window, width=804, height=804, bg="green")
canvas.place(x=25, y=25)

size = 8
def display():
    for i in range(size+1):
        x = 100*i+4
        y = 100*i+4
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
                    break
                if board[searchr][searchc] == 3-color:
                    n += 1
                if board[searchr][searchc] == color:
                    for i in range(n):
                        searchr -= y
                        searchc -= x
                        board[searchr][searchc] = color
                    break

def able(r, c, color):
    if board[r][c] > 0:
        return -1
    s = 0
    for y in range(-1, 2):
        for x in range(-1, 2):
            searchr = r
            searchc = c
            n = 0
            if s > 0:
                return s
            while True:
                searchr += y
                searchc += x
                if board[searchr][searchc] <= 0:
                    break
                if board[searchr][searchc] == 3-color:
                    n += 1
                if board[searchr][searchc] == color:
                    s += n
                    break
    return s

def ablecell(color):
    global cell, clk, unable, label
    for r in range(1, size+1):
        for c in range(1, size+1):
            if able(r, c, color) > 0:
                cell += 1
    if cell >= 1:
        label = tk.Label(window, text="そのマスには\n打てません。", font=("MS Gothic", 30))
        label.place(x=950, y=100)
    else:
        label = tk.Label(window, text="打てるマスがないため\nパスとなります。", font=("MS Gothic", 30))
        label.place(x=900, y=100)
        clk += 1
        unable.append(clk)

def judge():
    global label
    b = 0
    w = 0
    for r in range(1, size+1):
        for c in range(1, size+1):
            if board[r][c] == 1:
                b += 1
            elif board[r][c] == 2:
                w += 1
    if b > w:
        label = tk.Label(window, text=str(b)+" 対 "+str(w)+"\n黒石の勝利！", font=("MS Gothic", 30))
        label.place(x=950, y=100)
    elif b < w:
        label = tk.Label(window, text=str(b)+" 対 "+str(w)+"\n白石の勝利！", font=("MS Gothic", 30))
        label.place(x=950, y=100)
    else:
        label = tk.Label(window, text=str(b)+" 対 "+str(w)+"\n引き分け！", font=("MS Gothic", 30))
        label.place(x=950, y=100)

def click(c):
    global clkx, clky, clk, unable, label
    if label != "":
        label.place_forget()
    clkx = int((c.x -25 +4)/100) +1
    clky = int((c.y -25 +4)/100) +1
    if clk%2 == 0:
        if able(clky, clkx, black) > 0:
            board[clky][clkx] = black
            event(clky, clkx, black)
            clk += 1
        else:
            ablecell(black)
    else:
        if able(clky, clkx, white) > 0:
            board[clky][clkx] = white
            event(clky, clkx, white)
            clk += 1
        else:
            ablecell(white)
    piece()
    if len(unable) >= 2:
        for i in range(len(unable)-1):
            if unable[i] == unable[i+1]-1:
                judge()
    if clk == 64:
        judge()
canvas.bind("<Button>", click)

window.mainloop()
