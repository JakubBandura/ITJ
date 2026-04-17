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

    translations = {
        'Appliances': 'Zużycie energii AGD',
        'lights': 'Zużycie oświetlenia',
        'T1': 'Temperatura 1',
        'RH_1': 'Wilgotność 1',
        'T2': 'Temperatura 2',
        'RH_2': 'Wilgotność 2',
        'T3': 'Temperatura 3',
        'RH_3': 'Wilgotność 3',
        'T4': 'Temperatura 4',
        'RH_4': 'Wilgotność 4',
        'T5': 'Temperatura 5',
        'RH_5': 'Wilgotność 5',
        'T6': 'Temperatura 6',
        'RH_6': 'Wilgotność 6',
        'T7': 'Temperatura 7',
        'RH_7': 'Wilgotność 7',
        'T8': 'Temperatura 8',
        'RH_8': 'Wilgotność 8',
        'T9': 'Temperatura 9',
        'RH_9': 'Wilgotność 9',
        'T_out': 'Temperatura zewnętrzna',
        'Press_mm_hg': 'Ciśnienie atmosferyczne',
        'RH_out': 'Wilgotność zewnętrzna',
        'Windspeed': 'Prędkość wiatru',
        'Visibility': 'Widoczność',
        'Tdewpoint': 'Temperatura punktu rosy'
    }
    units = {
        'Appliances': 'Wh',
        'lights': 'Wh',
        'T1': '°C',
        'RH_1': '%',
        'T2': '°C',
        'RH_2': '%',
        'T3': '°C',
        'RH_3': '%',
        'T4': '°C',
        'RH_4': '%',
        'T5': '°C',
        'RH_5': '%',
        'T6': '°C',
        'RH_6': '%',
        'T7': '°C',
        'RH_7': '%',
        'T8': '°C',
        'RH_8': '%',
        'T9': '°C',
        'RH_9': '%',
        'T_out': '°C',
        'Press_mm_hg': 'mm Hg',
        'RH_out': '%',
        'Windspeed': 'm/s',
        'Visibility': 'km',
        'Tdewpoint': '°C'
    }

    unit_groups = {}
    for col, unit in units.items():
        if col in daily_mean.columns:
            unit_groups.setdefault(unit, []).append(col)

    title_by_unit = {
        '°C': 'Średnie dobowe temperatury',
        '%': 'Średnie dobowe wilgotności',
        'Wh': 'Średnie dobowe zużycia energii',
        'm/s': 'Średnie dobowe prędkości wiatru',
        'km': 'Średnie dobowe widoczności',
        'mm Hg': 'Średnie dobowe ciśnień atmosferycznego',
        'brak jednostki': 'Średnie dobowe wartości bez jednostki'
    }

    filenames = []
    for unit, cols in sorted(unit_groups.items()):
        if not cols:
            continue
        plt.figure(figsize=(12, 6))
        for col in cols:
            label = translations.get(col, col)
            plt.plot(daily_mean.index, daily_mean[col], label=label)
        title = title_by_unit.get(unit, f'Średnie dobowe dla jednostki: {unit}')
        plt.title(title)
        plt.xlabel('Data')
        plt.ylabel(f'Średnia wartość{f" ({unit})" if unit != "brak jednostki" else ""}')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        safe_unit = unit.replace('°', 'deg').replace('%', 'pct').replace(' ', '_').replace('/', '_')
        filename = f'agregacja_dobowa_{safe_unit}.png'
        plt.savefig(filename)
        plt.close()
        filenames.append(filename)

    if 'Appliances' in daily_mean.columns:
        plt.figure(figsize=(10, 5))
        plt.hist(daily_mean['Appliances'].dropna(), bins=30, color='orange', edgecolor='black')
        plt.title('Histogram średniego zużycia energii AGD (dobowego)')
        plt.xlabel('Średnie dobowe zużycie energii AGD (Wh)')
        plt.ylabel('Liczba dni')
        plt.tight_layout()
        plt.savefig('histogram_zuzycie_agd.png')
        plt.close()
        filenames.append('histogram_zuzycie_agd.png')

    generated_files = ', '.join(filenames)
    if not generated_files:
        generated_files = 'Brak wygenerowanych wykresów agregacyjnych.'

    if not correlation.empty:
        plt.figure(figsize=(14, 12))
        plt.imshow(correlation, cmap='coolwarm', vmin=-1, vmax=1)
        plt.colorbar(label='Współczynnik korelacji')
        ticks = np.arange(len(correlation.columns))
        labels = [translations.get(col, col) for col in correlation.columns]
        plt.xticks(ticks, labels, rotation=90)
        plt.yticks(ticks, labels)
        plt.title('Mapa korelacji zmiennych (średnie dobowe)')
        plt.tight_layout()
        plt.savefig('heatmap_korelacji.png')
        plt.close()
        generated_files = f'{generated_files}, heatmap_korelacji.png' if filenames else 'heatmap_korelacji.png'

    daily_mean.to_csv('daily_mean.csv')
    hourly_mean.to_csv('hourly_mean.csv')
    correlation.to_csv('correlation_daily_mean.csv')

    print(f'Wygenerowane pliki: {generated_files}')
    print('Dodatkowe pliki: daily_mean.csv, hourly_mean.csv, correlation_daily_mean.csv')

except FileNotFoundError:
    print(f'Błąd: Nie znaleziono pliku {file_path}. Sprawdź, czy CSV jest w głównym folderze.')
except Exception as error:
    print(f'Błąd: {error}')
