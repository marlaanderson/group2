#Kevin Ramirez
from collections import defaultdict									#Imports defaultdict: It overrides one method and adds one writable instance variable. The rest of its properties are the same as dict.

table = defaultdict(list)											#Creates a defaultdict with lists as values.

def main():
	infile = open("eng_dict.txt", "r")								#Open dictionary to analyze.
	outfile = open("anagramtest.txt", "w")							#Creates anagram document to export anagram data to.
	outfile2 = open("isogramtest.txt", "w")							#Creates isogram document to export all isogramic anagrams to.
	outfile3 = open("asciitest.txt", "w")							#Creates ascii document to export all anagrams families which share ascii summed values.

	anagramkeylist = anagram_permute(infile, outfile, table)		#Runs anagram creation.
	isograms(anagramkeylist, outfile2)								#Filters for all isogramic anagrams.
	ascii(anagramkeylist, outfile3)									#Filters for all anagrams related by ascii sum of each word.

	infile.close()													#Closes all Files.
	outfile.close()
	outfile2.close()
	outfile3.close()

def anagram_permute(infile, outfile, table):
	no_dupes = list(sorted(set(infile.read().lower().strip().split())))				#Creates a new list identical to eng_dict except every element is unique, lowercase, and stripped of newline characters.
																					#Words like cardigan were counted double because uppercase and lowercase version were counted as anagrams of each other.
	for line in no_dupes:															#Loops for each individual element in no_dupes.
		if len(line) > 7:															#Checks if line is greater than 7 characters.
			key = "".join(sorted(line))												#Creates a key out of the alphabetized lowercased letters of each word.
			table[key].append(line)													#A new element will then be added to the value list of the specific key being called.

	keylist = list(table.keys())													#Creates a list of the keys.
	keylist.sort(key=len)															#Sorts key list by key length.
	keylist = sorted(keylist, key=lambda x: len(table[x]))							#Sorts key list by length of value list (amount of anagrams).
	anagramkeylist = []																#Initializes a new list that excludes all keys which do not have atleast an anagram pair.
	count = 0																		#Initializes count variable
	for key in keylist:																#Iterates throught the entire list based on the keylists new order.
		if len(table[key]) > 1:														#Will only print if there is atleast an anagram pair.
			anagramkeylist.append(key)												#Appends keys with atleast an anagram pair to the anagramkeylist.
			count+=1																#Keeps track of how many keys there are are in total which have atleast an anagram pair.
			print("{:<25}| {}".format(key, ", ".join(table[key])), file=outfile)	#Prints out key and the list of anagrams associated with that key.	
	print("\nAMOUNT OF ANAGRAM FAMILIES:", count, file=outfile)						#Prints Final tally of anagram families. 
	return anagramkeylist															#Returns keylist so it can be used again when filtering for isograms and ascii functions.

def isograms(anagramkeylist, outfile2):
	count = 0																		#Reuses count variable to keep track for Final tally of isogramic anagram families.
	for key in anagramkeylist:														#Iterates throught the entire list based on the anagramlists new order.
		if len(set(key)) == len(key):												#Will only print anagram families whose key word's letters are unique (has no repeated letters).
			count+=1
			print("{:<25}| {}".format(key, ", ".join(table[key])), file=outfile2)	
	print("\nAMOUNT OF ISOGRAMIC ANAGRAM FAMILIES:", count, file=outfile2)

def ascii(anagramkeylist, outfile3):														
	numlist = []																	#Initializes number list which will be associated to ascii values of each key word.
	for key in anagramkeylist:														#Loops through every word in anagramkeylist and seperates each word into a list of its letters.
		letterlist = list(key)

		sum = 0
		for a in letterlist:														#For each newly created list of letters the letters are pulled in 1 by 1 and converted into ascii numeric values.
			sum+=ord(a)																#These values are then summed up and appended to the numlist.
		numlist.append(sum)

	anagramkeylist = [anagramkeylist for _,anagramkeylist in sorted(zip(numlist,anagramkeylist))]			#Orders the anagramkeylist by using the sorted version of the numlist (all keys will by order by the words numeric value).

	count = 0
	for key, i in zip(anagramkeylist, range(1, len(numlist))):												#Iterates by key and number (for index use) simultaneously.
		print("{}: {:<25}| {}".format(sorted(numlist)[i-1], key, ", ".join(table[key])), file=outfile3)		#Prints numeric value of key, the key itself, and all the anagrams associated with that key.
		if sorted(numlist)[i-1] != sorted(numlist)[i]:														#If the numeric value of the current indexed key is not equal to the previous key's numeric value a space is inserted creating groups. 
			count+=1																						#Counter also records when a grouping is made.
			print("", file=outfile3)
	print("AMOUNT OF ASCII RELATED ANAGRAMS:", count, file=outfile3)										#Amount of anagrams sorted into numerical group is printed at the end.


main()