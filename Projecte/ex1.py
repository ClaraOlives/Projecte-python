import random

#eligeix 3 nombre aleatoris entre l'1 i el 9
def gllistaaleatoris():
    l = []
    for i in range(3):
        l.append(random.randint(1,9))
    return l

#et demana introduir 3 nombres
def llegir_nombres():
    l = []
    for i in range(3):
        l.append(int(input("Introdueix un nombre: ")))
    return l

#compara tots els nombres amb la resposta correcta
def comparar(l,m):
    a = [0, 0, 0]
    for i in range(3):
        if l[i] == m[i]:
            a[i] = 10
    if a[0] == 10 and a[1] == 10 and a[2] == 10:
        print("Enhorabona, ho has encertat tot!")
        return 0
    
    for i in range(3):
        if a[i] == 0:
            if m[i] in l:
                a[i] = 5
    for i in range(3):
        if a[i] == 10:
            #et diu els correctes, els incorrectes o els que no estan en la seva posició
            print("L'element {} no és correcte".format(m[i]))
        elif a[i] == 5:
            print("L'element {} existeix, però no està al seu lloc".format(m[i]))
        else:
            print("L'element {} no existex".format(m[i]))

#bucle de les funcions
def pex1():
    op = 1
    l = gllistaaleatoris()
    while op!=0:
        m = llegir_nombres()
        op = comparar(l,m)

