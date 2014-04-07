#Displays the reversal of a DNA sequence and replaces a "t" and a "T" for a "U"
sequence=raw_input("enter DNA sequence ")

DNAsequence=sequence[::-1] #reversing
   
print DNAsequence 

Sequence=DNAsequence.upper()

print Sequence

for nucleotide in Sequence:
    if nucleotide=="T":
        print "U",
    else:
        print nucleotide,
        
    
