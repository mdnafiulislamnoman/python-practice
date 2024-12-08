l = ["Harry", "Soham", "Sachin", "Rahul"]

for i in l:
    if i[0] != "S":
        continue
    else:
        print(f"Hello {i}")