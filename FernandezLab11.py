numofstudents = 0
passed = 0
numlist = []

for y in range(5):
    num =int(input("Enter your grade here:"))
    
    if num <= 40 or num >= 101:
        print("Invalid. Number must be between 40 and 100 only")
        break
    else:
        numlist.append(num)
        
    if num>= 75:
        passed += 1
        numofstudents += 1
    else:
        numofstudents += 1
        
    if numofstudents == 5:
        print()
        sumNums = sum(numlist)
        averageGrade = sumNums / 5
        averageGrade = round(averageGrade, 2)
        
        passPercent = (passed / len(numlist)) * 100
        passPercent = round(passPercent,2)
        
        print("Grades entered:" + str(numlist))
        print("Average grade: " + str(averageGrade))
        print("Number of student passed: " + str(passed))
        print("Average of people who passed: " + str(passPercent) +"%" )