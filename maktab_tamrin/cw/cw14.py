lst = ["eat", "tea", "tan", "ate", "nat", "bat"]
output, lst2 = [], lst.copy()
j= 0
temp = []

for i in lst2:
    lst2[j] = list(sorted(list(i)))
    j += 1


for i in lst2:
    temp = []
    for j in range(len(lst2)):
        if i == lst2[j]:
            temp.append(j)
    if temp not in output:
        output.append(temp)

for i in range(len(output)):
    for j in output[i]:
        output[i][j] = lst[j]
print(output)
