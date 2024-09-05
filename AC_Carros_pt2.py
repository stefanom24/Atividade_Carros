#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 08:38:07 2024

@author: stefano
"""

#%%
import pandas as pd
#%%
carros_2 = pd.read_csv('carros_usados_atualizados.csv', decimal=',')
carros_2.info()
#%%
freq_marca = carros_2['marca'].value_counts()
freq_marca.plot.bar(title='Frequência das Marcas')

# Análise: Marcas como Maruti e Hyundai dominam o mercado, com uma presença significativa em relação às outras.
#%%
freq_modelo = carros_2['modelo'].value_counts()
freq_modelo.plot.bar(title='Frequência dos Modelos', figsize=(20,20))

# Análise: O modelo "i20" da Hyundai e "City" da Honda aparecem com maior frequência, o que sugere que são modelos populares entre os veículos usados.
#%%
freq_tipo_combustivel = carros_2['tipo_combustivel'].value_counts()
freq_tipo_combustivel.plot.bar( title='Frequência dos Tipos de Combustível')

# Análise: Veículos com combustível a gasolina são dominantes, seguidos por diesel. Veículos movidos a gás natural (CNG) representam uma pequena fração.
#%%
freq_tipo_transmissao = carros_2['tipo_transmissao'].value_counts()
freq_tipo_transmissao.plot.bar( title='Frequência dos Tipos de Transmissão')

# Análise: A transmissão manual é amplamente mais comum do que a automática, o que pode refletir as preferências de custo-benefício dos consumidores.
#%%
freq_assentos = carros_2['assentos'].value_counts()
freq_assentos.plot.bar(title='Frequência dos Assentos')

# Análise: A maioria dos veículos possui 5 assentos, com alguns tendo mais assentos, provavelmente SUVs ou vans, e um pequeno número de veículos especiais com menos assentos.
#%%
agrupamento = carros_2.groupby(['marca', 'tipo_combustivel'])['preco_venda'].mean().unstack()

#%%
agrupamento.plot(kind='bar', figsize=(10,6), title='Preço médio de venda por marca e tipo de combustível', ylabel='Preço médio de venda', rot=90)

# Análise: Marcas premium como BMW e Mercedes-Benz têm preços médios de venda significativamente maiores, especialmente para veículos movidos a diesel.
#%%
combustivel_transmissao_cruzado = pd.crosstab(carros_2['tipo_combustivel'], carros_2['tipo_transmissao'])

#%%
combustivel_transmissao_cruzado.plot.bar(stacked=True, title='Tipo de combustível vs Tipo de transmissão', ylabel='Contagem')

# Análise: A maioria dos carros a gasolina e diesel tem transmissão manual, com uma fração menor, especialmente para gasolina, possuindo transmissão automática.
#%%
correlacao = carros_2[['preco_venda', 'idade_veiculo', 'km_dirigidos', 'motor', 'poder_maximo']].corr()
#%%
print("Matriz de correlação:")
print(correlacao)
#%%
# Análise:
# - O preço de venda tem uma forte correlação com o poder máximo do veículo e o tamanho do motor.
# - A idade do veículo apresenta uma correlação negativa com o preço de venda, o que indica que veículos mais antigos tendem a ser vendidos por valores menores.
# - Quilometragem (km dirigidos) tem uma correlação baixa com o preço, sugerindo que outros fatores, como potência do motor, desempenham um papel maior no valor de venda.

#%%
carros_2.plot.scatter(x='idade_veiculo', y='preco_venda', title='Relação entre Idade do Veículo e Preço de Venda')

#%%
# Análise: 
# - Veículos mais antigos tendem a ter um preço de venda menor, conforme esperado. Porém, há algumas exceções, indicando que marcas premium podem reter valor mesmo com a idade.
#%% 

#Tentativas de boxplot que não funcionaram a não que showfliers é igual a False.

carros_2[['preco_venda']].plot.box(title='Boxplot do Preço de Venda', showfliers=False)
carros_2[['preco_venda']].describe().round(2)
#%%
carros_2[['km_dirigidos']].plot.box(title='Boxplot da Quilometragem Dirigida',  showfliers=False)
carros_2[['km_dirigidos']].describe().round(2)
#%%
carros_2[['idade_veiculo']].plot.box(title='Boxplot da Idade do Veículo',  showfliers=False)
carros_2[['idade_veiculo']].describe().round(2)
#%%
carros_2[['motor']].plot.box(title='Boxplot da Capacidade do Motor',  showfliers=False)
carros_2[['motor']].describe().round(2)
#%%
carros_2[['poder_maximo']].plot.box(title='Boxplot da Potência Máxima do Motor',  showfliers=False)
carros_2[['poder_maximo']].describe().round(2)
#%%
#%%
#%%
#%%
#%%
#%%