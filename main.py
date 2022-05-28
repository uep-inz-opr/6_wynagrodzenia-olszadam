import pandas as pd
ilosc_wpisywanych = int(input())

imiona = []
wynagrodzenia =[]
for i in range(ilosc_wpisywanych):
    imie_wynagrodzenie = input().split()
    imie = imie_wynagrodzenie[0]
    imiona.append(imie)
    wynagrodzenie = float(imie_wynagrodzenie[1])
    wynagrodzenia.append(wynagrodzenie)

zipped = list(zip(imiona, wynagrodzenia))

dane_pracownikow = pd.DataFrame(zipped, columns=['imie', 'wynagrodzenie_brutto'])

dane_pracownikow["skladka"] = round(dane_pracownikow["wynagrodzenie_brutto"] * 0.0976, 2) + round(dane_pracownikow["wynagrodzenie_brutto"] * 0.015, 2) + round(
    dane_pracownikow["wynagrodzenie_brutto"] * 0.0245, 2)

dane_pracownikow["ubezpieczenie"] = round((dane_pracownikow["wynagrodzenie_brutto"] - dane_pracownikow["skladka"]) * 0.09, 2)

dane_pracownikow["podatek"] = round((round((round(dane_pracownikow["wynagrodzenie_brutto"] - 111.25 - dane_pracownikow["skladka"], 2)) * 0.18, 2) - 46.33) - round(
    (round(dane_pracownikow["wynagrodzenie_brutto"] - dane_pracownikow["skladka"], 2)) * 0.0775, 2), 0)

dane_pracownikow["wyplata"] = round(dane_pracownikow["wynagrodzenie_brutto"] - dane_pracownikow["skladka"] - dane_pracownikow["ubezpieczenie"] - dane_pracownikow["podatek"], 2)

dane_pracownikow["sklad_pracodawcy"] = round(dane_pracownikow["wynagrodzenie_brutto"] * 0.0976, 2) + round(dane_pracownikow["wynagrodzenie_brutto"] * 0.065, 2) + round(
    dane_pracownikow["wynagrodzenie_brutto"] * 0.0193, 2) + round(dane_pracownikow["wynagrodzenie_brutto"] * 0.0245, 2) + round(
    dane_pracownikow["wynagrodzenie_brutto"] * 0.001, 2)

dane_pracownikow["koszt_suma"] = dane_pracownikow["wynagrodzenie_brutto"] + dane_pracownikow["sklad_pracodawcy"]

for x in range(ilosc_wpisywanych):
    print(dane_pracownikow.loc[x, "imie"], " ", dane_pracownikow.loc[x, "wynagrodzenie_brutto"], " ", dane_pracownikow.loc[x, "sklad_pracodawcy"], " ", dane_pracownikow.loc[x, "koszt_suma"])
print(dane_pracownikow["koszt_suma"].sum())
