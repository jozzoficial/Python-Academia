import pandas as pd
import time
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# Carregar dataset
df = pd.read_csv("mhia_dataset_treino.csv")
print(df)
# Codificar dados categóricos
for col in df.select_dtypes(include="object").columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])

X = df.drop("produto", axis=1)
y = df["produto"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# ID3
id3 = DecisionTreeClassifier(criterion="entropy", max_depth=3)
start = time.time()
id3.fit(X_train, y_train)
tempo_id3 = time.time() - start
y_pred=id3.predict(X_test)
y_pred_id3prob=id3.predict_proba(X_test)

# CART
cart = DecisionTreeClassifier(criterion="gini", max_depth=3)
start = time.time()
cart.fit(X_train, y_train)
tempo_cart = time.time() - start
y_pred=cart.predict(X_test)
y_pred_prob=cart.predict_proba(X_test)
print("ID3 nós:", id3.tree_.node_count)
print("CART nós:", cart.tree_.node_count)
print(f"Tempo ID3: {tempo_id3}")
print(f"Tempo Cart: {tempo_cart}")

plt.figure(figsize=(14,8))
plot_tree(id3, feature_names=X.columns, filled=True)
plt.title("Árvore ID3")
#plt.show()

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
CM=confusion_matrix(y_test,y_pred)
print(CM)
ConfusionMatrixDisplay(confusion_matrix=CM).plot()
plt.title("Matrix De Confusão")
plt.show()