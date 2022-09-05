from PIL import Image
# Pirma uzduotis
im=Image.open("logo.png")
box=(0,28,128,100)
croping=im.crop(box)
croping.show()
croping.save("naujas-logo.png")