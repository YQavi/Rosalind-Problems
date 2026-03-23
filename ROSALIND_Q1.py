dtfile = open('/Users/yusuf/Downloads/rosalind_dna.txt', 'r')
seq = dtfile.readlines()[0]
base = ['A', 'C', 'G', 'T']

for base in seq:
    counts = seq.count('A'), seq.count('C'), seq.count('G'), seq.count('T')
print(*counts)
