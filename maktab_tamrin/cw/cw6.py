nums = [2, 7, 11, 15]
target = 9
out=[]
for i in range(len(nums)):
    for j in range(len(nums)):
        if (nums[i] + nums [j] == target) and i != j:
            if list(reversed([i,j])) not in out:
                out.append([i,j])
for i in out:
    print(i)
