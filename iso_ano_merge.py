from collections import defaultdict

table = defaultdict(list)

def iso_ano_merge():
						#Creates a defaultdict with lists as values.	
    infile = open("eng_dict.txt", "r")			#Open dictionary to analyze.
    outfile = open("anagramtest.txt", "w")
    outfile2 = open("isogramtest.txt","w")
    anagram_permute(infile, outfile, table)		#Runs anagram creation.
    isograms(outfile2)
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
	
    print("\nThere are this many anagrams:", count, file=outfile)					#Prints Final tally of anagram families.
def isograms(outfile2): 
    count = 0
    for line in outfile2:
        line = line.lower().strip()
        if len(set(line)) == len(line):
            count+=1
            print("There are %s isograms!"%(line))
    print(count)
iso_ano_merge()
