from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

loni=Image.open("L.jpg")
lioni=Image.open("Li.jpg")
dr=ImageDraw.Draw(loni)

loni.paste(lioni,(10,10,605,605))

loni.show()
loni.save("lion_thumb.jpg")