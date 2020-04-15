import json


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


extraerFrases()
