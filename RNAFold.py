#!/usr/bin/python
def match(a,b):
	if a in 'AU':
		if b in 'AU' and b!=a:
			return 1
		else:
			return 0
	else:
		if b in 'CG' and b!=a:
			return 1
		else:
			return 0


def outputlist(list):
	for i in list:
		print i


def comp(i,dif,table,a,pair):
	comp1=find1(i,dif,table,a)
	comp2=find2(i,dif,table,a)
	
	if comp1[0]>comp2[0]:
		pair1(i,dif,pair,comp1[1])
	if comp1[0]<comp2[0]:
		pair2(i,dif,pair,comp2[1])
	if comp1[0]==comp2[0]:
		pair3(i,dif,pair,comp1[1],comp2[1])
		
	return max(comp1[0],comp2[0])


def find1(i,dif,table,a):
	bepair=match(a[i],a[i+dif])
	midpair=table[i+1][i+dif-1]
	return bepair+midpair,bepair


def pair1(i,dif,pair,comp1pair):
	pair[i][i+dif]=[]
	if comp1pair==1:
		for element in pair[i+1][i+dif-1]:
			pair[i][i+dif].append(element+[[i,i+dif]])


def find2(i,dif,table,a):
	maximum=0
	klist=[]
	for count in range(0,dif):
		k=i+count
		plus=table[i][k]+table[k+1][i+dif]
		if plus>maximum:
			klist=[k]
		if plus==maximum:
			klist.append(k)
		maximum=max(maximum,plus)
	return maximum,klist


def pair2(i,dif,pair,comp2list):
	pair[i][i+dif]=[]
	for k in comp2list:
		temp1=[]
		temp2=[]
		for firsthalf in pair[i][k]:
			for secondhalf in pair[k+1][i+dif]:
				pair[i][i+dif].append(firsthalf+secondhalf)


def pair3(i,dif,pair,comp1pair,comp2list):
	pair1(i,dif,pair,comp1pair)
	temp1=[]+pair[i][i+dif]
	pair2(i,dif,pair,comp2list)
	temp2=[]+pair[i][i+dif]
	pair[i][i+dif]=temp1+temp2


def map(a,b):
	length=len(a)
	smallestdif=int(b)
	table=[[0 for i in range(length)] for i in range(length)]
	pair=[[[[] for i in range(1)] for i in range(length)] for i in range(length)]
	
	for dif in range(smallestdif,length):
		for i in range(0,length-dif):
			table[i][i+dif]=comp(i,dif,table,a,pair)
			
	outputlist(table)
	
	print ""*2
	print "The total number of pairs in RNA chain : "
	print table[0][length-1]
	print ""*2
	print "The number of RNA pairing possibilities: "
	print len(pair[0][length-1])
	print ""*2
	print "The RNA pairing possibilities: "
	outputlist(pair[0][length-1])
	print ""*2
	print "Thanks for your kind consideration! Have a great day!"
	print ""*2


a=raw_input('Please input RNA (capital words): ')
b=raw_input('Input the smallest pair spacing : ')
print ''*2
print "The N-S algorithm table to search RNA pairing: "
map(a,b)
