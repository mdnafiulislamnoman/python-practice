#Taking input of a string
string = input("Enter a string:")

#Finding double space
double_space = string.find("  ")

#printing the result
if double_space >0:
    print("double space detected")