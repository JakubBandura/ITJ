# Sprawozdanie: Moduł 2 - Zaawansowana analiza danych w systemie IoT
**Autor:** Jakub Bandura

## Cel zadania
Celem ćwiczenia było wykorzystanie języka Python oraz bibliotek `pandas` i `matplotlib` do zaawansowanego przetwarzania, czyszczenia i analizy wzorców w dużym zbiorze danych pochodzącym z domowego systemu czujników IoT (`energydata_complete.csv`).

## Proces przetwarzania danych (Data Preprocessing)
Zamiast rysować surowe dane, zaimplementowano kroki czyszczenia i agregacji:
1. Przekonwertowano kolumnę tekstową z datą na odpowiedni typ `datetime`, usuwając przy tym błędne wiersze.
2. Odfiltrowano wyłącznie kolumny numeryczne.
3. Wykorzystano funkcję `resample('D').mean()` do zagregowania tysięcy pomiarów do postaci uśrednionych wartości dobowych, co znacząco zredukowało szum informacyjny.

## Analiza wyników i wizualizacja

### 1. Trend i sezonowość (Wykres Liniowy)
Na poniższym wykresie zestawiono zagregowane dobowe średnie dla zużycia energii (urządzenia, światło) oraz warunków zewnętrznych (temperatura i wilgotność). Agregacja pozwoliła zaobserwować rzeczywiste, długoterminowe trendy zachodzące w badanym okresie.

![Agregacja Dobowa](agregacja_dobowa.png)

### 2. Rozkład zużycia energii (Histogram)
Histogram prezentuje dystrybucję dobowego zapotrzebowania na energię dla głównych urządzeń (Appliances). Pozwala to łatwo zidentyfikować, jaki poziom zużycia występuje najczęściej (wartości typowe) oraz zidentyfikować ewentualne wartości skrajne (dni o nietypowo wysokim poborze).

![Histogram Zużycia Prądu](histogram_appliances.png)

### 3. Poszukiwanie zależności (Mapa Korelacji)
Aby zbadać liniowe relacje między wszystkimi czujnikami w inteligentnym domu, wygenerowano mapę korelacji (Heatmap). Intensywność kolorów pozwala błyskawicznie wychwycić parametry, które są ze sobą silnie powiązane (np. warunki pogodowe a zużycie prądu).

![Mapa Korelacji](heatmap_korelacji.png)

## Wnioski
Zastosowanie biblioteki *pandas* do resamplingu danych oraz filtrowania typów okazało się kluczowe przy pracy z rzeczywistymi logami IoT. Odpowiednie przetworzenie danych przed ich narysowaniem (narzędziem *matplotlib*) nie tylko poprawia czytelność wykresów, ale pozwala wyciągać konkretne wnioski biznesowe i fizyczne, niemożliwe do zauważenia w surowym gąszczu logów. Dołączone pliki `.csv` stanowią świetną bazę pod ewentualne trenowanie modeli uczenia maszynowego.