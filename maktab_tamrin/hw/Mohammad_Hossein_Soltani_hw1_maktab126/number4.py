print("""ebteda "tedad" ra vared konid be in sourat ke aval n(haman tedad Z)
bad az an m(tedad A va B) ra vared konid faghat ba "space" az ham joda konid
hala ke "tedad" vared shod yek "Enter" zade va "Z" ra vared konid dobare ba "space" az ham joda konid
hala ke "Z" ham vared shod dobare yek "Enter" zade va "A" ra vared konid ba "space" joda konid
va tamam ke shod yek "Enter" bezenid va "B" ra vared konid dobare ba "space" az ham joda konid
tedad azaye "A","B" bayad barabar bashad va "A" nabayad ozv tekrari dashte bashad hamin tor "B".
mesal:
3 2\n1 5 3\n3 1\n5 7
................
""")
vorodi = []
while len(vorodi) < 4:
    if len(vorodi) == 0:
        vorodi.append(input('tedad ra vared konid:\n'))
    if len(vorodi) == 1:
        vorodi.append(input('Z ra vared konid:\n'))
    if len(vorodi) == 2:
        vorodi.append(input('A ra vared konid:\n'))
    if len(vorodi) == 3:
        vorodi.append(input('B ra vared konid:\n'))

vorodi_named = [[],[],[],[]]
j=0
temp=' '
for i in vorodi:
    for c in i:
        if c.strip() and temp == ' ':
            vorodi_named[j].append(c)
        elif c.strip() and temp != ' ':
            vorodi_named[j][-1] += c
        temp = c
    temp=' '
    j += 1
del temp

tedad = vorodi_named[0]
Z = vorodi_named[1]
A = vorodi_named[2]
B = vorodi_named[3]

shadi = 0
for element in A:
    if element in Z:
        shadi +=1
for element in B:
    if element in Z:
        shadi -=1
print(f'\nshadi hast:\n{shadi}')
