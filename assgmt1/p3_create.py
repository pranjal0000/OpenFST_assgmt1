import sys
inFile = sys.argv[1]
# inFile='text_syn.txt'

# l=[]
# with open(inFile, "r") as f:
#     lines = f.readlines()
# with open(inFile, "w") as f:
#     for line in lines:
#     	line1=line.split(str="	")
#     	if not line1:
#     		continue
#     	if len(line1)==1:
#     		l.append(line1[0])
#     		continue
#     	else:
#     		f.write(line+'\n')
#     for i in l:
#     	f.write(str(i)+'\n')

f=open(inFile, "a+")
for i in range(18783):
	f.write(str(i+1)+'\n')


