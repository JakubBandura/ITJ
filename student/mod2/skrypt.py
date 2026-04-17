import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

script_dir = Path(__file__).resolve().parent
file_path = script_dir.parent.parent / 'energydata_complete.csv'

try:
    df = pd.read_csv(file_path, parse_dates=['date'])
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df = df.dropna(subset=['date'])

    numeric = df.select_dtypes(include=['number']).apply(pd.to_numeric, errors='coerce')
    if numeric.empty:
        raise ValueError('Brak numerycznych kolumn do analizy.')

    daily_mean = df.set_index('date').resample('D').mean()
    hourly_mean = df.set_index('date').groupby(df['date'].dt.hour).mean()
    correlation = daily_mean.corr()

    selected = [col for col in ['Appliances', 'lights', 'T_out', 'RH_out'] if col in daily_mean.columns]
    if selected:
        plt.figure(figsize=(12, 6))
        for col in selected:
            plt.plot(daily_mean.index, daily_mean[col], label=col)
        plt.title('Średnie dobowe: Appliances, lights, T_out, RH_out')
        plt.xlabel('Data')
        plt.ylabel('Wartość średnia')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig('agregacja_dobowa.png')
        plt.close()

    if 'Appliances' in daily_mean.columns:
        plt.figure(figsize=(10, 5))
        plt.hist(daily_mean['Appliances'].dropna(), bins=30, color='orange', edgecolor='black')
        plt.title('Histogram średniego zużycia Appliances (dobowego)')
        plt.xlabel('Średnie dobowe Appliances')
        plt.ylabel('Liczba dni')
        plt.tight_layout()
        plt.savefig('histogram_appliances.png')
        plt.close()

    if not correlation.empty:
        plt.figure(figsize=(14, 12))
        plt.imshow(correlation, cmap='coolwarm', vmin=-1, vmax=1)
        plt.colorbar(label='Współczynnik korelacji')
        ticks = np.arange(len(correlation.columns))
        plt.xticks(ticks, correlation.columns, rotation=90)
        plt.yticks(ticks, correlation.columns)
        plt.title('Mapa korelacji pomiędzy numerycznymi pomiarami (średnie dobowe)')
        plt.tight_layout()
        plt.savefig('heatmap_korelacji.png')
        plt.close()

    daily_mean.to_csv('daily_mean.csv')
    hourly_mean.to_csv('hourly_mean.csv')
    correlation.to_csv('correlation_daily_mean.csv')

    print('Wykresy zostały wygenerowane: agregacja_dobowa.png, histogram_appliances.png, heatmap_korelacji.png')
    print('Dodatkowe pliki: daily_mean.csv, hourly_mean.csv, correlation_daily_mean.csv')

except FileNotFoundError:
    print(f'Błąd: Nie znaleziono pliku {file_path}. Sprawdź, czy CSV jest w głównym folderze.')
except Exception as error:
    print(f'Błąd: {error}')
