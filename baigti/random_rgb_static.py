from PIL import Image
import random

im = Image.open('test.png')
pix = im.load()
print(im.size)
def test():
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            pix[x,y] = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    print("generated")
    save()
    test()
def save():
    im.save('test.png')
test()
