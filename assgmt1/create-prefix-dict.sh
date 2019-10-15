fstsynchronize Q.fst Qsyn.fst
fstprint --isymbols=osyms.txt --osymbols=osyms1.txt Qsyn.fst > text_syn.txt
python3 p3_create.py text_syn.txt
fstcompile --isymbols=osyms.txt --osymbols=osyms1.txt text_syn.txt > QPrefix.fst