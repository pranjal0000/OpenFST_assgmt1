import sys
import os

a=sys.argv[1]
s=sys.argv[2]
l=len(s)
ans=[]
for i in range(1,l):
	pre=s[:i]
	suff=s[i:]
	# print(suff)
	suff=suff[::-1]
	str1=''
	str2=''

	os.system("python3 p3_out.py "+str(pre))
	os.system("fstcompile --isymbols=isyms.txt --osymbols=osyms.txt p1.fst > A.fst")
	os.system("fstcompose A.fst "+a+"/QPrefix.fst " +"> Check.fst")
	os.system("fstminimize --allow_nondet Check.fst > Check_min.fst")
	os.system("fstepsnormalize Check_min.fst > Check_eps.fst")
	os.system("fstprint --isymbols=isyms.txt --osymbols=osyms1.txt Check_eps.fst > text_pre.txt")
	os.system("python3 p3_check.py text_pre.txt "+str(pre)+" > temp1.txt")
	f=open('temp1.txt','r')
	line=f.readline()
	# line=line.split()
	str1=str(line)
	os.system("rm -f A.fst Check.fst Check_min.fst Check_eps.fst text_pre.txt text_Qsyn.txt Qsyn.fst p1.fst text_syn.txt isyms.txt temp1.txt")
	os.system("python3 del.py")

	os.system("python3 p3_out.py "+str(suff))
	os.system("fstcompile --isymbols=isyms.txt --osymbols=osyms.txt p1.fst > A.fst")
	os.system("fstcompose A.fst "+a+"/QSuffix.fst " +"> Check.fst")
	os.system("fstminimize --allow_nondet Check.fst > Check_min.fst")
	os.system("fstepsnormalize Check_min.fst > Check_eps.fst")
	os.system("fstprint --isymbols=isyms.txt --osymbols=osyms1.txt Check_eps.fst > text_pre.txt")
	os.system("python3 p3_check.py text_pre.txt "+str(suff)+" > temp2.txt")
	f1=open('temp2.txt','r')
	line1=f1.readline()
	# line1=line1.split()
	line1=line1[::-1]
	str2=str(line1)
	os.system("rm -f A.fst Check.fst Check_min.fst Check_eps.fst text_pre.txt text_Qsyn.txt Qsyn.fst p1.fst text_syn.txt isyms.txt temp2.txt")
	os.system("python3 del.py")

	str3=str1+str2
	ans.append(str3)


maxstr=''

for i in ans:
	if(len(i)>len(maxstr)):
		maxstr=i

print(maxstr)