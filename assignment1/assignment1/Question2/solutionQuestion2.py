# Name: Austin Meng
# ccid: acmeng1
# studentId: 1801834
# operating system: Windows
# python version: 3.12.5

#Input: The given input string
#Output: The "clean" version of the input string without characters specified in the problem statement like ?, !, etc
def clean_input_string(string):
    #Add your implementation here
    Special_symbol = {".", ",", "!", "?","'"} # These are the symbols that
    STR = []
    NEWSTRING = list(string)
    for i in range(len(NEWSTRING)):
        if not (NEWSTRING[i] in Special_symbol):
            STR.append(NEWSTRING[i])
    JOINEDSTR = ''.join(STR)
    return JOINEDSTR
#Input: The output from clean_input_string()
#Output: The reversed version of the input string
def reverse_string(string):
    LIST = string.split(" ")
    REVSTR = LIST[::-1]
    REVJOIN = " ".join(REVSTR)
    return REVJOIN

#Input: The output from reverse_string()
#Output: A string with all the duplicate occurrences of words removed. Only the first occurrence will remain in the string
def remove_duplicates(revstr):
    #Add your implementation here
    STRLIST = revstr.split(" ")
    NEWLIST = []
    for item in STRLIST:
        if item not in NEWLIST:
            NEWLIST.append(item)
    DUPSTR = " ".join(NEWLIST)

    return DUPSTR

#Input: The output from remove_duplicates()
#Output: The median length of the words in the input string. This function must return an integer, more specifically the floor value.
def calculate_median_length(string):
    STRING = string.split(" ")
    LENGTH = []
    for i in range(len(STRING)):
        LENGTH.append(len(STRING[i]))
    LENGTH.sort()
    if len(LENGTH) % 2 == 0:
        MID = int(len(LENGTH)//2)
        return (LENGTH[MID])
    else:
        MID = int(len(LENGTH)//2)
        return (LENGTH[MID])
def main():
    inputString = input()
    reversedString = clean_input_string(inputString)

    reversedStringDUP = reverse_string(reversedString)
    print(reversedStringDUP)
    reversedStringWithoutDuplicates = remove_duplicates(reversedStringDUP)
    print(reversedStringWithoutDuplicates)

    medianWordLength = calculate_median_length(reversedStringWithoutDuplicates)
    print(medianWordLength)
if __name__ == "__main__":
    main()

