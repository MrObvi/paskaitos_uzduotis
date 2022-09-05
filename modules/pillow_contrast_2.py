from PIL import Image, ImageEnhance

def ikelimas(paveikslelis,exct, kontrastas, spalvingumas, ryskumas):
    imgs=Image.open(paveikslelis + exct)

    kontr=ImageEnhance.Contrast(imgs).enhance(kontrastas)
    colors=ImageEnhance.Color(kontr).enhance(spalvingumas)
    rysk=ImageEnhance.Brightness(colors).enhance(ryskumas)

    imgs.show(), rysk.show()

    pasirinkias=int(input("Ar norite koreguota faila isaugoti? 0-NE, 1-TAIP"))

    if pasirinkias == 1:
        rysk.save(paveikslelis + "_modified" + exct)
        print("Isaugoma")

    if pasirinkias == 0:
        print("Isjungiama")

ikelimas("dog",".jpg",2,2,3)