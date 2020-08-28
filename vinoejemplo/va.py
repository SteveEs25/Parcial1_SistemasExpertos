
import pandas as pd
df = pd.read_csv('winequality-red.csv', sep=';')
df.head()

def evaluacion_vinos(media, dato, nombre_componente):
    for i, ciclo in enumerate(dato):
        if ciclo >= media:
            print(df.loc[i, nombre_componente])  #Examina cada fila
            print('Alto')
        else:
            print(df.loc[i, nombre_componente])
            print('Bajo')
    lista = df.groupby(nombre_componente).quality.mean()  #Agrupa los datos por medio del componente especificado
    print(lista)
    

media = df.alcohol.median()
seleccionar_dato = df.alcohol 
componente = 'alcohol'

enviar_datos = evaluacion_vinos(media, seleccionar_dato, componente)
print(enviar_datos)

