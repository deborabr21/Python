#Write a program with an infinite loop and a list of numbers. 
#Each time through the loop the program#should ask the user to guess a number or type q to quit.
#If they type q the program should end. Otherwise it should tell them wether or not they successfully
#guessed a number in the list or not.

numbers = [1,3,5,7,9,11,15,18,21,23,34,35,38,41,43,47,49]
n=0
while True:
	print("Type q to quit")
	answer = input("Guess a number between 1 a 50: ")
	if answer == "q":
		break
	if int(answer) in numbers:
		print("Number " + answer + " was found! Congrats!")
		break
	else:
		print("Number " + answer + " was not found!Try again!")
		continue
	n +=1