tarikh_list = list(input('tarikh shamsi'))
sal_mah_roz = ['','','']
j=0
for i in tarikh_list:
    if i != '/':
        sal_mah_roz[j] += f'{i}'
    else:
        j += 1


sal_kabise = [1,5,9,13,17,22,26,30]
sal_mah_roz2 = ['','','']

if 0<int(sal_mah_roz[1])<7:

    if int(sal_mah_roz[2])+1 < 32:
        sal_mah_roz2[0],sal_mah_roz2[1],sal_mah_roz2[2] = sal_mah_roz[0],sal_mah_roz[1],str(int(sal_mah_roz[2])+1)

    elif int(sal_mah_roz[2])+1 > 31:
        sal_mah_roz2[2] = str(int(sal_mah_roz[2])+1 - 31)
        sal_mah_roz2[1] = str(int(sal_mah_roz[1])+1)
        sal_mah_roz2[0] = sal_mah_roz[0]
        if int(sal_mah_roz2[1]) > 12:
            sal_mah_roz2[1] = str(int(sal_mah_roz2[1])-1)
            sal_mah_roz2[0] = str(int(sal_mah_roz[0])+1)
else:
    if (int(sal_mah_roz[0]) % 33) not in sal_kabise:
        if int(sal_mah_roz[2])+1 < 30:
            sal_mah_roz2[0],sal_mah_roz2[1],sal_mah_roz2[2] = sal_mah_roz[0],sal_mah_roz[1],str(int(sal_mah_roz[2])+1)

        elif int(sal_mah_roz[2])+1 > 29:
            sal_mah_roz2[2] = str(int(sal_mah_roz[2])+1 - 29)
            sal_mah_roz2[1] = str(int(sal_mah_roz[1])+1)
            sal_mah_roz2[0] = sal_mah_roz[0]
            if int(sal_mah_roz2[1]) > 12:
                sal_mah_roz2[1] = str(int(sal_mah_roz2[1])-1)
                sal_mah_roz2[0] = str(int(sal_mah_roz[0])+1)
    else:
        if int(sal_mah_roz[2])+1 < 31:
            sal_mah_roz2[0],sal_mah_roz2[1],sal_mah_roz2[2] = sal_mah_roz[0],sal_mah_roz[1],str(int(sal_mah_roz[2])+1)

        elif int(sal_mah_roz[2])+1 > 30:
            sal_mah_roz2[2] = str(int(sal_mah_roz[2])+1 - 30)
            sal_mah_roz2[1] = str(int(sal_mah_roz[1])+1)
            sal_mah_roz2[0] = sal_mah_roz[0]
            if int(sal_mah_roz2[1]) > 12:
                sal_mah_roz2[1] = str(int(sal_mah_roz2[1])-1)
                sal_mah_roz2[0] = str(int(sal_mah_roz[0])+1)
print(f'{sal_mah_roz2[0]}/{sal_mah_roz2[1]}/{sal_mah_roz2[2]}')
