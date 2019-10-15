import sys
inp=sys.argv[2]
inFile=sys.argv[1]
f=open(inFile,'r')
lines=f.readlines()
s=''

index=0
for line in lines:
	line=line.split()
	if len(line) <= 1:
		continue
	if(inp[index]==line[2] and line[3]!='<eps>'):
		s=s+line[3]
		index+=1
	if(len(inp)==index):
		break

# for i in s:
# 	print(i,end=' ')



## BY OBSERVING THE LEXICON, WE SEE THAT THERE ARE CERTAIN EXCEPTIONS
## FOR THE SINGLE LETTER EXCEPTIONS, WE CAN DIRECTLY MAP THESE TO THE PHONES
##THIS CAN BE CONSIDERED A PRE-PROCESSING STEP TO INCREASE ACCURACY
if inp != "B" and inp!= "N" and inp!="D" and inp!="L" and inp!="S" and inp!="T":
	for i in s:
		print(i,end=' ')

if inp=='B':
	print('"b e:')
if inp=='D':
	print('"d e:')
if inp=='L':
	print('"E l')
if inp=='N':
	print('"E n')
if inp=='S':
	print('"E s')
if inp=='T':
	print('"t e:')









