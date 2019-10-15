python3 p2_create.py $1
fstcompile --isymbols=isyms.txt --osymbols=osyms.txt --keep_isymbols --keep_osymbols p1.fst > S.fst
# fstcompile --isymbols=isyms.txt --osymbols=osyms1.txt --keep_isymbols --keep_osymbols p2.fst > A.fst
fstinvert S.fst > inv.fst
# fstprint --isymbols=osyms.txt --osymbols=isyms.txt inv.fst > text.fst
# fstcompile --isymbols=osyms.txt --osymbols=isyms.txt text.fst > B.fst
fstcompose --fst_align inv.fst $2
python3 del.py
