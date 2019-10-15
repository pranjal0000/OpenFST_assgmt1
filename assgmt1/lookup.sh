if [[ $1 == *"L.fst"* ]];
then
    # code if found
    python3 p1_out.py $2
	if grep -Rq $2 isyms.txt
	then
	    # code if found
	    fstcompile --isymbols=isyms.txt --acceptor p1.fst > A.fst
		fstcompose A.fst $1 > C.fst 
		fstprint --isymbols=isyms.txt --osymbols=osyms1.txt C.fst > final.txt
	else
	    # code if not found
	    > final.txt
	fi

	python3 p1_check.py
	python3 del.py
else
    # code if not found
    python3 p3_out.py $2
    fstcompile --isymbols=isyms.txt --osymbols=osyms.txt p1.fst > A.fst
    fstcompose A.fst QPrefix.fst > Check.fst
    fstminimize --allow_nondet Check.fst > Check_min.fst
    fstepsnormalize Check_min.fst > Check_eps.fst
    fstprint --isymbols=isyms.txt --osymbols=osyms1.txt Check_eps.fst > text_pre.txt
    python3 p3_check.py text_pre.txt $2
    rm -f A.fst Check.fst Check_min.fst Check_eps.fst text_pre.txt text_Qsyn.txt Qsyn.fst p1.fst text_syn.txt isyms.txt
    python3 del.py
fi