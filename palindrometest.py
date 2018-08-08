from collections import defaultdict

#returns the reverse of a string
def reverse(s):
    return s[::-1]
 
def palindrome(s):
    #calls reverse function
    srev = reverse(s)
 
    #checks if strings are equal to each other
    if (s == srev):
        return True
    else: 
    	return False

def main():
    infile = open("eng_dict.txt", "r")
    for line in infile:
        line = line.strip()
        if palindrome(line) == True:
            return line
main()