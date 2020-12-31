#Write a program that asks the user to type a number, convert it to integer and print it.
#If you can't conert their input to an integer, print a message that says "Please type an integer"

answer = input("Type a number: ")
try:
    int(answer)
    print(answer)
except:
    print("Please type an integer")




