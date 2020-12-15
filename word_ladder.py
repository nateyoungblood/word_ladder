# Given two words (start and end), and a dictionary, find the length of shortest transformation sequence 
# from start to end, such that only one letter can be changed at a time and each intermediate word must exist in the dictionary. 
# For example, given:

start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]

def split(word):
    li=[char for char in word]  
    return(li)

def match(a,b):
    sp_a=split(a)
    sp_b=split(b)
    ma=0
    for x in range(0,len(sp_a)):
        if sp_a[x]==sp_b[x]:
            ma=ma+1
    return(ma)

def search(a,b):
    seq=[start]
#     print(match(seq[-1],b))
#     while match(seq[-1],b)<=1:
#         for x in range(len(dict)):
    if match(seq[-1],end)>1:
        print("they already match!")
    else:
        while match(seq[-1],end)<=1:
            for x in range(len(dict)):
                if match(seq[-1],dict[x])==1:
                    seq.append(dict[x])
                    break
                seq[x]=seq
                seq[x]=seq[x].append(dict[x])
    print(seq1,seq2)


# def search(a,b):
#     seq=list()
#     for x in range(len(dict)):
#         if match(a,b)>0:
#             print("match!")
#         elif match(a,dict[x])>1:
#             seq.append(dict[x])
#     if match(seq[len(seq)],b):
#         return(seq)
#     else:
#         for x in range()
            
#     print(seq)

# match("hot","gin")    
search(start,end)
    