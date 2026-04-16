import pandas as pd
import matplotlib.pyplot as plt

file_path = '../../energydata_complete.csv'

try:
 
    df = pd.read_csv(file_path)
    
    col1 = df.columns[1]
    col2 = df.columns[2]

    # Wykres liniowy (pierwsze 200 pomiarów)
    plt.figure(figsize=(10, 5))
    plt.plot(df[col1].head(200), label=col1, color='blue')
    plt.title(f'Wykres liniowy: {col1}')
    plt.xlabel('Numer pomiaru')
    plt.ylabel('Wartość')
    plt.legend()
    plt.grid(True)
    plt.savefig('wykres_liniowy.png')
    plt.close()

    # Histogram
    plt.figure(figsize=(10, 5))
    plt.hist(df[col2].dropna(), bins=30, color='orange', edgecolor='black')
    plt.title(f'Histogram dla: {col2}')
    plt.xlabel('Wartość')
    plt.ylabel('Liczba wystąpień')
    plt.savefig('histogram.png') 
    plt.close()

    print("Wykresy (wykres_liniowy.png i histogram.png) zostały wygenerowane.")

except FileNotFoundError:
    print(f"Błąd: Nie znaleziono pliku {file_path}. Sprawdź, czy CSV jest w głównym folderze.")