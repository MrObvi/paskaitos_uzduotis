import pickle


def biudzetas_picle():

    def islaidos():
        with open("biudzetas.pkl", "rb") as islaida:
            nauja_islaida = pickle.load(islaida)
            islaidos = str([x for x in nauja_islaida if x < 0])
            print(f"Jusu islaidos:{islaidos}")

    def pajamos():
        with open("biudzetas.pkl", "rb") as pajama:
            nauja_pajamos = pickle.load(pajama)
            pajamos = str([x for x in nauja_pajamos if x > 0])
            print(f"Jusu pajamos:{pajamos}")

    def viskas():
        with open("biudzetas.pkl", "rb") as viskas:
            nauja_viskas = pickle.load(viskas)
            viskas = [x for x in nauja_viskas]
            print(f"""----Pajamos ir Islaidos----
            {viskas}""")

    while True:
        try:
            with open("biudzetas.pkl", "rb") as pickle_in:
                zurnalas = pickle.load(pickle_in)
                suma = 0

                print("----Visi irasai:----")
                for skaicius, irasas in enumerate(zurnalas):
                    suma += irasas
                    print(skaicius + 1, irasas)
                print("Balansas:", suma)

        except:
            print("Nepavyko nuskaityt failo")
            zurnalas = []

        try:

            pasirinkimas = int(input("""Mini Biudzetas 3000

        ====Pasirinkite====
         1. Iveskite pajamas arba islaidas
         2. Parodyti pajamu islaidu balansa
         3. Perziureti pajamu islaidu ataskaita
         4. Gristi i pagrindini menu

           \n """))

            if pasirinkimas == 1:

                while True:

                    ivestis = int(input("Iveskite islaidas arba pajamas jei norite gristi i menu spauskite 0\n"))
                    if ivestis == 0:
                        break
                    zurnalas.append(ivestis)
                    try:
                        with open("biudzetas.pkl", "wb") as out_islaidos:
                            pickle.dump(zurnalas, out_islaidos)
                    except:
                        print("Nepavyko irasyti failo")


            if pasirinkimas == 2:
                with open("biudzetas.pkl", "rb") as viskas:
                    nauja_viskas = pickle.load(viskas)
                    print(f"""---Jusu balansas---
{sum(nauja_viskas)} """)
        #         print(f"""---Jusu balansas---
        #
        # {sum(zurnalas)}""")
            if pasirinkimas == 3:
                pasirinkimas2 = int(input("""
        1.Islaidu
        2.Pajamu\n"""))
                # if pasirinkimas2 == 1:
                #     viskas()
                if pasirinkimas2 == 1:
                    islaidos()
                if pasirinkimas2 == 2:
                    pajamos()
            if pasirinkimas == 4:
                print("----Programa uzdaroma----")
                break
        except:
            print("---Ivyko labai didele klaida, sulauzete programa!---")


