
from statistics import median,mean
variantas=int(input("""Pasirinkite uzduoti
1. Prie kiekvieno sakinio "The Zen of Python" žodžio pridės šauktuką ir atspausdins naują sakinį.
2. Uzduotys su sarasais
3.
4.
"""))

if variantas==1:
    try:
        variantas2=int(input("""Pasirinkite sprendimo buda:
        1. Comprehension variantas
        2. Su map ir lambda variantas"""))
        sakinys="The Zen of Python"
        if variantas2 == 1:
            try:
                # comprehension variantas
                print("""SPRENDIMAS
pridet_sauktuka=[x + "!" for x in sakinys.split()]
naujas_sakinys1 = " ".join(pridet_sauktuka1)\n""")
                pridet_sauktuka1=[x + "!" for x in sakinys.split()]
                naujas_sakinys1 = " ".join(pridet_sauktuka1)
                print(naujas_sakinys1)
            except:
                print("klaida")
        if variantas2 == 2:
            try:
                # comprehension variantas
                print("""SPRENDIMAS
pridet_sauktuka= map(lambda x: x+"!",sakinys.split())
naujas_sakinys= " ".join(pridet_sauktuka)\n""")
                # su map ir lambda variantas
                pridet_sauktuka = map(lambda x: x + "!", sakinys.split())
                naujas_sakinys = " ".join(pridet_sauktuka)
                print(naujas_sakinys)
            except:
                print("klaida")

    except:
        print("klaida")


if variantas==2:
    try:

        sarasas=[ x + 1 for x in range(0,50)]
        print("Sukurtų sąrašą iš skaičių nuo 0 iki 50 \n",sarasas)
        sarasas2 = [x * 10 for x in sarasas]
        print("Padaugintų visus sąrašo skaičius iš 10 ir atspausdintų \n", sarasas2)
        sarasas3 = [x for x in sarasas if x % 7 == 0]
        print("Atrinktų iš sąrašo skaičius, kurie dalinasi iš 7 ir atspausdintų \n", sarasas3)
        sarasas4 = [x**2 for x in sarasas]
        print("Pakeltų visus sąrašo skaičius kvadratu ir atspausdintų \n", sarasas4)
        sarasas5 = [x for x in sarasas4]
        print(f"Su kvadratų sąrašu atliktų šiuos veiksmus: atspausdintų sumą: {sum(sarasas5)}, mažiausią: {min(sarasas5)}  ir didžiausią skaičių: {max(sarasas5)} , vidurkį: {mean(sarasas5)} , medianą: {median(sarasas5)} \n")
        sarasas5 = sorted(sarasas4, reverse=True)
        print("Pakeltų visus sąrašo skaičius kvadratu ir atspausdintų \n", sarasas5)



    except:
        print("klaida")

if variantas==3:
    try:
        sarasas6 = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]
        skaiciu_suma=sum([x for x in sarasas6 if type(x) is int])
        print("Paskaičiuotų ir atspausdintų visų sąrašo skaičių sumą",skaiciu_suma)
        saraso_zodziai = [x for x in sarasas6 if type(x) is str]
        zodziu_sujungimas = " ".join(saraso_zodziai)
        print("Paskaičiuotų ir atspausdintų visų sąrašo skaičių sumą", zodziu_sujungimas)
        boolen_suma = sum([x for x in sarasas6 if type(x) is bool(True)])
        print("Suskaičiuotų ir atspausdintų, kiek sąraše yra loginių (boolean) kintamųjų su True reikšme", boolen_suma)

    except:
        print("klaida")

if variantas==4:
    try:
        class Zmogus:
            def __init__(self, vardas, amzius):
                self.vardas=vardas
                self.amzius=amzius
            def __repr__(self):
                print(self.vardas,self.amzius)


        zmogus_sarasas = []
        zmogus1 = Zmogus("Paulius", 10)
        zmongus2 = Zmogus("Jonas", 5)

        zmogus_sarasas.append(zmogus1.vardas)
        zmogus_sarasas.append(zmongus2.vardas)
        zmogus_sarasas.append(zmogus1.amzius)
        zmogus_sarasas.append(zmongus2.amzius)




        print(zmogus_sarasas)




    except:
        print("klaida")
