def isograms():
<<<<<<< HEAD
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
=======
    infile = open("/Users/Marla/Desktop/CAAP-CS/final_project/group2/eng_dict.txt", "r")
    count = 0
    for line in infile:
        line = line.lower().strip()
        if len(line) > 8:
            if len(set(line)) == len(line):
                count+=1
                print("There are %s isograms!"%(line))
    print(count)
isograms()
>>>>>>> d0cbd453967965f8bbf9c853e0a71e4e70be9c87
