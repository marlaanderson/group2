#returns the reverse of a string
def reverse(s):
    return s[::-1]
 
def palindrome(s):
    #calls reverse function
    srev = reverse(s)
 
    #checks if strings are equal to each other
    if (s == srev):
        print ("True")
    else: 
    	print ("False")
palindrome("racecar")
 

