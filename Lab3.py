import random

sequence = []
sequence_length = 4
max_turn = 12
lowest_guess = 1
highest_guess = 6

for i in range(sequence_length):
	i = str(random.randint(lowest_guess,highest_guess))
	sequence.append(i)
#print(sequence)

turn_count = 1
while turn_count < (max_turn + 1):
	guess = []
	output = []
	while len(guess) != sequence_length:
		print(f"Guess a sequence of {sequence_length} values from {lowest_guess}-{highest_guess}")
		guess = list(input(f'guess {turn_count} of {max_turn}: '))
		guess = [x for x in guess if x.isdigit() and int(x) in range(lowest_guess,highest_guess+1)]
		#print(guess)
		sequence_copy = sequence[:]
		guess_copy = guess[:]
		if len(guess_copy) != sequence_length: print("Invalid guess")
	for i in range(sequence_length):
		if guess_copy[i] == sequence_copy[i]:
			guess_copy[i] = "Match"
			sequence_copy[i] = "Match"
			output.append("\u25CF")
			#output.append("a")
			#print(guess_copy)
	for i in range(sequence_length):
		for j in range(sequence_length):
			if (guess_copy[i] == sequence_copy[j]) and (guess_copy[i] != "Match"):
				output.append("\u25CB")
				#output.append("b")
				break

	print(''.join(output),"\n")
	
	if guess == sequence:
		print("Correct - you win!")
		break

	turn_count = turn_count + 1
	if turn_count > max_turn:
		print(f"Sorry! The code was {''.join(sequence)}")