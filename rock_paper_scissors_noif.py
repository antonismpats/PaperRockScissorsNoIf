import random

while True:
	print("Make your guess:")
	
	#Ask for the user to create his/her input and lower-case it:
	guess = input()
	guess = guess.lower()
	print("You guessed", guess)
	
	choices = ['rock', 'paper', 'scissors']
	
	#Computer makes a random choice based one the list above
	computer_guess = random.choice(choices)
	print("Computer guessed", computer_guess)

	#Create a dictionary to assign each choice to a value
	guess_dict = {'rock': 0, 'paper': 1, 'scissors': 2}

	#Based on the dictionary assign the choices(keys) to the responding int values 
 	guess_idx = guess_dict.get(guess, 3)
	computer_idx = guess_dict.get(computer_guess)

	#The result is based on this list
	result_matrix = [[0,2,1],
					[1,0,2],
					[2,1,0],
					[3,3,3]]

	#result_idx will be used to determine the result from the result messages
	result_idx = result_matrix[guess_idx][computer_idx]
	result_messages = ["it is a tie", "You win!!! Congrats", 'the computer wins :(', 'invalid guess']
	result = result_messages[result_idx]
	print(result)
	print()