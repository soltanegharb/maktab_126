n = int(input('n:\n'))
n_bin = bin(n)[2:]
n_bin_reversed = '0b' + str(n_bin)[::-1]
n_new = int(n_bin_reversed,2)
print(n_new)
