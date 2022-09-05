from PIL import Image

im=Image.open("dog.jpg")

data=im.getdata()

def riba(sk):
    if sk < 0:
        return 0
    elif sk > 255:
        return 255
    return sk

r=100
g=50
b=100
rgb=[]
new_data=[]

for pixel in data:

    new_r = riba(r + pixel[0])
    new_g = riba(g + pixel[1])
    new_b = riba(b + pixel[2])

    new_pixel = (new_r, new_g, new_b)
    new_data.append(new_pixel)
im.putdata(new_data)

im.show()

