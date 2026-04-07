# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
#
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.

dtfile = open('/Users/yusuf/Downloads/rosalind_gc.txt', 'r')

from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

gc_content = {}
for record in SeqIO.parse(dtfile, 'fasta'):
    gc_content[record.id] = gc_fraction(record.seq) * 100

best_id = max(gc_content, key=gc_content.get)

print(f"{best_id}\n{gc_content[best_id]:.6f}")
