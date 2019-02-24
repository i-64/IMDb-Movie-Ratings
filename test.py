myList = []
for n in range(0,100) :
	with open("X:\\SentienceIQ\\aclImdb\\train\\labeledBow.feat") as f:
		#print("path is correct, file opened")
		myLine = ""
		#print(n," ", end='')
		countp = 0
		countn = 0
		x = 0
		sub = " "+str(n)+":"
		for x in range(1,12500) :
			myLine = f.readline()
			if myLine.count(sub) == 1 :
				countn = countn + 1
		#x = 0
		for x in range(12501,25000) :
			myLine = f.readline()
			if myLine.count(sub) == 1 :
				countp = countp + 1
		if (countp+countn) == 0 :
			#print(countp,countn,"infinity")
			myList.append(999)
		else :
			#print(countp,countn,countp/(countp + countn))
			myList.append(countp/(countp + countn))
print(myList)