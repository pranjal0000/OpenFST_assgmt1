f=open('lex.txt','r')
lines=f.readlines()
newf=open('rev_lex.txt','w+')


for line in lines:
	line=line.split()
	stw=line[0]
	stw=stw[::-1]
	l=line[1:]
	l.reverse()
	s=''
	for i in l:
		s=s+' '+i
	newf.write(str(stw)+' '+str(s)+'\n')

