student_grade = []
numOfstudent = 5
passing_grade = 75
passing_count= 0

for i in range (numOfstudent):
     x=int(input(f"Enter grade for student {i + 1}: "))
     if 40 <= x <=100:
         student_grade.append(x)
         if x >= passing_grade:
             passing_count +=1 
     else:
        print("Invalid grade, try again")
        break
else:
    average_grade = sum(student_grade)/numOfstudent
    percentage_passing = (passing_count/numOfstudent)*100
    
    print("Here are the grades:", student_grade)
    print("The average grade is:", average_grade)
    print("The percentage of students who passed is:", percentage_passing)
    print("The number of students who passed is:", passing_count)
    
   