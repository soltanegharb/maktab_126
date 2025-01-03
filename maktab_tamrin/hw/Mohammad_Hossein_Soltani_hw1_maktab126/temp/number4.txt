vorodi = list(input("""ebteda "tedad" ra vared konid be in sourat ke aval n(haman tedad Z)
bad az an m(tedad A va B) ra vared konid faghat ba "space" az ham joda konid
hala ke "tedad" vared shod yek "," zade va "Z" ra vared konid dobare ba "space" az ham joda konid
hala ke "Z" ham vared shod dobare yek "," zade va "A" ra vared konid ba "space" joda konid
va tamam ke shod yek "," bezenid va "B" ra vared konid dobare ba "space" az ham joda konid
tedad azaye "A","B" bayad barabar bashad va "A" nabayad ozv tekrari dashte bashad hamin tor "B".
mesal: 3 2,1 5 3,3 1,5 7
"""))
vorodi_named = [[],[],[],[]]
j=0
for i in vorodi:
    if i != ',':
        if i != ' ':
            vorodi_named[j].append(i)
    else:
        j += 1
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
print(shadi)
