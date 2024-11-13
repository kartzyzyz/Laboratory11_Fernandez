#LAB 11 hehehe
Sports = []

print("Enter different kinds of sports you like")
count = 0
while count <10:
    word = input(f"Sports {count + 1} ")
    Sports.append(word)
    count += 1
    
numofletters = int(input("Enter the number of letters you want to search for: "))

matchingwords = []
for word in word: 
    if len(word) == numofletters:
        matchingwords.append(word)
    
if matchingwords:
    print("The following are the words with", numofletters, "letters:")
    for word in matchingwords:
        print(word)
else:
    print("There are no available words with", numofletters, "letter/s.")
    