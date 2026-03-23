dtfile = open('/Users/yusuf/Downloads/rosalind_rna.txt', 'r+')
seq = dtfile.readlines()[0]
rna = seq.replace('T','U')
print(rna)