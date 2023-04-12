from PIL import Image
from PIL import ImageDraw

fri=Image.open("fr.jpg")
lii=Image.open("Li.jpg")
dr=ImageDraw.Draw(fri)

fri.paste(lii,(15,15,235,185))

fri.show()