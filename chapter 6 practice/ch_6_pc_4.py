username = input("Enter your user name:")

length = len(username)

if length < 10:
    print("Yes it contains less than 10 characters")
else:
    print("No it doesn't contains less than 10 characters")