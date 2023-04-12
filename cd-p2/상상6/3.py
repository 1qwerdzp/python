from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

f=open("ml.txt","w")
f.write(input("설명:"))
f.close()
fri=Image.open("fr.jpg")
lii=Image.open("Li.jpg")
c3i=Image.open("c3.jpg")
dr=ImageDraw.Draw(fri)
f=open("ml.txt","r")
r=f.read()
fri.paste(lii,(15,15,235,185))
fri.paste(c3i,(105,187,146,197))
dr.text((150,30),r,'#000000',align="Left")

fri.show()