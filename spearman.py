# computes the Spearman correlation between a file (containing edit distances of sequences) and several tensor block
# results
from scipy import stats


def get_dist(fname):
    fed = open(fname)
    ed = []
    for line in fed.readlines():
        assert (line[-1] == '\n')
        vals = line[:-1].split('\t')
        for i in range(1, len(vals)):
            ed.append(float(vals[i]))
    print(f'Loaded {len(ed)} values')
    return ed


def main():
    dir = '/tmp/fasta'
    print('Loading edit distances...')
    fed = get_dist(dir + '/ed_normalized')

    for k in range(30, 42):
        for b in range(1, int((k + 1) / 2) + 1):
            if k % b != 0:
                continue
            fname = f'{dir}/tsb.csv_{k}_{b}'
            print(f'Reading {fname}..')
            ftsb = get_dist(fname)
            assert (len(fed) == len(ftsb))
            print(f'Computing Spearman correlation...')
            print(stats.spearmanr(fed, ftsb));


if __name__ == "__main__":
    main()
