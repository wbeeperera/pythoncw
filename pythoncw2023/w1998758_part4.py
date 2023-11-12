#introducing variables
count=1
progress1 = []
trailer1 = []
exclude1 = []
retriever1=[]
num=1
mydictionary={}
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

    print("Staff Version With Histogram")
    #starting a while loop to run the code unlimited times
    while (count>0):

        #creating a list to append every mark user enters
        marks=[]

        #using try except function to display required message
        uow_num=check_student_id()
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
            progress2.append(marks)   #appending marks to a list according to the gradings
            mydictionary[uow_num]='progress-',marks

        elif (credpass<=120 and credpass>=100):
            print("Progress(module trailer)")
            trailer2.append(marks)
            mydictionary[uow_num] = 'progress(module trailer)',marks


        elif (credref<=120 and credref>=80):
            print("Exclude")
            exclude2.append(marks)
            mydictionary[uow_num] = 'Exclude - ',marks


        else:
            print("Do not progress- module retriever")
            retriever2.append(marks)
            mydictionary[uow_num] = 'Do not progress- module retriever-',marks


       #rerunning the loop
        print("\nWould you like to enter another set of data?")
        answer=input("If yes enter y if not enter q:")
        if (answer=="q"):
            break
        elif (answer=="y"):
            continue






    for key,value in mydictionary.items():
        print(key,value,sep=':')

    break



