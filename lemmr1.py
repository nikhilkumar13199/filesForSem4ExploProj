import re



def cons(s,i):
    if re.match('[aeiou]',s[i]):
        return False
    if re.match('y',s[i]):
        if i==0:
            return True
        else:
            return (not cons(s,i-1))
    return True

#This function return the measure of word or word part, (C)(VC)^m(C)
def m(s):
    m = 0
    for i in range(0, len(s) - 1):
        if (not cons(s, i)) and cons(s, i + 1):
            m += 1
    return m


#loading various databases
base={'mice':'mouse','is':'be'}
exceps={'NNP':['gasses','fezzes','fuzzes']}
same={'NNP':['sheep','hair','species','deer','series']}
f=open("irregularVerbs",'r')
irrverbs1={}
irrverbs2={}
for x in f:
	ar=[i for i in x.split()]
	# print(ar)
	irrverbs2[ar[2]]=ar[0]
	irrverbs1[ar[1]]=ar[0]
compAdj={}
superAdj={}
f=open('degreesAdj','r')
for x in f:
	ar=[i for i in x.split()]
	compAdj[ar[1]]=ar[0]
	superAdj[ar[2]]=ar[0]



while True:
    s=input()
    if len(re.findall('\d',s))>0:
        break
    str=[i for i in s.split()]
    s=str[0]
    s=s.lower()
    tag=str[1]
    #rule for proper noun
    if tag=='PN':
    	pass
    elif tag=='NNS' or tag=='nns' or tag=='nnps' or tag=='NNPS': #rule for other nouns plural
    	t=s[:len(s)-2]
    	if s not in exceps['NNP'] and s not in same['NNP']:
	    	if re.match('[a-z]*ies$',s) and m(s[:len(s)-3]):
	    		print(1)
	    		s=s[:len(s)-3]+'y'
	    	elif re.match('[a-z]*es$',s) and m(s[:len(s)-2])>0 and ( re.match('[a-z]*zz$',s[:len(s)-2]) or re.match('[a-z]*ss$',s[:len(s)-2]) ):
	    		print(2)
	    		s=s[:len(s)-3]
	    	elif re.match('[a-z]*ves$',s) and m(s[:len(s)-3])>0:
	    		print(3)
	    		s=s[:len(s)-3]+'f'
	    	elif re.match('[a-z]*ves$',s) and m(s[:len(s)-3])==0:
	    		print(4)
	    		s=s[:len(s)-3]+'fe'
	    	elif re.match('[a-z]*s$',s) and m(s[:len(s)-1])>0 and s[-2]=='y' and not cons(s,-3):
	    		print(5)
	    		s=s[:len(s)-1]
	    	elif re.match('[a-z]*es$',s) and m(s[:len(s)-2])>0 and s[-3]=='o':
	    		print(6)
	    		s=s[:len(s)-2]
	    	elif re.match('[a-z]*i$',s) and m(s[:len(s)-1])>0:
	    		print(7)
	    		s=s[:len(s)-1]+'us'
	    	elif re.match('[a-z]*es$',s) and m(s[:len(s)-2])>0 and ( re.match('[a-z]*s$',t) or re.match('[a-z]*ss$',t) or re.match('[a-z]*sh$',t) or re.match('[a-z]*ch$',t) or re.match('[a-z]*x$',t) ):
	    		print(8)
	    		s=s[:len(s)-2]
    elif tag=='v' or tag=='vb' or tag=='vbd' or tag=='vbg' or tag=='vbn' or tag=='vbp' or tag=='vbz': # rules for verbs
        if s in irrverbs1:
            s=irrverbs1[s]
        elif s in irrverbs2:
            s=irrverbs2[s]
        elif re.match('[a-z]*ing$',s) and m(s[:len(s)-3])>0:
            s=s[:len(s)-3]
            if s[-1]=='v' or s[-1]=='c':
                s+='e'
            elif s[-1]==s[-2] and not (s[-1]=='l' or s[-1]=='s'):
                s=s[:len(s)-1]
        elif re.match('[a-z]*ed$',s) and m(s[:len(s)-2])>0:
            s=s[:len(s)-2]
        elif re.match('[a-z]*d$',s) and m(s[:len(s)-1])>0:
            s=s[:len(s)-1]
    elif tag=='jjr' or tag=='JJR': #rules for comparative degree adjectives
        if s in compAdj:
            s=compAdj[s]
        elif re.match('[a-z]*er$',s):
            if re.match('[a-z]*ier$',s):
                s=s[:len(s)-3]+'y'
            else:
                s=s[:len(s)-2]
    elif tag=='jjs' or tag=='JJS': # rules for superlative degree adjectives
        if s in superAdj:
            s=superAdj[s]
        elif re.match('[a-z]*est$',s):
            if re.match('[a-z]*iest$',s):
                s=s[:len(s)-4]+'y'
            else:
                s=s[:len(s)-3]


    print(s)
