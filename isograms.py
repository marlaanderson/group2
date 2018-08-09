def isograms():
    infile = open("eng_dict.txt", "r")
    count = 0
    for line in infile:
        line = line.lower().strip() #makes string lower case and strips it 
        if len(line) > 7:
            if len(set(line)) == len(line): #checks if the length of the set of line is equal to the length of line
                count+=1
                print(line)
    print("There are %s isograms!"%(count))
isograms()
