import os
from getch import getch

def triangle(x,y):
    r = 3 # the amount of rows that triangle will have
    k = r - 1 # number of spaces

    # set the cursor at x (filled with line feed)
    print("\n" * x)

    # handle the number of rows
    for i in range(0, r):
        # set cursor at y (filled with spaces)
        for _ in range(0, y + k):
            print(end=" ")
        k = k - 1 # makes the triangle equilateral
        for _ in range(0, i + 1):
            print("* ", end="")
        # ends the line
        print("\r")

def start():
    x,y=0,0
    while True:
        triangle(x,y) #prints the triangle starting on point x,y
        key = ord(getch())
        # key codes are for Linux
        if key == 65: # down
            x += 1
        if key == 66: # up
            x -= 1
        if key == 67: # left
            y += 1
        if key == 68: # right
            y -= 1
        os.system("clear")

if __name__ == "__main__":
    start()
