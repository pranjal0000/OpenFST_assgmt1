import sys
inFile = sys.argv[1]
# inFile='lex.txt'
d={}
l=[]
with open(inFile,"r") as f:
	#f=f.encode('latin1').decode('utf8')
	for line in f:
		line=line.split()
		if not line:
			continue
		l.append(line[0])

l.sort()

ins=open('isyms.txt','w+')
ops=open('osyms.txt','w+')
ins.write("<eps> 0\n")
ops.write("<eps> 0\n")
out_syms=[]
c1=1
c2=1
for i in l:
	ins.write(i+' '+str(c1)+'\n')
	c1+=1
	d[i]=[]
	for k in i:
		d[i].append(k)
		out_syms.append(k)
		
out_syms=list(set(out_syms))
out_syms.sort()
for i in out_syms:
	ops.write(i +' '+str(c2)+'\n')
	c2+=1
term_state=[]
#initial state adn final state is 0
fst=open('p1.fst','w+')
c1=1
for i,j in d.items():
	# print(len(j))
	t=1
	for k in j:
		if t==1:
			fst.write(str(0)+' '+str(c1)+' '+i+' '+k+'\n')
			if t==len(j):
				term_state.append(c1)
			c1+=1
		elif t==len(j):
			fst.write(str(c1-1)+' '+str(c1)+' <eps> '+k+'\n')
			term_state.append(c1)
			c1+=1
		else:
			fst.write(str(c1-1)+' '+str(c1)+' <eps> '+k+'\n')
			c1+=1
		t+=1
for i in term_state:
	fst.write(str(i)+'\n')

	