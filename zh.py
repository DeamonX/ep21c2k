
file = open("valaszok.txt", "r")
VersenyzoId=[]
VersenyzoValasz=[]
HelyesMegoldas=[]

def F1():
    counter=0
    line = file.readline()
    while line!="":
        if counter!=0:
            SpT=line.split(' ')
            VersenyzoId.append(SpT[0])
            FormaltValasz = SpT[1].replace('\n','')
            VersenyzoValasz.append(FormaltValasz)
        else:
            FormaltValasz = line.replace('\n','')
            HelyesMegoldas.append(FormaltValasz)
        counter+=1
        line = file.readline()
    file.close()
    print("1. feladat: Az adatok beolvasása.")
    print(f"2. feladat: A versenyen {counter-1} versenyző indult.")
def F2():
    bekert = input("3. feladat: Kérem adja meg a versenyző azonosítóját: ")
    if VersenyzoId.index(bekert)!=1:            #x[2:]
        ValaszID=(int)(VersenyzoId.index(bekert))
        print(f"{VersenyzoValasz[ValaszID]}")
    else:
        ValaszID=0
        print(f"Ilyen kóddal nem indult versenyző.")
    print(f"4. feladat: A helyes megoldás:\n{HelyesMegoldas[0]}")
    Valasz = VersenyzoValasz[ValaszID]
    Megoldas = HelyesMegoldas[0]
    output=""
    for i in range(14):
        if Megoldas[int(i)] == Valasz[int(i)]:
            output+="+"
        else:
            output+=" "
    print(output)
def F5():
    try:
        sorszam = int(input("5. feladat: Kérem adja meg a feladat sorszámát: "))
        if(sorszam<0 or sorszam>14):
            print("Nincs ilyen feladat!")
        else:
            osszesValasz= len(VersenyzoValasz)
            joValasz=0
            Megoldas = HelyesMegoldas[0]
            for i in VersenyzoValasz:
                if i[int(sorszam-1)] == Megoldas[int(sorszam-1)]:
                    joValasz+=1
            print(f"A feladatra {joValasz} fő, a versenyzők {(joValasz/osszesValasz)*100:.2f}%-a adott helyes választ.")
    except ValueError:
        print("Hibás input")
def F6():
    pontok=[]
    print("6. feladat: A versenyzők pontszámának meghatározása.")
    Megoldas = HelyesMegoldas[0]
    for i in VersenyzoValasz:
        PontSum=0
        for s in range(14):
            if i[s] == Megoldas[s]:
                if s <5:
                    PontSum+=3
                elif s>=5 and s<10:
                    PontSum+=4
                elif s>=10 and s<13:
                    PontSum+=5
                elif s==13:
                    PontSum+=5
        pontok.append(PontSum+1)
    UjFile = open("pontok.txt","w")
    for i in range(len(VersenyzoId)):
        UjFile.write(f"{VersenyzoId[int(i)]} {pontok[int(i)]}\n")
    UjFile.flush()
    UjFile.close()
    print("7. feladat: A verseny legjobbjai:")
    RegiPontok = pontok.copy()
    pontok.sort(reverse=True)

    MaxHaromPont=[]
    hely =3
    counter=0
    while hely !=0:
        try:
            if MaxHaromPont.index(pontok[counter])!=-1:
                counter+=1
        except ValueError:
            MaxHaromPont.append(pontok[counter])
            hely-=1
            counter+=1
    output=""
    for index in range(0,3):
        for i in range(len(RegiPontok)):
            if RegiPontok[i] == MaxHaromPont[index]:
                output+=f"{index+1}. díj ({RegiPontok[i]} pont): {VersenyzoId[i]}\n"
    print(output)
F1()
F2()
F5()
F6()