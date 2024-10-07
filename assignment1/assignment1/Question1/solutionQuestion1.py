# Name: Austin Meng
# ccid: acmeng1
# studentId: 1801834
# operating system: Windows Os
# python version: python 3.12
import string
def validate_email(email):
    # Add your implementation in here
    extension = {"com","ca","org","net","gov","edu"} # Set of Valid Extensions
    Forbidden = {"scam","spam","fakeemail","trashmail","pleasenotspam","therealtaylorswift","sendmoney"} # These are all the invalid domains
    
    EMAIL = email.split("@")  # Splits the email at the '@' sign
    LOCAL = EMAIL[0] # zero'th index is the local part
    domain = EMAIL[1] # first index is the domain part
    NEWLIST = domain.split(".") # splits the domain at the ".""
    TALLY = 0 # This is to count the number of @ in the list
    INVALID = False

    for i in range(len(email)): # Goes through the list
        if email[i] == "@": 
            TALLY += 1 # Increase the tally by 1
    if len(NEWLIST) == 1:  
        print("Invalid")
    elif TALLY >= 2:
        print("Invalid")
    elif NEWLIST[1] in extension:
        for i in range(len(LOCAL)):
            if  not (LOCAL[i].isalpha() or LOCAL[i].isdigit() or LOCAL[i] == "." or LOCAL[i] == "-"):
                print("Invalid")  
                INVALID = True
                break
        if NEWLIST[0] in Forbidden and INVALID == False:
            print("Forbidden")
        elif INVALID == False:
            print("Valid")
    else:
        print("Invalid")
def main():
    # Takes in the input and stores the email addresses in a list
    emails = list(input().split()) # Splits all the input emails at the space between each email
    # Validate each email here
    for email in emails:
        validate_email(email)

if __name__ == "__main__":
    main()
