from PIL import Image
from PIL import ImageDraw

fri=Image.open("fr.jpg")
lii=Image.open("Li.jpg")
c3i=Image.open("c3.jpg")
dr=ImageDraw.Draw(fri)

fri.paste(lii,(15,15,235,185))
fri.paste(c3i,(105,187,146,197))

fri.show()