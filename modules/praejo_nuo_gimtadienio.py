
import datetime
def praejo_laiko():
    while True:

        print("Suzinoti kiek laiko praejo nuo jusu gimtadienio\n")
        try:
            gimtadienis_ivedimas = input("""Iveskite tikslia gimimo data tokiu formatu 2000-00-00
Noredami gristi i menu spauskite 0:""")
            if gimtadienis_ivedimas == "0":
                print("Gristam i menu")
                break
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
        print(f"Praejo menesiu: {rezultatas.days / 30}")
        print(f"Praejo dienu: {round(rezultatas.total_seconds() / 86400)}")
        print(f"Praejo dienu: {rezultatas.days}")
        print(f"Praejo valandu: {round(rezultatas.total_seconds() / 3600)}")
        print(f"Praejo minuciu: {round(rezultatas.total_seconds() / 60)}")
        print(f"Praejo sekundziu: {round(rezultatas.total_seconds())}")