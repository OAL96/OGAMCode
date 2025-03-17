# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 18:44:47 2024

@author: oscar
"""
# Plantilla de Pre Procesado - Datos Catgóricos

# Como importar las librerías
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importar el data set

dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 3].values

# Codificar Datos Categóricos

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
labelencoder_X = LabelEncoder()
X[ : , 0] = labelencoder_X.fit_transform(X[ : , 0])
columntransformer = ColumnTransformer([("Country", OneHotEncoder(), [0])], remainder='passthrough')
X = columntransformer.fit_transform(X)
labelencoder_Y = LabelEncoder()
Y = labelencoder_Y.fit_transform(Y)