from typing import List, Tuple
import emoji
from collections import Counter
import json

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    """
    Función que retorna los 10 días mas tweeteados presentes en el json de entrada, en conjunto
    al nombre de usuario que mas tweets realizó.

    Parametros:
        - file_path (str): Ruta del archivo json a trabajar.

    Return: 
        - Lista de Tuplas con formato (Emoji, Repeticiones)

    """
     
    #Se abre el archivo y por cada linea se carga un json, se inicializa un Counter().
    with open(file_path, 'r') as file:
        emoji_counts = Counter()
        for line in file:
            obj = json.loads(line)
    #Por cada char presente en emoji.EMOJI_DATA se añadira este un +1 a su contador en el Counter.
            for char in obj["content"]:
                if char in emoji.EMOJI_DATA:
                    emoji_counts[char] += 1
    #Una vez terminado el conteo, se ordenan segun cantidad de repeticiones y se seleccionan los 10
    #mas altos para el retorno.
    emoji_counts=sorted(emoji_counts.items(), key=lambda x: x[1], reverse=True)[:10]

    return emoji_counts