import sys
inp = sys.argv[1]

ins=open('isyms.txt','w+')
ins.write("<eps> 0\n")
fst=open('p1.fst','w+')
c1=1

for i in inp:
	ins.write(str(i)+' '+str(c1)+'\n')
	fst.write(str(c1-1)+' '+str(c1)+' '+str(i)+' '+str(i)+'\n')
	c1+=1

fst.write(str(c1-1))



