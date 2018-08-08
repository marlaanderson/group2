#Kevin Ramirez

from collections import defaultdict
		
def read():
	infile = open("eng_dict.txt", "r")
	outfile = open("anagramtest.txt", "w")
	anagram_permute(infile, outfile)
	infile.close()
	outfile.close()

def anagram_permute(infile, outfile):
	table = defaultdict(list)
	c = 0
	for line in infile:			#loops for each individual line in infile
		c+=1
		if len(line) > 8:		#checks if line is greater than 7 characters (8 because of newline character)
			key = "".join(sorted(line.lower().strip()))
			table[key].append(line.lower().strip())

	keylist = list(table.keys())
	keylist.sort(key=len)
	count = 0
	for key in keylist:
		if len(table[key]) > 1:
			count+=1
			print("{}: {}".format(key, ", ".join(table[key])), file=outfile)
	
	print("\nAMOUNT OF WORDS:", count, file=outfile)
	
read()