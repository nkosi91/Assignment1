def read_fasta_file(fastafile):
    fastafile=raw_input("enter path to fasta file ")
    open("fastafile","r")
    return fastafile

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
