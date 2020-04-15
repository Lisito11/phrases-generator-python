import json
import marshal


def extraerFrases():
    with open("frases.json", encoding="utf8") as file:
        lista_frases = []
        frases = json.load(file)
        for i in range(0, 62):
            frase = frases["frases"][i]["frase"]
            autor = frases["frases"][i]["autor"]
            reflexion = frases["frases"][i]["reflexion"]
            lista_frases.append(frase)
            lista_frases.append(autor)
            lista_frases.append(reflexion)
        nueva_lista = [lista_frases[i:i + 3] for i in range(0, len(lista_frases), 3)]
        return nueva_lista


frases = extraerFrases()
lista2 = []

# Cargamos las frases guardadas
txt_frases_abrir = open("comprobacion_frases.txt", "br")
datos = marshal.load(txt_frases_abrir)
txt_frases_abrir.close()





# for frase in frases:
 #    if frase not in lista2:
  #      print(frase)
   #      break

# Guardamos la frase usada
txt_frases_cerrar = open("comprobacion_frases.txt", "bw")
marshal.dump(lista2, txt_frases_cerrar)
txt_frases_cerrar.close()
