"""Making a dictionary of Bangla words with values as their English
translation"""
dictionary = {
    "Ami" : "Me",
    "Tumi" : "You",
    "Tara" : "They",
    "Amader" : "Our",
    "tader" : "Their"
}

#Option for users to look it up
word = input("Enter the word you are looking for:")

print(dictionary[word])