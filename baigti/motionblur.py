from PIL import Image

def test(oldimage):
    pix1 = oldimage.load()
    newimage = Image.open('test.png')#should be camera input
    pix2 = newimage.load()
    output = Image.new("RGB",(newimage.size[0],newimage.size[1]),(0,0,0))
    pix3 = output.load()
    for x in range(newimage.size[0]):
        for y in range(newimage.size[1]):
            if(pix1 != pix2):
                pix3[x,y] = (0,0,0)
    save(output)
    test(newimage)
def save(output):
    output.save('test.png')
test(Image.new("RGB",(200,200),(0,0,0)))
