import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

chemin_fichier = "C:\\Users\\ANGE\\Downloads\\MusicAnalysisPython\\Spotify - All Time Top 2000s Mega Dataset\\Spotify-2000.csv"
df = pd.read_csv(chemin_fichier)

print("Premieres 5 ligne dataset :")
print(df.head())

Valeurs_manquantes = df.isnull().sum()
print("\nValeurs manquantes par colonne :")
print(Valeurs_manquantes)


df.fillna({
    col: df[col].median() if np.issubdtype(df[col].dtype, np.number) else df[col].mode()[0]
    for col in df.columns
}, inplace=True)

print("\nStatistiques descriptives :")
print(df.describe())

comptes_genres = df['genre'].value_counts()
print("\nNombre de chansons par genre :")
print(comptes_genres)

genre_dominant = comptes_genres.idxmax()
print(f"Genre le plus représenté dans le top 100 : {genre_dominant}")

plt.figure(figsize=(10, 6))
comptes_genres.plot(kind='bar', color='skyblue')
plt.title('Distribution des genres musicaux')
plt.xlabel('Genre')
plt.ylabel('Nombre de chansons')
plt.show()


df['year'] = pd.to_numeric(df['year'], errors='coerce')
df.dropna(subset=['year'], inplace=True)  
regroupement_annee = df.groupby('year')['listens'].mean()

regroupement_annee.plot(kind='line', figsize=(12, 6), color='green')
plt.title('Nombre moyen d\'écoutes par année')
plt.xlabel('Année')
plt.ylabel('Écoutes moyennes')
plt.show()