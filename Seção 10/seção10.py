import pandas as pd
import seaborn as srn
import statistics  as sts

#importar dados
dataset = pd.read_csv("tempo.csv", sep=";")
#visulizar
dataset.head()

dataset.shape

#explorar dados categoricos
#Aparencia
grupo = dataset.groupby(['Aparencia']).size()
grupo

grupo.plot.bar(color = 'gray')

#Vento
grupo = dataset.groupby(['Vento']).size()
grupo

#Jogar
grupo = dataset.groupby(['Jogar']).size()
grupo

#explorar colunas numéricas
#Temperatura
dataset['Temperatura'].describe()

srn.boxplot(dataset['Temperatura']).set_title('Temperatura')

srn.distplot(dataset['Temperatura']).set_title('Temperatura')

#Umidade
dataset['Umidade'].describe()

srn.boxplot(dataset['Umidade']).set_title('Umidade')

srn.distplot(dataset['Umidade']).set_title('Umidade')

#contamos valores NAN
dataset.isnull().sum()

#Umidade
#remover nas e substiutir pela mediana
dataset['Umidade'].describe()

mediana = sts.median(dataset['Umidade'])
mediana

#substituir NAN por mediana
dataset['Umidade'].fillna(mediana, inplace=True)

#Verificamos se NAN não existem mais
dataset['Umidade'].isnull().sum()

#Vento
#remover nas e substiutir pela mediana
dataset.groupby(['Vento']).size()

#substituir NAN por mediana
dataset['Vento'].fillna('FALSO', inplace=True)
#Verificamos se NAN não existem mais
dataset['Vento'].isnull().sum()

#Aparencia
dataset.groupby(['Aparencia']).size()

dataset.loc[dataset['Aparencia'] ==  'menos', 'Aparencia'] = "sol"

dataset.groupby(['Aparencia']).size()

#Temperatura fora do dominio
dataset['Temperatura'].describe()

#visualizar 
dataset.loc[(dataset['Temperatura'] <  -130 )  | ( dataset['Temperatura'] >  130) ]

mediana = sts.median(dataset['Temperatura'])
mediana

#substituir
dataset.loc[(dataset['Temperatura'] <  0 )  | ( dataset['Temperatura'] >  120), 'Temperatura'] = mediana

#Umidade fora do dominio
dataset['Umidade'].describe()

#visualizar 
dataset.loc[(dataset['Umidade'] <  0 )  | ( dataset['Umidade'] >  100) ]

mediana = sts.median(dataset['Umidade'])
mediana

dataset.loc[(dataset['Umidade'] < 0) | (dataset['Umidade'] > 100),'Umidade'] = mediana

#visualizar 
dataset.loc[(dataset['Umidade'] <  0 )  | ( dataset['Umidade'] >  100) ]

dataset.head()

dataset.shape

dataset