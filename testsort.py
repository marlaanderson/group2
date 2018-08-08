from collections import defaultdict
		
def read():
    infile = open("eng_dict.txt", "r")
    outfile = open("anagramtest.txt", "w")
    table = defaultdict(list)
    for line in infile:			#loops for each individual line in infile
        if len(line) > 8:		#checks if line is greater than 7 characters (8 because of newline character)
            key = "".join(sorted(line.lower().strip()))
		#print("{} {:>25}" .format(key, line.lower().strip()), file=outfile)	#stores results in anagramtest file
            table[key].append(line.lower().strip())
        for keys,values in table.items():
            print(keys, file=outfile)
            print(values, file=outfile)
            print("", file=outfile)
        print(len(table))
			
    infile.close()
    outfile.close()	
	
read()
