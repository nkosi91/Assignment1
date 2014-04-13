def read_fasta_file(fastafile):
    fasta=open(fastafile, "r")
    fasta.seek(0,0)
    header=""
    seq=""
    for line in fasta:
        if line.startswith(">"):
            header=line.strip()
        else:
            seq=seq+line.strip()
    idandseq=(header,seq)
    return idandseq
    
fasta=raw_input("enter path to fasta file ")
print read_fasta_file(fasta)


def reverse_complement(seq):
    revcomp=''
    nuc=''
    for nucleotide in seq.upper():
            if nucleotide=='A':
                nuc='t'
            elif nucleotide=='C':
                nuc='g'
            elif nucleotide=='G':
                nuc='c'
            elif nucleotide=='T':
                nuc='a'
            else:
                print nucleotide, "is not a nucleotide base"
            revcomp=nuc+revcomp
    return revcomp
            
seq=raw_input("enter sequence ")
#reverse_complement(seq)

print reverse_complement(seq)
