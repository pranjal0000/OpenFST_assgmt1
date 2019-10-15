import sys
import os
if os.path.exists("isyms.txt"):
	os.remove("isyms.txt")
if os.path.exists("osyms.txt"):
	os.remove("osyms.txt")
inp=sys.argv[1]


d={}
with open('lex.txt',"r") as f:
	#f=f.encode('latin1').decode('utf8')
	for line in f:
		line=line.split()
		if not line:
			continue
		d[line[0]]=line[1:]

ins=open('isyms.txt','w+')
# ops=open('osyms.txt','w+')
l=[]
ins.write("<eps> 0\n")
# ops.write("<eps> 0\n")
c1=1
c2=1
for i in sorted(d.keys()):
	ins.write(i+' '+str(c1)+'\n')
	c1+=1
	for k in d[i]:
		
		l.append(k)

l=list(set(l))
l.sort()
for i in l:
	# ops.write(i +' '+str(c2)+'\n')
	c2+=1

fst=open('p1.fst','w+')
fst.write('0 0 '+ str(inp)+'\n')
fst.write('0 \n')
