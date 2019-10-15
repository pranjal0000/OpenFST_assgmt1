import sys
inFile = sys.argv[1]
d={}
with open(inFile,"r") as f:
	#f=f.encode('latin1').decode('utf8')
	for line in f:
		line=line.split()
		if not line:
			continue
		d[line[0]]=line[1:]

ins=open('isyms.txt','w+')
ops=open('osyms1.txt','w+')
l=[]
ins.write("<eps> 0\n")
ops.write("<eps> 0\n")
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
	ops.write(i +' '+str(c2)+'\n')
	c2+=1
	
#initial state adn final state is 0
fst=open('p1.fst','w+')
c1=1
for i,j in d.items():
	# print(len(j))
	t=0
	for k in j:
		if t==0 and len(j)!=1:
			fst.write(str(0)+' '+str(c1)+' '+i+' '+k+'\n')
			c1+=1
		elif t==0 and len(j)==1:
			fst.write(str(0)+' '+str(0)+' '+i+' '+k+'\n')
		elif t==(len(j)-1):
			fst.write(str(c1-1)+' '+str(0)+' '+'<eps>'+" "+k+'\n')
		else:
			fst.write(str(c1-1)+' '+str(c1)+" "+'<eps>'+' '+k+'\n')
			c1+=1
		t+=1
fst.write(str(0))

	