from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

lioni=Image.open("L.jpg")
liond=ImageDraw.Draw(lioni)
liond.ellipse([(0,0), (600,600)],width=10,outline="yellow")

lioni.show()
lioni.save("lion_thumb.jpg")