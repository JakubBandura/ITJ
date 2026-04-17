# Sprawozdanie: Moduł 2 - Zaawansowana analiza danych w systemie IoT
**Autor:** Jakub Bandura

## Cel zadania
Celem ćwiczenia było przygotowanie inżynierskiej analizy danych z systemu czujników IoT. Skrypt miał przetworzyć surowy zapis z pliku `energydata_complete.csv`, zidentyfikować sensowne miary oraz zwizualizować je w sposób ułatwiający interpretację i porównanie.

## Przetwarzanie danych
W skrypcie wykonano następujące operacje:
1. Wczytanie pliku CSV i konwersję kolumny `date` do formatu `datetime`.
2. Odfiltrowanie tylko kolumn numerycznych, aby skoncentrować analizę na pomiarach fizycznych i energetycznych.
3. Agregację do wartości dobowych za pomocą `resample('D').mean()`, co redukuje szum krótkookresowy i uwydatnia długoterminowe trendy.
4. Wyliczenie macierzy korelacji dla średnich dobowych, co pozwala ocenić powiązania między parametrami.
5. Zapis wygenerowanych danych do plików:
   - `daily_mean.csv`
   - `hourly_mean.csv`
   - `correlation_daily_mean.csv`

## Wykresy i ich znaczenie
Analiza została przedstawiona za pomocą oddzielnych wykresów dla każdej grupy zmiennych o tej samej jednostce. Taka organizacja jest inżyniersko uzasadniona, ponieważ porównywanie wartości o różnych jednostkach na jednym wykresie prowadzi do zniekształconych interpretacji.

### Wykresy agregacji dobowej według jednostek
Wygenerowano zestawy wykresów, które pokazują dobowe średnie dla grup parametrów posiadających wspólną jednostkę:
- `agregacja_dobowa_degC.png` — wszystkie temperatury (T1–T9, T_out, Tdewpoint)
- `agregacja_dobowa_pct.png` — wszystkie wilgotności (RH_1–RH_9, RH_out)
- `agregacja_dobowa_Wh.png` — zużycie energii (`Appliances`, `lights`)
- `agregacja_dobowa_m_s.png` — prędkość wiatru (`Windspeed`)
- `agregacja_dobowa_km.png` — widoczność (`Visibility`)
- `agregacja_dobowa_mm_Hg.png` — ciśnienie atmosferyczne (`Press_mm_hg`)

Każdy z tych wykresów pokazuje, jak zachowuje się dana klasa pomiarów w czasie. Dzięki temu można np. porównać wzorce temperatur wewnętrznych i zewnętrznych lub obserwować sezonowość wilgotności.

### Histogram zużycia energii AGD
- `histogram_zuzycie_agd.png`

Histogram obrazuje, jak rozkłada się dobowe zużycie energii przez urządzenia AGD. Taki wykres jest przydatny do identyfikacji wartości typowych, odchyleń oraz potencjalnych dni o nadmiernym poborze prądu.

### Mapa korelacji
- `heatmap_korelacji.png`

Mapa korelacji prezentuje powiązania między wszystkimi badanymi zmiennymi w formie macierzy. Dzięki spójnym, polskim etykietom łatwiej wskazać silne zależności, np. między temperaturą zewnętrzną, wilgotnością i zużyciem energii.

## Uzasadnienie inżynierskie
Takie podejście jest typowe w analizie systemów IoT:
- agregacja dobowych średnich upraszcza wielkoskalową analizę i pozwala skupić się na istotnych trendach,
- grupowanie po jednostkach zapobiega błędnym wnioskom wynikającym z mieszania różnych skal,
- mapa korelacji umożliwia szybkie wykrycie zależności, które mogą być podstawą do dalszych modeli predykcyjnych,
- zapis wyników do plików `.csv` zachowuje dane w formacie gotowym na kolejne etapy analizy.

## Wnioski
Skrypt przenosi analizę z poziomu surowych logów do postaci czytelnych wykresów i zbiorów danych. Przetworzenie czasowe oraz podział na grupy jednostek daje praktyczne narzędzie do monitorowania zachowań systemu oraz do późniejszego wykorzystania w modelowaniu predykcyjnym lub optymalizacji zużycia energii.