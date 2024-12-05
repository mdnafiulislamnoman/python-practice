sub_1 = int(input("Enter number of subject 1:"))
sub_2 = int(input("Enter number of subject 2:"))
sub_3 = int(input("Enter number of subject 3:"))

total_percentage = sub_1+sub_2+sub_3

if sub_1>33 and sub_2>33 and sub_3>33 and total_percentage>40:
    print("Passed")
else:
    print("failed")