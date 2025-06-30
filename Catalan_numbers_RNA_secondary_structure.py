def compute_catalan_numbers(edges):
    lst = [0]*(edges+2)
    lst[0] = 1
    lst[2] = 1
    lst[4] = 2
    for n in range(6, edges + 2,2):
        catalan_num = 0
        for i in range(2,n+2,2):
            catalan_num = catalan_num + lst[n-i] * lst[i-2]
        lst[n] = catalan_num
    return lst[-2]

bond_dict = {'A':'U','U':'A', 'C':'G','G':'C'}

def secondary_structure(RNA_seq):
    catalan_num = 0
    n = len(RNA_seq)
    if(n) == 0:
        return 1
    if(n) == 2:
        return 1
    for k in range(1,n+1,2):
        if(RNA_seq[k] != bond_dict[RNA_seq[0]]):
            continue
        catalan_num = catalan_num + secondary_structure(RNA_seq[1:k]) * secondary_structure(RNA_seq[k+1:])
    return catalan_num

    

def secondary_structure_optimized(RNA_seq):
    def score(i,j):
        if RNA_seq[i] == bond_dict[RNA_seq[j]]:
            return 1
        return 0
    
    n = len(RNA_seq)
    lst = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n-1):
        if(RNA_seq[i] == bond_dict[RNA_seq[i+1]]):
            lst[i][i+1] = 1
            
    # Think of i as the start index, j as finish index all inclusive.
    
    for j in range(1,n):
        for i in range(j-2,-1,-1):
            value = 0
            for k in range(j-1,i-1,-1):
                
                if(j-1 == k):
                    value = value + lst[i][k-1]*score(j,k)
                else:
                    value = value + lst[i][k-1] * (lst[k+1][j-1]) *score(j,k)
            value = value + score(i,j)*lst[i+1][j-1]
            if (((i+j)%2 ==0)):
                lst[i][j] = 0
            else:
                lst[i][j] = value
    return lst[0][-1]

string = ""

with open("rosalind_cat.txt") as f:
    f.readline()
    for x in f:
        string = string + x.rstrip('\n')
print(string)

print(secondary_structure_optimized(string)%1000000)
#print(compute_catalan_numbers(len(string)))
    
