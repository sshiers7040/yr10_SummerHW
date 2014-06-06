'''
Repeatable for use with different numbers
number is the number that the timestable is of.
upTo is the highest multiplication of number that you want to see.'''
def displayTimestable(number, upTo):
    for x in range(1, upTo + 1):
        print("{0} X {1} is {2}".format(x, number, x * number))

#The code is contained within a function to make it easy to call the whole program and
#the timestsble function sperately
def main():
    while True: #Looped so that they can see multiple timestables if they want to
        selecting = True #Used for validation
        while selecting: #This code will loop until a valid number is given by the user
            number = input("\nEnter an integer that you want to see the timestable of: ")
            if number.isdigit(): #Returns True if the value in the sstring can be converted into an int
                selecting = False #If it can be an int, then stop the loop
            else:
                print("\nThat is not an integer!") #

        selecting = True #Reset for more validation
        while selecting: #Validation for the highest mutiplication that they want to see
            upTo = input("\nEnter how many multiplications (an integer) you want to see up to: ")
            if upTo.isdigit():
                selecting = False
            else:
                print("\nThat is not an integer!")
                
        print() #Adds a blank line to make the timestables seperate from the previous print
        displayTimestable(int(number), int(upTo)) #Contained in a function. int() converts to ints.

        selecting = True #Reset for more validation
        while selecting: #If they want to see another timestable
            choice = input("\nDo you want to see another timestable (Enter Y for yes or N for no)?: ")
            if choice.upper() == "N":
                return
            elif choice.upper() == "Y":
                selecting = False
            else:
                print("\nThat input is not understood!")

main()
