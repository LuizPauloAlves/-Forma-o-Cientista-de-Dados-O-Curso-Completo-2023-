import pandas as pd
import seaborn as srn
import statistics  as sts

"""Importando os dados e visualizando"""

#importar dados
dataset = pd.read_csv("dados.csv", sep=";")
#visulizar
dataset.head()

dataset.shape

"""Exploração dos dados"""

dataset.groupby(['MUNICIPIO']).size()

i = 'PIB'
print(dataset[i].describe())
srn.boxplot(dataset[i]).set_title(i)

i = 'VALOREMPENHO'
print(dataset[i].describe())
srn.boxplot(dataset[i]).set_title(i)

"""Verificar se tem valores NAN e se tem valores duplicados"""

dataset.isnull().sum()

dataset[dataset.duplicated(['CODIGO'], keep=False)]

dataset.drop_duplicates(subset = 'CODIGO', keep = 'first', inplace=True)

dataset[dataset.duplicated(['CODIGO'], keep=False)]

"""PIB e VALOREMPENHO apresentaram outlier"""

desv = sts.stdev(dataset['PIB'])
dataset.loc[dataset['PIB'] >= 2*desv]

mediana = sts.median(dataset['PIB'])
dataset.loc[dataset['PIB'] >= 2*desv, 'PIB'] = mediana
dataset.loc[dataset['PIB'] >= 2*desv]

desv = sts.stdev(dataset['VALOREMPENHO'])
dataset.loc[dataset['VALOREMPENHO'] >= 2*desv]

mediana = sts.median(dataset['VALOREMPENHO'])
dataset.loc[dataset['VALOREMPENHO'] >= 2*desv, 'VALOREMPENHO'] = mediana
dataset.loc[dataset['VALOREMPENHO'] >= 2*desv]

"""Apresentação dos dados"""

srn.boxplot(dataset.PIB).set_title('PIB')

srn.histplot(dataset.PIB, kde = True, bins = 7).set(title = 'PIB')

srn.boxplot(dataset.VALOREMPENHO).set_title('Valor Empenho')

srn.histplot(dataset.VALOREMPENHO, kde = True, bins = 7).set(title = 'Valor Empenho')