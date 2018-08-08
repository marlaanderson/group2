def symmetry():
    infile = open("eng_dict.txt", "r")
    horizontals = {"B","C","D","E","H","I","K","O","X"}
    count = 0
    for line in infile:
        line = line.upper().strip()
        if len(line) > 7:
            letters = list(line)
            if set(letters).issubset(horizontals):
                print (line)
symmetry()

'''
#By changing the letters, you can search for different types of words. Fo instance, words that can be played on a piano: 
def musical_notes():
    infile = open("eng_dict.txt", "r")
    horizontals = {"A","B","C","D","E","F","G"}
    count = 0
    for line in infile:
        line = line.upper().strip()
        if len(line) > 7:
            letters = list(line)
            if set(letters).issubset(horizontals):
                print (line)
musical_notes()
'''
