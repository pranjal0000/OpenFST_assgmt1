import os

ins=open("final.txt",'r')
l=[]
for line in ins:
	line=line.split()
	if len(line)<=1:
		continue
	l.append(line[-1])

if len(l)==0:
	print("<OOV>")
else:
	for i in range(len(l)):
		print(l[i],end=" ")

if os.path.exists("isyms.txt"):
	os.remove("isyms.txt")
if os.path.exists("osyms.txt"):
	os.remove("osyms.txt")
if os.path.exists("p1.fst"):
	os.remove("p1.fst")
if os.path.exists("A.fst"):
	os.remove("A.fst")
if os.path.exists("C.fst"):
	os.remove("C.fst")
if os.path.exists("final.txt"):
	os.remove("final.txt")



