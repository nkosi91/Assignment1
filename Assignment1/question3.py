#takes a DNA sequence and returns the number of non-nucleotide bases
sequence=raw_input("enter DNA sequence ")

Sequence=sequence.upper()
print Sequence

counter=0

for nucleotide in Sequence:
    if nucleotide=="A":
        continue
    elif nucleotide=="T":
        continue
    elif nucleotide=="G":
        continue
    elif nucleotide=="C":
        continue
    else:
        counter=counter+1        
print "number of non-nucleotides is:",counter
        
        