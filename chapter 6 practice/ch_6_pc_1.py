num_1 = int(input("Enter number 1:"))
num_2 = int(input("Enter number 2:"))
num_3 = int(input("Enter number 3:"))
num_4 = int(input("Enter number 4:"))

if num_1 > num_2 and num_1 > num_3 and num_1 > num_4:
    print("Greatest number is:",num_1)
elif num_2 > num_1 and num_2 > num_3 and num_2 > num_4:
    print("Greatest number is:",num_2)
elif num_3 > num_1 and num_3 > num_2 and num_3 > num_4:
    print("Greatest number is:",num_3)
elif num_4 > num_1 and num_4 > num_3 and num_4 > num_2:
    print("Greatest number is:",num_4)
else: print("Numbers are equal")