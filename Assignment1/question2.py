#inputs a DNA sequences and returns the first AND last three bases, exepet for when there is only six or less
DNAsequence=raw_input("enter a DNA sequence: ")

if len(DNAsequence)<=6:
    print "There are six nucleotides or less in your sequence, task can not be executed"
else:
    print DNAsequence[0:3]
    print DNAsequence[-3:]