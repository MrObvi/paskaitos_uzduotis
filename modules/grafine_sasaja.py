from tkinter import *

langas = Tk()
langas.title("Biudzetas 300")
langas.geometry("500x250")

saugojimas= []
def atvaizduoti():
    ivedimas = ivestis.get()
    rezultatas["text"] =f"Labas, {ivedimas}"
    apacia["text"]="Sukurta"
    saugojimas.append(ivedimas)
    ivestis.delete(0,'end')

    return saugojimas

def isvalyti():
    ivedimas = ivestis.get()

    rezultatas["text"] =f"Labas, {ivedimas}"
    # rezultatas.destroy()
    ivestis.delete(0,'end')
    apacia["text"] = "Isvalyta"
def atkurit():
    ivesties_isaugojimas = saugojimas[-1]
    rezultatas["text"] = f"Labas, {ivesties_isaugojimas}"
    apacia["text"] = "Atkurta"
    langas.bind("<Escape>", lambda event: iseiti())
    ivestis.insert(0,ivesties_isaugojimas)
    print(ivesties_isaugojimas)

def iseiti():
    langas.quit()

menu_langas = Menu(langas)
langas.config(menu=menu_langas)
submenu = Menu(menu_langas, tearoff=0)

menu_langas.add_cascade(label="Meniu", menu=submenu)
submenu.add_command(label="Isvalyti", command=isvalyti)
submenu.add_command(label="Atkurti paskurini", command=atkurit)
submenu.add_separator()
submenu.add_command(label="Iseiti", command=iseiti)

apacia=Label(langas, text="", bd=1, relief=SUNKEN, anchor=W)


ivestis_vardas = Label(text="Iveskite vardas")
ivestis = Entry()

mygtukas= Button(text="Patvirtinti", command=atvaizduoti)
langas.bind("<Return>", lambda event: atvaizduoti() )
rezultatas = Label(text="")

ivestis_vardas.pack()
ivestis.pack()
rezultatas.pack()
mygtukas.pack()
apacia.pack(side=BOTTOM, fill=X)
langas.mainloop()
