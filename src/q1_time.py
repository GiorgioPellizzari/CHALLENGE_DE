from typing import List, Tuple
from datetime import datetime
import json 
import pandas as pd

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    """
    Función que retorna los 10 días mas tweeteados presentes en el json de entrada, en conjunto
    al nombre de usuario que mas tweets realizó.

    Parametros:
        - file_path (str): Ruta del archivo json a trabajar.

    Return: 
        - Lista de Tuplas con formato (Fecha, Usuario)

    """


    data=[]
    #Se abre el archivo json, el cual se lee linea por linea, dado que cada linea es un objeto.
    with open(file_path, 'r') as file:
        for line in file:
            obj = json.loads(line)
            data.append(obj)
    
    #Se genera un dataframe del json agregando columnas de utilidad
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    df['date_only'] = df['date'].dt.date
    df['username'] = df['user'].apply(lambda x: x['username'])

    #Se generan dos dataframe, uno con el recuento de tweets por fecha y otro con el usuario que
    #mas tweeteo por fecha.
    grouped = df.groupby(['date_only', 'username']).size().reset_index(name='count')
    most_frequent_user = grouped.loc[grouped.groupby('date_only')['count'].idxmax()]
    grouped_df=df.groupby('date_only').size().reset_index(name='count')

    #Se juntan ambos dataframes segun fecha, se ordenan de mayor a menor cantidad de tweets
    # y se genera la lista de tuplas del top 10.
    join=pd.merge(most_frequent_user,grouped_df, on='date_only')
    sorted_join = join.sort_values(by='count_y', ascending=False)
    dateuser=sorted_join[['date_only','username']].head(10)
    q1_t = [tuple(x) for x in dateuser.values]

    return q1_t