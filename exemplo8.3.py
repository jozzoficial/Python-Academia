 import pandas as pd
from scipy.stats import chi2_contingency 
  
# Gerar dados de exemplo (simulados) 
dados_preferencia = pd.DataFrame({ 
    'Genero' : [ 'Masculino' , 'Feminino' , 'Masculino' , 'Feminino' , 
'Masculino' , 'Feminino' , 'Masculino' , 'Feminino' , 'Masculino' , 
'Feminino' , 
               'Masculino' , 'Feminino' , 'Masculino' , 'Feminino' , 
'Masculino' , 'Feminino' , 'Masculino' , 'Feminino' , 'Masculino' , 
'Feminino' ], 
    'Produto_Preferido' : [ 'A' , 'B' , 'A' , 'A' , 'B' , 'B' , 'A' , 'B' , 'A' , 
'A' , 
                          'B' , 'A' , 'B' , 'B' , 'A' , 'A' , 'B' , 'A' , 'B' , 
'B' ] 
}) 
  
print ("\n--- Teste Qui-Quadrado (Associação entre Variáveis Categóricas) ---") 
print ("Primeiras 5 linhas dos dados de preferência:" ) 
print (dados_preferencia.head()) 
  
# Criar uma tabela de contingência 
tabela_contingencia = pd.crosstab(dados_ preferencia[ 'Genero' ], 
dados_preferencia[ 'Produto_Preferido' ]) 
print ("\nTabela de Contingência:" ) 
print (tabela_contingencia) 
  
# Realizar o teste Qui-Quadrado 
chi2, p_value, dof, expected = chi2_contingency(tabela_contingencia) 
  
print (f"\nEstatística Qui-Quadrado: {chi2 :.2f }") 
print (f"Valor p: {p_value :.3f }") 
print (f"Graus de Liberdade (dof): {dof }") 
print ("Frequências Esperadas:" ) 
print (pd.DataFrame(expected, index =tabela_contingencia.index, 
columns =tabela_contingencia.columns)) 
  
alpha = 0.05 # Nível de significância 
if p_value < alpha: 
    print ("\nRejeitamos a hipótese nula: Existe uma associação 
significativa entre Gênero e Preferência por Produto." ) 
else : 
    print ("\nNão rejeitamos a hipótese nula: Não há evidência suficiente 
para uma associação significativa." ) 
