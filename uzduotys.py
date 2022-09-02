import modules.praejo_nuo_gimtadienio as praejo_laiko
import modules.triukai_su_sarasai as uz8
import modules.biudzetas as biudzetas
import modules.kelemieji_nekelemieji as nekelemieji
# import modules.grafine_sasaja as grafine

import datetime

while True:
    try:
        uzduotis = int(input("""Pasirinkite programa: 
        1-Suzinoti ar ivestas skaicius sveikas, 
        2-Atimti iš dabartinės datos ir laiko 5 dienas
        3-Suzinoti kiek laiko praejo nuo jusu gimtadienio
        4-Suzinokite ar metai yra kelemieji ar ne
        5.Triukai su Sarasais Uzduotys
        6.BIUDZETO PROGRAMA\n"""))

        if uzduotis == 1:
            print("Suzinoti ar ivestas skaicius sveikas")
            try:
                sveikas_skaicius = float(input("Iveskite skaiciu:"))
                if sveikas_skaicius.is_integer():
                    print("Skaicius yra sveikas")
                else:
                    print("Skaicius yra nesveikas")
            except:
                print("Ivedete ne skaiciu")

        if uzduotis == 2:
            print("Atimtis iš dabartinės datos ir laiko 5 dienas")
            now=datetime.datetime.today()
            print(now)
            print(now - datetime.timedelta(days=5))
            print(now + datetime.timedelta(hours=8))
            print(now.strftime("%Y %m %d %X "))

        if uzduotis == 3:
            praejo_laiko.praejo_laiko()

        if uzduotis == 4:
            nekelemieji.ar_kelemieji()

        if uzduotis == 5:
            uz8.triukai()

        if uzduotis == 6:
            biudzetas.biudzetas()

        # if uzduotis == 7:
        #     grafine.grafine_sasaja()
        #


    except:
        print("Nera tokios programos")

