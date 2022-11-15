# https://datos.gob.es/es/
# consume los datos del archivo inversiones
#almacena en un dataFrame el NOM_ENS, la SUPERFICIE y el TIPUSSOL

import pandas as pd
import matplotlib.pyplot as plt

def consumirInversiones():
    datos=pd.read_csv('suelo.csv')
    #print(datos)
    df=datos[['NOM_ENS','SUPERFICIE','TIPUSSOL']] # convertir los datos en dataframe
    print(df)
#consumirInversiones()

#gráfico de dispersión de los importes de inversiones por TIPUSSOL

def consumirDisperson():
    datos=pd.read_csv('suelo.csv')
    #print(datos)
    df=datos[['NOM_ENS','TIPUSSOL','SUPERFICIE']] # convertir los datos en dataframe
    #print(df)
    df.plot.scatter(x='NOM_ENS',y='SUPERFICIE',alpha=0.5)
    plt.show()
consumirDisperson()

#gráfico de barras de la inversión media de los 10 primeros NOM_ENS

def consumirBarras():
    datos=pd.read_csv('suelo.csv')
    #print(datos)
    df=datos[['NOM_ENS','SUPERFICIE','TIPUSSOL']] # convertir los datos en dataframe
    #print(df)
    valor_por_ciudad = df.groupby('NOM_ENS')['SUPERFICIE'].mean()
    valor_por_ciudad.head(10).plot.bar()
    df.plot.bar()
    plt.show()
# barh-> horizontal.  bar-> vertical
#consumirBarras()

# grafico circular de las inversiones de 10 TIPUSSOL
