lst = []
def check_number(num):
    string = str(num)
    for digit in string:
        if(digit not in ['1','2','3','4']):
            return False
    return True

for i in range(1000,10000,1):
    if(check_number(i)):
        lst.append(i)

num_to_base = {'1':'A','2':'C','3':'G','4':'T'}
def num_to_K_mer(num):
    k_mer = ""
    string = str(num)
    for digit in string:
        k_mer = k_mer + num_to_base[digit]
    return k_mer

k_mer_list = []
for num in lst:
    k_mer_list.append(num_to_K_mer(num))
    
DNA_seq = ""
with open("/Users/khanhvu/Desktop/Academic/Coding_stuff/Rosalind/rosalind_kmer.txt") as f:
    for line in f:
        if line.startswith(">"):
            continue
        DNA_seq = DNA_seq + line.rstrip()
        
DNA_seq_k_mer_list = []
for i in range(len(DNA_seq)-3):
    DNA_seq_k_mer_list.append(DNA_seq[i:i+4])

for k_mer in k_mer_list:
    print(DNA_seq_k_mer_list.count(k_mer), end=" ")
    



