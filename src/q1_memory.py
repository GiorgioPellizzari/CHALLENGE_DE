from typing import List, Tuple
from datetime import datetime, date
from collections import Counter
import json

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    """
    Función que retorna los 10 días mas tweeteados presentes en el json de entrada, en conjunto
    al nombre de usuario que mas tweets realizó.

    Parametros:
        - file_path (str): Ruta del archivo json a trabajar.

    Return: 
        - Lista de Tuplas con formato (Usuario, Menciones)

    """

    #Se abre el archivo y por linea se carga el json. Se cuenta y se almacena en un counter
    #las veces que se repite cada fecha
    with open(file_path, 'r') as file:
        date_count=Counter()
        for line in file:
            obj = json.loads(line)
            dt = datetime.fromisoformat(obj['date'])
            date = dt.strftime('%Y-%m-%d')
            date_count[date]+=1
        top_dates=date_count.most_common(10)
    date_user=[]
    #A partir de las 10 fechas mas tweeteadas, se cuenta el usuario que mas tweeteo en cada una
    #de ellas
    for dates in top_dates:
            user_count=Counter()
            with open(file_path, 'r') as file:
                for line in file:
                    obj = json.loads(line)
                    dt = datetime.fromisoformat(obj['date'])
                    date = dt.strftime('%Y-%m-%d')
                    if date==dates[0]:
                        user = obj['user']['username']
                        user_count[user]+=1
                dt = datetime.strptime(dates[0], '%Y-%m-%d')
                date_obj = dt.date()
    #Se toma la tupla (Fecha, Usuario) y se almacena en date_user para el retorno
                date_user.append((date_obj,user_count.most_common(1)[0][0]))
    return date_user
