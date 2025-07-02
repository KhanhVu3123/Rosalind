lst = []
seq = ""


# Reverse complement function for a sequence.
complementary_dict = {'A':'T','T':'A','G':'C','C':'G'}
def reverse_complement(seq):
    rev_seq = ""
    for nu in seq:
        rev_seq = complementary_dict[nu] + rev_seq
    return rev_seq

def hamming_distance(seq1, seq2):
    dist = 0
    for i in range(len(seq1)):
        if(seq1[i] != seq2[i]):
            dist +=1
    return dist


# Add all sequences into 1 big list.
with open("/Users/khanhvu/Desktop/Academic/Coding_stuff/Rosalind/rosalind_corr.txt") as f:
    for line in f:
        if line.startswith(">") == True:
            lst.append(seq)
            seq = ""
        else:
            seq = seq + line.rstrip()
    lst.append(seq)

lst = lst[1:]

# Convert big list into dictionary of occurence.
big_dict = {}
for seq in lst:
    if seq in big_dict.keys():
        big_dict[seq] += 1
        continue
    if reverse_complement(seq) in big_dict.keys():
        big_dict[reverse_complement(seq)] +=1
        continue
    big_dict[seq] = 1
    
    

errors = []
corrects = []

for seq in list(big_dict.keys()):
    if(big_dict[seq] == 1):
        errors.append(seq)
    else:
        corrects.append(seq)

# Correct the error sequence.

for error_seq in errors:
    for correct_seq in corrects:
        if(hamming_distance(error_seq,correct_seq) == 1):
            print(error_seq+"->"+correct_seq)
            break
        if(hamming_distance(error_seq, reverse_complement(correct_seq)) == 1):
            print(error_seq+"->"+reverse_complement(correct_seq))
            break

                
