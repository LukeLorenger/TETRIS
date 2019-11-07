# Tetris Using Python 3 and Turtle Module

# Import turtle module
import turtle

# Screen for game
wn = turtle.Screen()
wn.title("TETRIS by @iNode.code")
wn.bgcolor("black")
wn.setup(width=600, height=800)
wn.tracer(0) # turns off screen updates


class Shape():
    def __init__(self): # Initializing 
        self.x = 5 # Setting the object at 5 on x axis
        self.y = 0 # Setting the object at 0 on y axis
        self.color = 4

# New List
grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]            
]

# Using turtle object to draw
pen = turtle.Turtle()
pen.penup() # Wont draw lines
pen.speed(0) # 0 for fast animation speed
pen.shape("square") # Shape of pen



# Methods/functions
def draw_grid(pen, grid):
    top = 230
    left = -110

    # List called colors
    colors = ["black", "blue", "lightblue", "orange", "yellow", "green", "purple", "red"]

    # For loop to go through every row in the grid (24 rows down, rows start at 0, )
    for y in range(len(grid)):
        # For loop to go through every row and gather legth of every row, row starts at 0
        for x in range(len(grid[0])):
            screen_x = left + (x * 20) # Each block is 20 pixels wide
            screen_y = top - (y * 20) # Each block is 20 pixels tall
            color_number = grid[y][x] # Goes to this spot
            color = colors[color_number] # Allowing color variable to pull from colors list
            pen.color(color) # The pen will color a color from colors list
            pen.goto(screen_x, screen_y) # Pen go to this spot
            pen.stamp() # Stamps color

# Create the basic shape for the start of the game
shape = Shape()

# put the shape in the grid
grid[shape.y][shape.x] = shape.color

# Draw the initial grid
draw_grid(pen, grid)

# Main game loop
while True:
    wn.update() # Updates the screen

    # Move the shape
    if grid[shape.y + 1][shape.x] == 0:
        grid[shape.y][shape.x] = 0
        shape.y +=1 # Add 1 to y
        grid[shape.y][shape.x] = shape.color
    
    draw_grid(pen, grid)

#wn.mainloop()