vorodi = [1,2,2,1,2,3,2,3,4,9,3,2,3,4,4,5]
output = vorodi
output.reverse()
for i in vorodi:
    for j in range(output.count(i)-1):
        output.remove(i)
output.reverse()
print(output)
