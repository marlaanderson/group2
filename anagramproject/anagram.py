#Kevin Ramirez

from collections import defaultdict				#Imports defaultdict: It overrides one method and adds one writable instance variable. The rest of its properties are the same as dict.

table = defaultdict(list)						#Creates a defaultdict with lists as values.

def read():
	infile = open("eng_dict.txt", "r")			#Open dictionary to analyze.
	outfile = open("anagramtest.txt", "w")		#Open new file to write outcome to.
	anagram_permute(infile, outfile, table)		#Runs anagram creation.
	infile.close()
	outfile.close()

def anagram_permute(infile, outfile, table):
	no_dupes = list(sorted(set(infile.read().lower().strip().split())))				#Creates a new list identical to eng_dict except every element is unique and lowercase.
																					#Words like cardigan were counted double because uppercase and lowercase version were counted as anagrams of each other.

	for line in no_dupes:															#Loops for each individual element in no_dupes.
		if len(line) > 7:															#Checks if line is greater than 7 characters.
			key = "".join(sorted(line))												#Creates a key out of the alphabetized lowercased letters of each word and strips the newline characters.
			table[key].append(line)													#A new element will then be added to the value list of the specific key being called.

	keylist = list(table.keys())													#Creates a list of the keys.
	keylist.sort(key=len)															#Sorts key list by key length.
	keylist = sorted(keylist, key=lambda x: len(table[x]))							#Sorts key list by length of value list (amount of anagrams).

	count = 0																		#Initializes count variable
	for key in keylist:																#Iterates throught the entire list.
		if len(table[key]) > 1:														#Will only print if there is atleast an anagram pair.
			count+=1																#Keeps track of how many keys there are are in total which have atleast an anagram pair.
			print("{:<25}| {}".format(key, ", ".join(table[key])), file=outfile)	#Prints out key and the list of anagrams associated with that key.

	print("\nAMOUNT OF ALPHABETIZED WORDS:", count, file=outfile)					#Prints Final tally of anagram families.

read()
