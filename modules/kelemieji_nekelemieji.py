def ar_kelemieji():
    print("Suzinokite ar metai yra kelemieji ar ne")

    def ar_klemieji():
        metai = int(input("Iveskite metus:"))

        if metai % 400 == 0 and metai % 100 == 0:
            print("Kelemieji metai")
        elif metai % 4 == 0 and metai % 100 != 0:
            print("Kelemieji metai")
        else:
            print("Nekelemieji metai")
        return metai

    ar_klemieji()