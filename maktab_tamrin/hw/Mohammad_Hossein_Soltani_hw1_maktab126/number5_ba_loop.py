N = int(input('n:\n'))


n = abs(N)
i = 0
while n > 2 ** i:
    i += 1
pow_of_2 = i - 1


binary_n = ''
for i in range(pow_of_2,-1,-1):
    binary_n += str(n // (2 ** i))
    n -= (n // (2 ** i)) * (2 ** i)


binary_n_r = binary_n[::-1]
j,out = 0,0
for i in binary_n_r:
    out += int(i) * 2 ** (len(binary_n_r)-1 - j)
    j += 1

if N < 0:
    print(-out)
else:
    print(out)
