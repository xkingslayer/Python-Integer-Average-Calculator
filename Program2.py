#***************************************************************
#
#  Developer:         Dane A. Knudsen
#
#  Program #:         Program 2
#
#  File Name:         Program2.py
#
#  Course:            COSC 1336 Programming Fundamentals I 
#
#  Due Date:          Feburary 14, 2020
#
#  Instructor:        Fred Kumi 
#
#  Chapter:           Chapter 1-2
#
#  Description:
#     Gets five integer test  scores from  the  user,
#     calculates their average, and prints it on the screen.
#
#***************************************************************

#***************************************************************
#
#  Function:     main
# 
#  Description:  The main function of the program
#
#  Parameters:   None
#
#  Returns:      Nothing 
#
#**************************************************************
def main():
    
    developerInfo()
    
    score1 = int(input("Enter Score 1: ")) 
    score2 = int(input("Enter Score 2: "))
    score3 = int(input("Enter Score 3: "))
    score4 = int(input("Enter Score 4: "))
    score5 = int(input("Enter Score 5: "))

    avgScore = (score1 + score2 + score3 + score4 + score5)/5

    print("You scored an average of:",avgScore)

    if avgScore > int(70):
        print("You passed, good job!")
    else:
        print("You can do better!") 
   

    

    
    # End of the main function 
    
#***************************************************************
#
#  Function:     developerInfo
# 
#  Description:  Prints Programmer's information
#
#  Parameters:   None
#
#  Returns:      Nothing 
#
#**************************************************************
def developerInfo():
    print('Name:     Dane A. Knudsen')
    print('Course:   Programming Fundamentals I')
    print('Program:  One')
    print()
    # End of the developerInfo function

# Call the main function
main()

# End of Program 1

