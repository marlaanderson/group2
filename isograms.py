def isograms():
    infile = open("eng_dict.txt", "r")
    count = 0
    for line in infile:
        line = line.lower().strip()
        if len(line) > 7:
            if len(set(line)) == len(line):
                count+=1
                print(line)
    print("There are %s isograms!"%(count))
isograms()
