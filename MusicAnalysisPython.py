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
    col: df[col].median() if df[col].dtype != '0' else df[col].mode()[0]
    for col in df.columns
}, inplace=True)

print("\nStatistiques descriptives :")
print(df.describe())