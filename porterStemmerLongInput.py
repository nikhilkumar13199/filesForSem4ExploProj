import re
import nltk
from nltk.stem.porter import *

print('Enter any number to stop the program or a word to stem it!')

def cons(s,i):
    if re.match('[aeiou]',s[i]):
        return 0
    if re.match('y',s[i]):
        if i==0:
            return 1
        else:
            return (not cons(s,i-1))
    return 1

#This function return the measure of word or word part, (C)(VC)^m(C)
def m(s):
    m = 0
    for i in range(0, len(s) - 1):
        if (not cons(s, i)) and cons(s, i + 1):
            m += 1
    return m

stemmer=PorterStemmer()
f=open("sample.txt",'r')
if f.mode=='r':
    sr=f.read()
    sr2=re.findall("['\w']+",sr)
for s in sr2:
    if len(re.findall('\d',s))>0:
        break
    str=[i for i in s.split()]
    s=str[0]
    s=s.lower()
    x=stemmer.stem(s)

    # step 1a
    if re.match('[a-z]*sses$',s):
        s=s[:len(s)-4]+'ss'
    elif re.match('[a-z]*ies$',s):
        s=s[:len(s)-3]+'i'
    elif re.match('[a-z]*s$',s):
        s=s[:len(s)-1]

    #step 1b
    if re.match('[a-z]*eed$',s):
        if m(s[:len(s)-3])>0:
            s=s[:len(s)-3]+'ee'
        else:
            s=s
    if re.match('[a-z]*[aeiou][a-z]*ed$',s):
        s=s[:len(s)-2]
        #cleanup
        if re.match('[a-z]*at$',s):
            s=s+'e'
        elif re.match('[a-z]*bl$',s):
            s+='e'
    if re.match('[a-z]*[aeiou][a-z]*ing$',s):
        s=s[:len(s)-3]
        #cleanup
        if re.match('[a-z]*at$',s):
            s=s+'e'
        elif re.match('[a-z]*bl$', s):
            s += 'e'

    #cleanup
    if cons(s,-1) and cons(s,-2) and s[-1]==s[-2] and (s[-1]!='l' and s[-1]!='s' and s[-1]!='z'):
        s=s[:len(s)-1]
    elif len(s)>=3 and m(s)==1 and cons(s,-1) and not cons(s,-2) and cons(s,-3):
        s+='e'

    #1c Y elimination
    if re.match('[a-z]*[aeiou][a-z]*y$',s):
        s=s[:len(s)-1]+'i'
    #derivational morphology
    elif m(s)>0 and re.match('[a-z]*tional$',s):
        s=s[:len(s)-6]+'te'
    elif m(s)>0 and re.match('[a-z]*ization$',s):
        s=s[:len(s)-7]+'ize'
    elif m(s)>0 and re.match('[a-z]*biliti$',s):
        s=s[:len(s)-6]+'ble'
    elif m(s)>0 and re.match('[a-z]*icate$',s):
        s=s[:len(s)-5]+'ic'
    elif m(s)>0 and re.match('[a-z]*ful$',s):
        s=s[:len(s)-3]
    elif m(s)>0 and re.match('[a-z]*ness$',s):
        s=s[:len(s)-4]
    elif m(s[:len(s)-3])>0 and re.match('[a-z]*tion$',s):
        s=s[:len(s)-3]
    elif m(s[:len(s)-5])>0 and re.match('[a-z]*ation$',s):
        s=s[:len(s)-5]
    elif m(s[:len(s)-4])>0 and re.match('[a-z]*[ae]nce$',s):
        s=s[:len(s)-4]
    elif m(s[:len(s)-4])>0 and re.match('[a-z]*ment$',s):
        s=s[:len(s)-4]
    elif m(s[:len(s)-3])>1 and re.match('[a-z]*ive$',s):
        s=s[:len(s)-3]
    elif m(s[:len(s)-2])>1 and re.match('[a-z]*ly$',s):
        s=s[:len(s)-2]
    elif m(s[:len(s)-4])>1 and re.match('[a-z]*izer*',s):
        s=s[:len(s)-4]

    if m(s[:len(s)-1])>1 and re.match('[a-z]*e$',s):
        s=s[:len(s)-1]
    print(s,end=" ")
    print(x)