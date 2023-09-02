number_of_students = int(input('\n'"Enter number of students:"))                           #this is the total number of students in class.
def records():                                                                         #this will contain the details of each student.
   for i in range(number_of_students):
      global name
      name = str(input('\n'"name:"))
      
      for k in range(1):                                                               # all the while loops used in this for loop is to weight the 3 components.
         while True:
            global assignment
            assignment = float(input('\n'"assignment score:"))
            if assignment > 10:
               print('\n'"Assignment score should be less than or equal to Ten!")
               continue
            if assignment <=10: pass
            break
         while True:
            global quiz
            quiz = float(input('\n'"quiz score:"))
            if quiz > 20:
               print('\n'"quiz score should be less than or equal to 20")
               continue
            elif quiz <=20: pass
            break
         while True:
            global exams
            exams= float(input('\n'"exams score:"))
            if exams > 70: 
               print('\n'"exams score should be less than or equal to 70"'\n')
               continue
            elif exams <= 70: pass
            break         
            
         total = assignment + quiz + exams                                               # this for loop is to weight the total of the 3 components
         for j in range(1):
            global finalGrade
            if total <= 100 and total >=95:  
               finalGrade = "A+"
            elif total <=89 and total >=85:
               finalGrade = "A"
            elif total <= 84 and total >=80:
               finalGrade = "B+"
            elif total <=79 and total >= 75:
               finalGrade = "B"
            elif total <=74 and total >= 65:
               finalGrade = "C+"
            elif total <=64 and total >=55:
               finalGrade = "C"
            elif total <=54 and total >=45:
               finalGrade = "D"
            elif total <= 45 and total >=1:
               finalGrade = "F"
            else:
               print("Invalid Inputs")
records()    
   

Student_details = {"Name":"{}".format(name),"Assignment":"{}".format(assignment),"Quiz":"{}".format(quiz),"Exams":"{}".format(exams),"Final Grade":"{}".format(finalGrade)}
results = ""
for key,value in Student_details.items():
   results += f"{key}: {value}\n"
print(results)
      