#computes the average length of a list of DNA Sequences
i=0
seqlist=raw_input("first sequence ")


for seq in seqlist:
    print seq   
    averagelength= len(seq)/len(seqlist)
print "seqlist contains",len(seq),"objects"
print "the average is", averagelength