#Take the list ["The", "fox", "jumped", "over", "the", "fence", "."] and turn it into the string 
#"The fox jumped over the fence ." (Don't forget, you learned a method that turns a list of 
#strings into a single string.) Note, there should be a blank space between the final "e" and 
#the period at the end. Make sure to print your new string. 

list = ["The", "fox", "jumped", "over", "the", "fence", "."]
newList = " ".join(list)
print(newList)