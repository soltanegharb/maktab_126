lst = [3,2,3]
out = []
for i in lst:
    if lst.count(i)>len(lst)/2:
        if i not in out:
            out.append(i)
for i in out:
    print(i)
