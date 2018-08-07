#
		
def read():
	infile = open("eng_dict.txt", "r")
	outfile = open("anagramtest.txt", "w")
	for line in infile:			#loops for each individual line in infile
		if len(line) > 8:		#checks if line is greater than 7 characters (8 because of newline character)
			sort = "".join(sorted(line.lower().strip()))
			print("{} {:>25}" .format(sort, line.lower().strip()), file=outfile)	#stores results in anagramtest file
			
	infile.close()
	outfile.close()	
	
read()