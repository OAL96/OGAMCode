# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 18:46:40 2024

@author: oscar
"""
# Plantilla de Pre Procesado - Datos Faltantes

# Como importar las librerías
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importar el data set

dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 3].values

# Tratamiento de los NAs

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = "mean")
imputer = imputer.fit(X[:,1:3])
X[ : ,1:3] = imputer.transform(X[:,1:3])