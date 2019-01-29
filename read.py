f=open("irregularVerbs",'r')
irrverbs1={}
irrverbs2={}
for x in f:
	ar=[i for i in x.split()]
	print(ar)
	irrverbs2[ar[2]]=ar[0]
	irrverbs1[ar[1]]=ar[0]
while 1:
	x=input()
	if x in irrverbs1:
		print(irrverbs1[x])
	elif x in irrverbs2:
		print(irrverbs2[x])
	break
compAdj={}
superAdj={}
f=open('degreesAdj','r')
for x in f:
	ar=[i for i in x.split()]
	print(ar)
	compAdj[ar[1]]=ar[0]
	superAdj[ar[2]]=ar[0]
