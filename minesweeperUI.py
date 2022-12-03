# tk inter
import tkinter as tk

root = tk.Tk()
root.title("Minesweeper")
root.geometry("400x400")

# creating a button
height = 9
width = 9

def calling(x,y):
    print((x,y))

# create a button
def create_button(x,y):
    button = tk.Button(root, text=" ")
    button.grid(row=x, column=y)

    # when button is clicked change text to position
    button.bind("<Button>", lambda event: button.config(calling(x,y)))

# create a all buttons in grid
for i in range(height): #Rows
    for j in range(width): #Columns
        create_button(i,j)

root.mainloop()
