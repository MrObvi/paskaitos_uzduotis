from tkinter import *

langas= Tk()
langas.geometry("1000x500")

zurnalas = []


def islaidos():
    islaidos = [x for x in zurnalas if x < 0]
    if not islaidos:
        rezultatas['text'] = f"Islaidu nerasta"
    else:
        rezultatas['text'] = f"Jusu Islaidos {islaidos}"

    print(f"""----Jusu Islaidos----
  {list(islaidos)}""")

def pajamos():
    pajamos = [x for x in zurnalas if x > 0]
    if not pajamos:
        rezultatas['text'] = f"Pajamu nerasta"
    else:
        rezultatas['text'] =f"Jusu Pajamos: {pajamos} "

    print(f"""----Jusu Pajamos----
  {list(pajamos)}""")

def viskas():
    viskas = [x for x in zurnalas]
    rezultatas['text']=f"Jusu Pajamos ir islaidos: {viskas}"
    print(f"""----Pajamos ir Islaidos----
  {list(viskas)}""")
def ivedimo_veiksmas():
    ivestis = int(ivedimas.get())
    zurnalas.append(ivestis)
    ivedimas.delete(0,'end')

def balansas():
    rezultatas['text'] = sum(zurnalas)
    print(f"""---Jusu balansas---
    #     {sum(zurnalas)}""")


pranesimas=Label(text="Iveskite pajamas arba islaidas")
ivedimas = Entry()
mygtukas_ivestis=Button(text="Patvirtinti", command=ivedimo_veiksmas)
mygtukas_ataskaita=Button(text="Perziureti atsakaita", command=viskas)
mygtukas_pajamos=Button(text="Perziureti pajamas", command=pajamos)
mygtukas_islaidos=Button(text="Perziureti Islaidas", command=islaidos)
mygtukas_balansas=Button(text="Perziureti Balansa", command=balansas)

rezultatas=Label(text="")

pranesimas.pack()
ivedimas.pack()
mygtukas_ivestis.pack()
mygtukas_ataskaita.pack()
mygtukas_pajamos.pack()
mygtukas_islaidos.pack()
mygtukas_balansas.pack()
rezultatas.pack()
langas.mainloop()



#
# while True:
#
#     try:
#
#
#
#         pasirinkimas = int(input("""Mini Biudzetas 3000
#
#     ====Pasirinkite====
#      1. Iveskite pajamas arba islaidas
#      2. Parodyti pajamu islaidu balansa
#      3. Perziureti pajamu islaidu ataskaita
#      4. Gristi i pagrindini menu
#
#        \n """))
#
#         if pasirinkimas == 1:
#
#             while True:
#
#                 ivestis = int(input("Iveskite islaidas arba pajamas jei norite gristi i menu spauskite 0\n"))
#                 if ivestis == 0:
#                     break
#                 zurnalas.append(ivestis)
#
#         if pasirinkimas == 2:
#             print(f"""---Jusu balansas---
#     {sum(zurnalas)}""")
#         if pasirinkimas == 3:
#             pasirinkimas2 = int(input("""1. Pajamu/Islaidu
#     2.Islaidu
#     3.Pajamu\n"""))
#             if pasirinkimas2 == 1:
#                 viskas()
#             if pasirinkimas2 == 2:
#                 islaidos()
#             if pasirinkimas2 == 3:
#                 pajamos()
#         if pasirinkimas == 4:
#             print("----Programa uzdaroma----")
#             break
#     except:
#         print("---Ivyko labai didele klaida, sulauzete programa!---")
