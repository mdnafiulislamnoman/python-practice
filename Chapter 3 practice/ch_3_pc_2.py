#Taking input of name
Name = input("Enter the name:")

#Taking input of date
Date = input("Enter the date:")

#Letter body
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

#Replacing place holder with values
filled_letter= letter.replace("<|Name|>",Name).replace("<|Date|>",Date)

print(filled_letter)