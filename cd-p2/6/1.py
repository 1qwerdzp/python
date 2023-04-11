from PIL import Image

ar=(230, 155, 1110, 770)
si=(640, 200)

lioni=Image.open("Li.jpg")
fruiti=Image.open("fru.jpg")

print(lioni.size, lioni.format, lioni.mode)
print(fruiti.size, fruiti.format, fruiti.mode)

fruitr=fruiti.resize(si)
lionc=lioni.crop(ar)
lioni.show()

lionc.save("lion_cropped.jpg")
fruitr.save("fru_cropped.jpg")