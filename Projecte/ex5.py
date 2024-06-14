import re
import requests

#web la qual agafem la informació
website = "https://www.mercadolibre.com.ar/c/computacion#menu=categories"
#agafem el script
resultado = requests.get(website)
#pasem tot a text
content = resultado.text
patron = r"https://listado.mercadolibre.com.ar/computacion/[\w-]*"
#cerca dins dels resultats de texte tot el que contingui el patró
maquines_repetides = re.findall(patron, str(content))

#evitem que apareguin apartats duplicats
no_duplicats = list(set(maquines_repetides))

maquines_finals = []

def pex5():
    print("Apartats de informàtica de mercado libre: ")
    for i in no_duplicats:
        #substitueix tota la ruta per res
        nom_maquines = i.replace("https://listado.mercadolibre.com.ar/computacion/", "")
        maquines_repetides.append(maquines_finals)
        print(nom_maquines)

