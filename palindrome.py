def palindromes():
    infile = open("eng_dict.txt", "r")
    for line in infile:
            line=line.strip()    
            #if len(line) >7: #will not work because there are no palindroms greater than 7 characters
            if line==line[::-1]:  # reverses and tests in one step
                print(line)
palindromes()