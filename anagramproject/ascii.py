#ascii
keylist = ["bbb", "abc", "ccc", "bcd", "bb"]
numlist = []

def ascii_ordering(keylist, numlist):
	for key in keylist:
		letterlist = list(key)

		sum = 0
		for a in letterlist:
			sum+=ord(a)
		numlist.append(sum)

	keylist = [keylist for _,keylist in sorted(zip(numlist,keylist))]

	for z in keylist:
		print(z)

ascii_ordering(keylist, numlist)