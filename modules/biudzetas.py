
def biudzetas():
    zurnalas = []


    def islaidos():
        islaidos = [x for x in zurnalas if x < 0]
        print(f"""----Jusu Islaidos----
      {list(islaidos)}""")

    def pajamos():
        pajamos = [x for x in zurnalas if x > 0]
        print(f"""----Jusu Pajamos----
      {list(pajamos)}""")


    def viskas():
        viskas = [x for x in zurnalas]
        print(f"""----Pajamos ir Islaidos----
      {list(viskas)}""")

    while True:

        try:

            pasirinkimas=int(input("""Mini Biudzetas 3000
            
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

            if pasirinkimas == 2:
                print(f"""---Jusu balansas--- 
        {sum(zurnalas)}""")
            if pasirinkimas == 3:
                pasirinkimas2=int(input("""1. Pajamu/Islaidu
        2.Islaidu
        3.Pajamu\n"""))
                if pasirinkimas2 == 1:
                    viskas()
                if pasirinkimas2 == 2:
                    islaidos()
                if pasirinkimas2 == 3:
                    pajamos()
            if pasirinkimas == 4:
                print("----Programa uzdaroma----")
                break
        except:
            print("---Ivyko labai didele klaida, sulauzete programa!---")





