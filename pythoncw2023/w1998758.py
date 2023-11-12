# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID- w1998758
# Date- 2022.04.20
#introducing variables
count=1
progress1 = []
trailer1 = []
exclude1 = []
retriever1=[]
num=1
#introducing user defined function
def check_student_id():
    count2=1
    while count2>0:
        student_id = input("Enter your UOW ID: ")
        if   len(student_id) != 8:
            print("Wrong student ID-wxxxxxxx")
        else:
            break


while (num>0):
#creating lists
    progress2=[]
    trailer2=[]
    retriever2=[]
    exclude2=[]

    print("Staff Version With Histogram\n")
    #starting a while loop to run the code unlimited times
    while (count>0):

        #creating a list to append every mark user enters
        marks=[]

        #using try except function to display required message
        check_student_id()
        try:
            credpass=int(input("\nPlease enter your PASS credits:"))    #getting user inputs
            marks.append(credpass)
        except ValueError:
            print("Integer required")
        credpass1=[0,20,40,60,80,100,120]   #creating a list which includes possible marks
        if(credpass not in credpass1):     #comparing user input with created list
            print("out of range")
        try:
            creddef = int(input("Please enter your DEFER credits:"))
            marks.append(creddef)
        except ValueError:
            print("Integer required")
        creddef1 = [0, 20, 40, 60, 80, 100, 120]
        if (creddef not in creddef1):
            print("out of range")
        try:
            credref = int(input("Please enter your FAIL credits:"))
            marks.append(credref)
        except ValueError:
            print("Integer required")
        credref1 = [0, 20, 40, 60, 80, 100, 120]
        if (credref not in credref1):
            print("out of range")

        total=credpass+creddef+credref  #getting the total of the user input credits
        if (total>120):                 #checking if credit total matches the required level
            print("Total invalid")
        elif (credpass==120):          #grading students according to the credit levels
            print("Progress")
            progress1.append("*")     #appending a * to the lists according to the gradings
            progress2.append(marks)   #appending marks to a list according to the gradings


        elif (credpass<=120 and credpass>=100):
            print("Progress(module trailer)")
            trailer1.append("*")
            trailer2.append(marks)



        elif (credref<=120 and credref>=80):
            print("Exclude")
            exclude1.append("*")
            exclude2.append(marks)



        else:
            print("Do not progress- module retriever")
            retriever1.append("*")
            retriever2.append(marks)



       #rerunning the loop
        print("\nWould you like to enter another set of data?")
        answer=input("If yes enter y if not enter q:")
        if (answer=="q"):
            break
        elif (answer=="y"):
            continue
    p1 = len(progress1)
    p2 = len(trailer1)
    p3 = len(exclude1)
    p4 = len(retriever1)
    print("-"*80)
    #creating a horizontal histogram using the lists created before
    print("\nHorizontal Histogram")
    print("\nProgress ",p1,"=",*progress1)
    print("Trailer",p2,"=",*trailer1)
    print("Excluded",p3,"=",*exclude1)
    print("Module retriever",p4,"=",*retriever1)
    print("-"*80)


    #getting the number of outcomes using the length of lists created
    total2=p1+p2+p3+p4
    print('\n',total2,'outcomes in total')


    #displaying the marks of students according to gradings
    print("\nProgress - ",*progress2)
    print("Progress (Module Trailer) -",*trailer2)
    print("Module Retriever - ",*retriever2)
    print("Exclude - ",*exclude2,'\n')


    #creating and appending marks of students according to gradings to a text file
    with open ('progression_data.txt','w') as file:
        for item in progress2:
            file.write('progress -'+str(item)+'\n')
    with open ('progression_data.txt','a') as file:
        for item in trailer2:
            file.write('Progress (module trailer) - '+str(item)+'\n')
    with open ('progression_data.txt','a') as file:
        for item in retriever2:
            file.write('Module retriever -'+str(item)+'\n')
    with open ('progression_data.txt','a') as file:
        for item in exclude2:
            file.write('Exclude - '+str(item)+'\n')
    with open ('progression_data.txt','r') as  file:
        for line in file:
            print(line)

    break



