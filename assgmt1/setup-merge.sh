python3 invert.py

python3 p1_create.py lex.txt
fstcompile --isymbols=isyms.txt --osymbols=osyms1.txt --keep_isymbols --keep_osymbols p1.fst > L.fst

python3 p2_create.py lex.txt
fstcompile --isymbols=isyms.txt --osymbols=osyms.txt --keep_isymbols --keep_osymbols p1.fst > S.fst
fstinvert S.fst > inv.fst
fstcompose --fst_align inv.fst L.fst > Q.fst
python3 del.py

fstsynchronize Q.fst Qsyn.fst
fstprint --isymbols=osyms.txt --osymbols=osyms1.txt Qsyn.fst > text_syn.txt
python3 p3_create.py text_syn.txt
fstcompile --isymbols=osyms.txt --osymbols=osyms1.txt text_syn.txt > QPrefix.fst
python3 del.py
rm -f Qsyn.fst text_syn.txt

python3 p1_create.py rev_lex.txt
fstcompile --isymbols=isyms.txt --osymbols=osyms1.txt --keep_isymbols --keep_osymbols p1.fst > rev_L.fst

python3 p2_create.py rev_lex.txt
fstcompile --isymbols=isyms.txt --osymbols=osyms.txt --keep_isymbols --keep_osymbols p1.fst > rev_S.fst
fstinvert rev_S.fst > rev_inv.fst
fstcompose --fst_align rev_inv.fst rev_L.fst > rev_Q.fst
python3 del.py

fstsynchronize rev_Q.fst rev_Qsyn.fst
fstprint --isymbols=osyms.txt --osymbols=osyms1.txt rev_Qsyn.fst > rev_text_syn.txt
python3 p3_create.py rev_text_syn.txt
fstcompile --isymbols=osyms.txt --osymbols=osyms1.txt rev_text_syn.txt > QSuffix.fst
python3 del.py
rm -f rev_L.fst rev_S.fst rev_inv.fst rev_Q.fst rev_Qsyn.fst rev_text_syn.txt 

mkdir -p $2
mv QPrefix.fst $2
mv QSuffix.fst $2


