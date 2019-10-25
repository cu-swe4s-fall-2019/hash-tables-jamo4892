import matplotlib.pyplot as plt
import sys
import argparse
import matplotlib
matplotlib.use('Agg')

if __name__ == '__main__':
    """
    This is the main function that runs the
    scatter plot.
    """
    parser = argparse.ArgumentParser(description='Scatter plot',
                                     prog='scatter')
    parser.add_argument('--out_file', type=str,
                        help='Name of output file', required=True)
    args = parser.parse_args()
    # Add input arguments.

    out_file = args.out_file

    X = []
    Y = []
    i = 0
    for l in sys.stdin:
        A = l.rstrip().split()
        if len(A) == 2:
            X.append(float(A[0]))
            Y.append(float(A[1]))
        elif len(A) == 1:
            X.append(float(i))
            Y.append(float(A[0]))
            i += 1

    width = 3
    height = 3
    fig = plt.figure(figsize=(width, height), dpi=300)

    ax = fig.add_subplot(1, 1, 1)

    ax.plot(X, Y, '.', ms=1, alpha=0.5)
    ax.set_xlabel('Hashed Word')
    ax.set_ylabel('Hashed Value')
    ax.set_title('Hash Functions')

    plt.savefig(out_file, bbox_inches='tight')
    # I copied all this code from the /lectures/hash_tables repo.