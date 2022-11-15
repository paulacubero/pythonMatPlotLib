# https://naps.com.mx/blog/ejemplos-en-matplotlib-de-5-tipos-graficos/
import pandas as pd
import matplotlib.pyplot as plt

def consumir():
    datos=pd.read_csv('casasboston.csv')
    #print(datos)
    df=datos[['RM','CRIM','TOWN','TAX']] # convertir los datos en dataframe
    #print(df)
    df.RM.plot.hist()
    plt.show()
#consumir()

def consumirDisperson():
    datos=pd.read_csv('casasboston.csv')
    #print(datos)
    df=datos[['RM','CRIM','TOWN','TAX','MEDV']] # convertir los datos en dataframe
    #print(df)
    df.plot.scatter(x='CRIM',y='MEDV',alpha=0.3)
    plt.show()
#consumirDisperson()

def consumirBarras():
    datos=pd.read_csv('casasboston.csv')
    #print(datos)
    df=datos[['RM','CRIM','TOWN','TAX','MEDV']] # convertir los datos en dataframe
    #print(df)
    valor_por_ciudad = df.groupby('TOWN')['MEDV'].mean()
    valor_por_ciudad.head(5).plot.bar()
    df.plot.bar()
    plt.show()
# barh-> horizontal.  bar-> vertical
#consumirBarras()

def consumirCajas():
    datos=pd.read_csv('casasboston.csv')
    #print(datos)
    df=datos[['RM','CRIM','TOWN','TAX','MEDV']] # convertir los datos en dataframe
    #print(df)
    df.head(10).boxplot(column="MEDV",by='TOWN',figsize=(10, 6))
    plt.show()

#consumirCajas()

def consumirCircular():
    datos=pd.read_csv('casasboston.csv')
    #print(datos)
    df=datos[['RM','CRIM','TOWN','TAX','MEDV']] # convertir los datos en dataframe
    #print(df)
    df.RM.head(7).value_counts().plot.pie()
    plt.show()

consumirCircular()