#Take the items in this list of lists: [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]] 
#and write them to a CSV file. The data from each list should be a row in the file, with each item in
#the list separated by a comma.

import csv
with open("C:\\Users\\debor\\OneDrive\\Documents\\SDE Apprentice\\Python\\test.csv", "w") as file:
	write = csv.writer(file, delimiter=",")
	write.writerow(["Top Gun", "Risky Business", "Minority Report"])
	write.writerow(["Titanic", "The Revenant", "Inception"])
	write.writerow(["Training Day", "Man on Fire", "Flight"])