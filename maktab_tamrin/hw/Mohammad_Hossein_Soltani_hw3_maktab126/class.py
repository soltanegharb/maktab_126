def jam_tavan2_zoj(alist):
    summation = 0
    for i in alist:
        if i % 2 ==0:
            summation += i**2
    out = sum([i for i in map(lambda x:x**2 if x%2 ==0 else None , alist) if i is not None])
    return summation,out
print(jam_tavan2_zoj([1,2,3,4]))