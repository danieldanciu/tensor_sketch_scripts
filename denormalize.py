f = open('/tmp/fasta/ed_normalized')
out = open('/tmp/fasta/ed_normalized.csv', 'w')
names = []
for line in f.readlines():
    vals = line[:-1].split('\t')
    names.append(vals[0])
    for i in range(0, len(names) - 1):
        out.write(names[i] + ', ' + names[-1] + ', ' + vals[i+1] + '\n')

out.close()
f.close()

