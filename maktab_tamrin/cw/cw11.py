string = "abcabcbb"
listed_string = list(string)
out = list(reversed(listed_string))
for i in listed_string:
    for j in range(out.count(i)-1):    
        out.remove(i)
out.reverse()
print(len(out))
