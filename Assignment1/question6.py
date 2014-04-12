#computes the average length of a list of DNA Sequences
seq1=raw_input("first sequence ")
seq2=raw_input("first sequence ")
seq3=raw_input("first sequence ")

seqlist=seq1

for seq in seqlist:
    print seq   
    averagelength= len(seq)/len(seqlist)
print "seqlist contains",len(seq),"objects"
print "the average is", averagelength