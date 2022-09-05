from tkinter import *

langas = Tk()
langas.geometry("500x200")


def ar_klemieji():
    metai = int(ivestis.get())

    if metai % 400 == 0 and metai % 100 == 0:
        rezultatas["text"]="Kelemieji metai"
        print("Kelemieji metai")
    elif metai % 4 == 0 and metai % 100 != 0:
        rezultatas["text"] = "Kelemieji metai"
        print("Kelemieji metai")
    else:
        rezultatas["text"] = "Nekelemieji metai"
        print("Nekelemieji metai")
    ivestis.delete(0, 'end')

metu_lable=Label(text="Iveskite metus")
ivestis=Entry()
mygtukas=Button(text="Tikrinti", command=ar_klemieji)
rezultatas=Label(text="")

metu_lable.pack()
ivestis.pack()
mygtukas.pack()
rezultatas.pack()
langas.mainloop()

