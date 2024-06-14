import json
import os

def menu():
    op = -1 
    while op<0 or op>6:
        print("""
            Llista de compra:
              0. Crear llista
              1. Afegir element
              2. Editar element
              3. Eliminar element
              4. Llegir llista
              5. Guardar abans de sortir
              6. Sortir
            """)
        op = int(input("Introdueix una opció: "))
        if op<0 or op>6:
            print("Opció no vàlida!")
        else:
            return op
        
#Si el fitxer no està creat el crea
def crear_fixter(nom):
    with open(nom, "w") as f:
        print("El fiter {} s'ha creat".format(nom))

#Carrega el diccionari al fitxer
def carregar_fitxer(nom, dic):
    with open(nom, "r") as f:
        dic = json.load(f)
    return dic

#Diu que a la clau li sumi 1 cada vegada que hi hagi un element nou
#i li afegeix el seu valor
def afegir(dic):
    n = len(dic) + 1
    dic[str(n)] = input("Introdueix un producte: ")
    return dic

#Apareix un "index" amb tots els productes afegits 
#fiques el número del que vols i el pots modificar
def editar_element(dic, it):
    print("editar")
    for x,y in it:
        print("{}: {}\n".format(x,y))
    n = input("Indiqui el número del producte a modificar: ")
    dic[n] = input("Introdueix el nou producte: ")
    for x,y in it:
        print("{}: {}\n".format(x,y))

#El mateix que l'anterior però s'elimina
def eliminar_producte(it, n, pu):
    for x,y in it:
        print("{}: {}\n".format(x,y))
    n
    pu 
    for x,y in it:
        print("{}: {}\n".format(x,y))

#Llistar tots els elements del fitxer
def llegir_un_per_un(it):
    for x,y in it:
        print("{}: {}\n".format(x,y))

#Guarda les modificacions que hem fet
def guardar(dic, nom):
    with open(nom, "w") as f:
        json.dump(dic, f, indent=4)
    with open(nom, "r") as f:
        dic = json.load(f)

def pex2():
    #Comprova si el fitxer està creat
    nom = "llista_compra.json"
    dic = {}

    it = dic.items()
    if os.path.isfile(nom):
        dic = carregar_fitxer(nom, dic)
    else:
        crear_fixter(nom)
    
    op = -1
    while op!=6:
        op = menu()
        match(op):
            case 0:
                crear_fixter(nom)
            case 1:
                dic = afegir(dic)
            case 2:
                editar_element(dic, it)
            case 3:
                n = input("Indiqui el número del producte a eliminar: ")
                pu = dic.pop(n)
                dic = eliminar_producte(it, pu, n)
            case 4:
                llegir_un_per_un(it)
            case 5:
                guardar(dic, nom)
            case 6:
                print("Gràcies per emprar aquesta llista!")