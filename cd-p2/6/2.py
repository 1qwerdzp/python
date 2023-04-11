from PIL import Image

si=(128, 128)

lioni=Image.open("Li.jpg")
lionr=lioni.rotate(90)
lionc=lioni.convert('L')
liont=lioni.transpose(Image.FLIP_LEFT_RIGHT)
lioni.thumbnail(si)

print("lion_converted.mode =", lionc.mode)
print("lion_img.size=", lioni.size)

lionc.show()
liont.show()
lionr.show("lion_rotated.jpg")
lioni.save("lion_thumb.jpg")