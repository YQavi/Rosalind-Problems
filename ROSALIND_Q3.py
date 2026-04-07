dtfile = open('/Users/yusuf/Downloads/rosalind_revc.txt', 'r')
seq = str(dtfile.readline().strip())
cDict = {'A':'T', 'C':'G', 'G':'C', 'T':'A', 'N':'N', 'a':'t', 'g':'g', 'c':'c', 't':'a', 'n':'n'}
print(''.join([cDict[nuc]for nuc in reversed(seq.upper())]))