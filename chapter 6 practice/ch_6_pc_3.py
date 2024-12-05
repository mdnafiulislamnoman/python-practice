Input_string = input("Enter your comment:")

com_1 = "Make a lot of money"
com_2 = "buy now"
com_3 = "subscribe this"
com_4 = "click this"

if com_4 in Input_string or com_3 in Input_string or com_2 in Input_string or com_1 in Input_string:
    print("Spam comment detected")
else:
    print("Comment excepted")