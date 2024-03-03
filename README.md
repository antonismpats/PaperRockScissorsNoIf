# PaperRockScissorsNoIf
This is a mini-project, visualising the classic paper rock scissors games, but without using any If statements. I used Sublime Code to run the code, which had serious issues with the 'input' method, so I had to download and install a new SublimeREPL to run the code properly. Sublime Text sometimes faces issues with the input() function due to the way it interacts with the console. Using a REPL environment like Sublime REPL or running the script directly in a terminal or command prompt should work well for taking user input. How to setup REPL in Sublime (https://www.youtube.com/watch?v=gEFBBuyiRMU). Run the code by going to Tools->SublimeREPL->Python-> Python - RUN current file 

## Description:

### Game Flow

The game uses a while True loop, ensuring that the game continues indefinitely until manually interrupted.
User input is obtained for their guess (rock, paper, or scissors) and converted to lowercase for case-insensitive comparison.

### Computer's Choice:

The computer randomly selects its choice from the predefined options: rock, paper, or scissors.

### Result Calculation:

A dictionary (guess_dict) is used to map user and computer choices to integer values (0, 1, 2).
A 2D matrix (result_matrix) defines the outcomes of the game based on the numeric values of choices.
The result index is determined from the matrix, and the corresponding result message is selected.
### Result Display:

The game prints out the user's and computer's choices, the result of the round, and a newline for clarity.
Results include messages for a tie, user win, computer win, and an invalid guess.

### Reusability:

The code is concise and can serve as a simple rock-paper-scissors game template.

