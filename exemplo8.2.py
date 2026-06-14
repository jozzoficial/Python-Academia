import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
  
def detectar_outliers_iqr (data): 
    Q1 = np.percentile(data, 25) 
    Q3 = np.percentile(data, 75) 
    IQR = Q3 - Q1 
     
    limite_inferior = Q1 - 1.5 * IQR 
    limite_superior = Q3 + 1.5 * IQR 
     
    outliers = data[(data < limite_inferior) | (data > limite_superior)] 
    return outliers, limite_inferior, limite_superior 
  
# Dados de exemplo com outliers 
dados_salarios = np.array([ 
    30000 , 35000 , 40000 , 42000 , 45000 , 50000 , 52000 , 55000 , 60000 , 65000 , 
    70000 , 75000 , 80000 , 85000 , 90000 , 150000 , 20000 , 1000000 # 150k, 
20k, 1M são outliers 
]) 
  
print ("\n--- Detecção de Outliers com IQR ---") 
print (f"Dados originais: {dados_salarios }") 
  
outliers, li, ls = detectar_outliers_iqr(dados_salarios) 
  
print (f"\nQ1: {np.percentile(dados_salarios, 25):.2f }") 
print (f"Q3: {np.percentile(dados_salarios, 75) :.2f }") 
print (f"IQR: {ls - li :.2f }") 
print (f"Limite Inferior: { li :.2f }") 
print (f"Limite Superior: { ls :.2f }") 
print (f"Outliers detectados: {outliers }") 
  
# Visualização com Box Plot 
plt.figure( figsize =(8, 5)) 
sns.boxplot( x=dados_salarios) 
plt.title( 'Box Plot de Salários com Outliers' ) 
plt.xlabel( 'Salário' ) 
plt.show() 
