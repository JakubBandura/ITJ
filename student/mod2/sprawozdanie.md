# Sprawozdanie: Moduł 2 - Praca z danymi w systemie IoT
**Autor:** Jakub Bandura

## Cel zadania
Celem ćwiczenia było wykorzystanie języka Python, wirtualnego środowiska oraz bibliotek `pandas` i `matplotlib` do wczytania i wizualizacji zbioru danych pochodzącego z domowego systemu IoT (`energydata_complete.csv`).

## Wykonanie
1. **Środowisko:** Zgodnie z instrukcją utworzono wirtualne środowisko `venv` oraz wygenerowano plik `requirements.txt` ze spisem użytych pakietów. Zablokowano wysyłanie środowiska do repozytorium przy użyciu pliku `.gitignore`.
2. **Przetwarzanie danych:** Za pomocą modułu `pandas` i funkcji `read_csv()` wczytano zbiór danych znajdujący się w nadrzędnym katalogu projektu.
3. **Wizualizacja:** Przy użyciu `matplotlib` wygenerowano różnorodne wykresy podsumowujące wybrane kolumny z pliku CSV (m.in. wykres liniowy ukazujący zmienność parametrów w czasie oraz histogram pokazujący dystrybucję danych). Wykresy zostały poprawnie wyeksportowane do formatu PNG.

## Wnioski
Narzędzia takie jak *pandas* oraz *matplotlib* w połączeniu ze środowiskiem Visual Studio Code pozwalają na szybką i wygodną analizę dużych zbiorów danych (jak logi z systemów IoT).