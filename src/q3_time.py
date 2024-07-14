from typing import List, Tuple
import re
from collections import Counter
import json

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    """
    Función que retorna los 10 días mas tweeteados presentes en el json de entrada, en conjunto
    al nombre de usuario que mas tweets realizó.

    Parametros:
        - file_path (str): Ruta del archivo json a trabajar.

    Return: 
        - Lista de Tuplas con formato (Usuario, Menciones)

    """
    #Se abre el archivo, y se inicializa un Counter(). Ademas se utiliza una expresion regular
    #la cual detectará toda palabra que empiece con "@".
    with open(file_path, 'r') as file:
        dif_mentions = Counter()
        mention = re.compile(r'@(\w+)')
    #Se carga el json linea por linea, en el content del tweet se utiliza la expresion regular
    #para buscar todas sus instancias y luego agregar cada una de estas al Counter.
        for line in file:
            obj = json.loads(line)
            mentions = mention.findall(obj["content"])
            dif_mentions.update(mentions)
    #Finalmente se toman los counter y se retornan los 10 mas repetidos.
    return dif_mentions.most_common(10)
    