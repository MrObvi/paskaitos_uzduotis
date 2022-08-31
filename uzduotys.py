import datetime
while True:
    try:
        uzduotis = int(input("""Pasirinkite uzduoti: 
        1-Suzinoti ar ivestas skaicius sveikas, 
        2-Atimti iš dabartinės datos ir laiko 5 dienas
        3-Suzinoti kiek laiko praejo nuo jusu gimtadienio \n"""))

        if uzduotis == 1:
            print("Suzinoti ar ivestas skaicius sveikas")
            try:
                sveikas_skaicius = int(input("Iveskite skaiciu:")) > 0
                if sveikas_skaicius == True:
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

            print("Suzinoti kiek laiko praejo nuo jusu gimtadienio")
            try:
                gimtadienis_ivedimas=input("Iveskite tikslia gimimo data bei laika tokiu formatu 2000-00-00  :")
                gimtadienis = datetime.datetime.strptime(gimtadienis_ivedimas, "%Y-%m-%d")
                print(f"Tavo gimtadienis: {gimtadienis}")
                # Palikta testavimui
                # gimtadienis = datetime.datetime(1991,6,30,0,0,0)

            except:
                print("Neteisingai ivedete data ar laika")
                break
            now = datetime.datetime.today()
            print(f"Dabartinis laikas: ({now}")

            rezultatas = now - gimtadienis

            print(f"Praejo metu: {now.year - gimtadienis.year}")
            print()
            print(f"Praejo menesiu: {round(rezultatas.total_seconds() / 2629746)}")
            print(f"Praejo menesiu: {rezultatas.days/30}")
            print(f"Praejo dienu: {round(rezultatas.total_seconds() / 86400)}")
            print(f"Praejo dienu: {rezultatas.days}")
            print(f"Praejo valandu: {round(rezultatas.total_seconds() / 3600)}")
            print(f"Praejo minuciu: {round(rezultatas.total_seconds() / 60)}")
            print(f"Praejo sekundziu: {round(rezultatas.total_seconds())}")

    except:
        print("Nera tokios uzduoties")
