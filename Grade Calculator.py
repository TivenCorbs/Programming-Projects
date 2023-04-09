

#Consider how many credits ask amount of credit
#functions added to see how many credits the classes and multiply it with the grade they have
#Variables : number of credits for each class, grade the user gets, and total number of credits (dividor)
courses = int(input("How many courses have you taken? \n"))


credit= 0


for x in range(1,courses+1):
    # loops until all courses and grades are input

        
    grades = input("Enter the grades or press q to quit \n")

    

    if grades == "A" or grades == "a":
        credit += float(4.0)

    elif grades == 'B+' or grades == 'b+':
        credit +=float(3.5)

    elif grades == "B" or grades == "b":
        credit+= float(3.0)

    elif grades == "C+" or grades == "c+":
        credit+= float(2.5)

    elif grades == "C" or grades == "c":
        credit+= float(2.0)

    elif grades == "D+" or grades == "d+":
        credit+= float(1.5)

    elif grades == "D" or grades == "d":
        credit+= float(1.0)

    elif grades =="F" or grades == 'f' or grades =='np' or grades =='NP':
        credit+= float(0.0)

    elif grades =='q': #breaks out of loop if you press 'q'(quit)
        break

#try to figure out how to loop if they press wrong thing so it says "Try Again"
    
    


print("Total credit amount\n")
print(credit)




def GPACalculation():

        gpa = float((credit)/courses)
        print("Your GPA is " + str(gpa))

GPACalculation()
        

        

    

    

    

    


    


    

   # i = 0

    #total credits should equal the amount of courses taken and the grades they got
   
    #

    #while(i > 0):

        
        




#(grade * credit)/credit = gpa

    


    



        

    
            
        

        

        

        


    

    














    
    






    







