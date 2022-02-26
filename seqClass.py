import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")

# To search for a specifit motif inside a sequence
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

# Interpreting lower case and differentiating DNA from RNA
args.seq = args.seq.upper()
if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq) and not re.search('U', args.seq):
        print ('The sequence is DNA')
    elif re.search('U', args.seq) and not re.search('T', args.seq):
        print ('The sequence is RNA')
    else:
        print ('The sequence is not DNA or RNA')
else:
    print ('The sequence is not DNA nor RNA')

# To search for a specific motif inside a sequence
if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("FOUND")
    else:
        print("NOT FOUND")
