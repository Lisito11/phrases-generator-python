Tenemos 3 archivos. El programa.py que es donde esta el codigo python, el json que es donde estan las frases cuales extraemos con el programa.py y el comprobacion_frases.txt que explicare la funcion ahora:

El programa extraes todas las frases del json y las guarda en una lista. Cada frase consta del autor, una pequeña reflexion y la frase misma, seáse 3 elementos, entonces cuando guardo las frases en la lista las guardo un sublistas de 3 elementos, lo que constituye una frase completa. Un ejemplo: lista = [["frase1", "autor1","reflexion1" ], ["frase2", "autor2","reflexion2"]...]

Entonces en el comprobacion_frases.txt estan todas las frases que usare, pero serializadas y lo que hago es deserializalas y con un ciclo for recorrer la lista inicial y comparar si una frase se encuentra en la lista que extraje de comprobacion_frases.txt
immediatamente coincidira con la primera, entoces cuando eso pase seleccione eso y lo mando como mensaje por telegram luego borro el primer elemento de comprobacion_frases.txt y cargo de nuevos esa lista a ese archivo y ahora comenzara por la segunda frase que ahora ocupara la primera posicion y cuando vuelvo a ejecutar el programa la frase que coincide es la segunda y asi continua la secuencia.

Canal de telegram: https://t.me/inspiracionn

