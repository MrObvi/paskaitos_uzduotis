import os
from PIL import Image

#Norint kad programa veiktu, reikia nurodyti kataloga su nuotraukomis
your_url= "C:\\Users\\"

print(os.listdir(your_url))
nuotraukos=[]

for i in os.listdir(your_url):
    if ".jpg" in i or ".png" in i:
        nuotraukos.append(i)
resizer_w = 300
resizer_h = 300
for x in nuotraukos:
    im = Image.open(x)
    sk_proporcija_h=resizer_h/im.size[0]
    sk_proporcija_w=resizer_w/im.size[1]

    dydis_h = int(sk_proporcija_h*resizer_h)
    dydis_w = int(sk_proporcija_w*resizer_w)

    im1=im.resize((dydis_w ,dydis_h))
    im_logo=Image.open("logo_2.png")
    logo_location=(0,0,im_logo.size[0], im_logo.size[1])
    im1.paste(im_logo,logo_location,im_logo)
    im1.show()

print(nuotraukos)