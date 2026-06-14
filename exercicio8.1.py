import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import accuracy_score, classification_report 
  
# Dados de exemplo (reviews de produtos e seus sentimentos) 
dados_reviews = pd.DataFrame({ 
    'review' : [ 
        'Este produto é excelente, adorei!' , 
        'Muito bom, recomendo a todos.' , 
        'Péssima qualidade, dinheiro jogado fora.' , 
        'Funciona bem, mas a bateria dura pouco.' , 
        'Melhor compra que fiz este ano.' , 
        'Não gostei, muito complicado de usar.' , 
        'Atendeu às minhas expectativas, satisfeito.' , 
        'Terrível, nunca mais compro desta marca.' , 
        'Produto razoável pelo preço.' , 
        'Incrível! Superou todas as expectativas.' 
    ], 
    'sentimento' : [ 
        'positivo' , 'positivo' , 'negativo' , 'neutro' , 'positivo' , 
        'negativo' , 'positivo' , 'negativo' , 'neutro' , 'positivo' 
    ] 
}) 
  
# Para simplificar, vamos considerar 'neutro' como 'positivo' ou 
'negativo' para este exercício 
# Ou podemos remover os neutros 
dados_reviews = dados_reviews[dados_reviews[ 'sentimento' ] != 'neutro' ] 
  
X = dados_reviews[ 'review' ] 
y = dados_reviews[ 'sentimento' ] 
  
# Dividir dados em treino e teste 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size =0.3 , 
random_state =42) 
  
print ("\n--- Análise de Sentimento de Reviews (Classificação de Texto) ---") 
  
# Vetorização de texto (TF-IDF) 
# Converte texto em representações numéricas que o modelo pode entender 
vectorizer = TfidfVectorizer( max_features =1000) # Limita o número de 
palavras/features 
X_train_vec = vectorizer.fit_transform(X_train) 
X_test_vec = vectorizer.transform(X_test) 
  
# Treinar um classificador (Regressão Logística) 
model_sentiment = LogisticRegression( max_iter =1000) 
model_sentiment.fit(X_train_vec, y_train) 
  
# Fazer previsões 
y_pred_sentiment = model_sentiment.predict(X_test_vec) 
  
# Avaliar o modelo 
print (f"Acurácia do modelo de sentimento: {accuracy_score(y_test, 
y_pred_sentiment) :.2f }") 
print ("Relatório de Classificação:" ) 
print (classification_report(y_test, y_pred_sentiment)) 
  
# Exemplo de previsão para um novo review 
novo_review = ["Este é um produto mediano, não é bom nem mau." ] 
novo_review_vec = vectorizer.transform(novo_review) 
previsao = model_sentiment.predict(novo_review_vec) 
print (f"\nPrevisão para \"{ novo_review[ 0]}\": {previsao[ 0]}") 
