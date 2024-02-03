# **Python Assignment**
## Objectives:
- Introduction to Object Oriented Programming
- Hands on experience at game development using pygame.
- Introduction of some new python libraries

## **Marks Directory**
### Features:
- Maintaining marks directory for faculty use
- Creating database and storing for future use
- Importing data into the code for modification through csv file
- Flexibility of addition, removal and editing of enteries
- Storing the modified database

### Setup
- Clone this directory
- Run `pip install prettytables` to install necessary module
- Run `python3 mdirectory`

### Input
- A menu based approach has been used
- Each command has particular option as displayed in menu. Input the option to run the command
- Chose the option displayed and input required data to proceed

### Output
- The result will be displayed on the terminal itself.
- For edition and removal direct continue option will be shown on success

### Assumptions
- Input of parameters  for search,edit and removal will have attribute type and value without space just comma separted and each parameter space separtef.
For eg `FirstName,Rajat Lastname,Garg`
- Each key is case sensitive
- Field heading of csv file should be same as key
- Each search query joins all parameters and display only intersection

## **Position-Distance Map**
### Features
- The standard problem of direction sense test can be visualized through this progaram
- The program offers option to view trajectory of person based on the location
- We can also find relative position of person from the starting position
- Total distance keeps on updating as the person moves and can be viewed through terminal

### Setup
- Clone this directory
- Run `pip install matplotlib`
- Run `python3 map.py`

### Input
- A menu based approach has been used
- Each command has particular option as displayed in menu. Input the option to run the command
- Chose the option displayed and input required data to proceed
- The input for next location should be magnitude. units and direction each space separted with unique code for direction
- Do close the graph of movement to proceed further

### Output
- The result will be displayed on terminal itself
- The graph will be popped up on screen.

### Assumptions
- The input for location follows fixed format. For eg. 3 cm N
- Units can be cm (centi-meter) or mm (mili-meter)
- Location would be based on eight axes in direction
- The person always starts from origin
- The total distance is in centi-meter

## **"Kaooa" Board Game**
### Features
- The game interface include following:
    - A **board** with **star** embeded on it. Each **circle** on star represents **position**
    - A **Vulture** represented by **yellow** color
    - A **crow** represented by **sea green** color
- The game is designed for Human v/s Human
- The rules of game are simple:
    - The crow can be at max 7 on the board where as the vulture is only 1
    - The crow's objective is to block the vulture
    - The vulture's objective is to eat atleast 4 crows
    - First to fulfill objective wins the game
    - The movement allowed is only adjacent circle but in vulture case is second position is unoccupied in straight line and crow is at first then he jumps to eat crow.
- Opponent 1 is by deafut Crow as the first to play the move on start of game
- Opponent 2 is vulture

### Setup
- Clone this directory
- Run `pip install pygame`
- Run `python3 kaooa.py`

### Input
- Clicking on empty circles insert the piece
- For any valid movement one has to drag the piece from current ot desired position wihtout lifting mouse click
- For any invalid movement the piece stays there only

### Output
- As any of the Opponent fulfill thier objective, he/she is declared winner
- The interface closes after a few seconds

### Assumptions
- The time complexity of check algorithm has not taken under consideration due to small value of n
- The first turn is of crow according to rules of game
- Most of the movement error has been taken care of, but kindly requested to ignore if any
- Dragging should be wihtout mouse click lift and it should be dropped anywhere in the desired position (area of circle)
- The game automatically closes after few seconds on completion
