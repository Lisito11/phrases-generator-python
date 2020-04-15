import json
import marshal
import requests


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

print(datos)
for frase in frases:
    if frase not in datos:
        f = frase[0]
        autor = frase[1]
        reflexion = frase[2]
        idChat = "-1001377568752"
        respuesta = requests.post(
            'https://api.telegram.org/bot1001617621:AAHW2Sbdvjx8bpXKDJdxXgGDe5CeJqQIHoA/sendMessage',
            data={f'chat_id': f'{idChat}', 'text': f"""¡BUENOS DIAS!\U0001F31E\U0001F60B

La frase de hoy es...\U0001F440

-{f}

-{autor}.

Y la pequeña reflexión es...\U0001F60C

-{reflexion}"""})
        lista2.append(frase)
        break

# Guardamos la frase usada
txt_frases_cerrar = open("comprobacion_frases.txt", "bw")
marshal.dump(lista2, txt_frases_cerrar)
txt_frases_cerrar.close()
