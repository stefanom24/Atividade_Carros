#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 09:59:28 2024

@author: stefano
"""

#%%
import pandas as pd

#%%
carros = pd.read_csv('base_carros_usados.csv', decimal=',')

#%%
carros.info()

#%%
carros = carros.rename(columns={'car_name':'nome_carro',
                                'brand':'marca',
                                'model':'modelo',
                                'new_price':'preco_novo',
                                'min cost_price':'custo_minimo',
                                'max_cost_price':'custo_maximo',
                                'vehicle age':'idade_veiculo',
                                'km_driven':'km_dirigidos',
                                'seller_type':'tipo_vendedor',
                                'fuel_type':'tipo_combustivel',
                                'transmission_type':'tipo_transmissao',
                                'mileage':'milhagem',
                                'engine':'motor',
                                'max power':'poder_maximo',
                                'seats':'assentos',
                                'selling price':'preco_venda'})
#%%
carros.info()
#%%
carros.head(5)
#%%
carros.tail(5)
#%%
carros.isnull().sum()
#%%
carros_vazios = carros.isnull()
carros_preco_novo = carros_vazios[carros_vazios['preco_novo'] == True].index
#%%
carros_custo_minimo = carros_vazios[carros_vazios['custo_minimo'] == True].index
#%%
carros_custo_maximo = carros_vazios[carros_vazios['custo_maximo'] == True].index
#%%
carros = carros.drop(carros_preco_novo)
carros.isnull().sum()
#%%
carros = carros.drop(carros_custo_minimo)
carros.isnull().sum()
#%%
carros = carros.drop(carros_custo_maximo)
carros.isnull().sum()

#%%
carros = carros.reset_index(drop=True)
#%%
carros_tata = carros[carros['marca'] == 'Tata'].index
carros = carros.drop(carros_tata)
#%%
carros.reset_index(drop=True)
#%%
carros.loc[(carros['tipo_vendedor'] == 'Individual'), ['tipo_vendedor']] = 'particular'
#%%
carros.loc[(carros['tipo_vendedor'] == 'Trustmark Dealer'), ['tipo_vendedor']] = 'concessionaria'
#%%
carros.loc[(carros['tipo_vendedor'] == 'Dealer'), ['tipo_vendedor']] = 'distribuidora'
#%%
carros['ipva'] = 1
#%%
carros.loc[(carros['idade_veiculo'] < 20), ['ipva']] = carros['preco_venda'] * 0.04
#%%
carros.loc[(carros['idade_veiculo'] >= 20), ['ipva']] = 0

#%%
isento = carros[carros['ipva'] == 0].index

#%%
carros['km_por_ano'] = carros['km_dirigidos'] / carros['idade_veiculo']
#%%
carros['fabricacao'] = 2024 - carros['idade_veiculo']

#%%
print(carros)
#%%
carros.to_csv('carros_usados_atualizados.csv')
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%
#%%