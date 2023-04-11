from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

lioni=Image.open("Li.jpg")
c3i=Image.open("c3.jpg")
c3i.thumbnail((120,120))
dr=ImageDraw.Draw(lioni)

stx, sty= (150, 285)
c3x, c3y=c3i.size
msg1="The              is"
msg2="the best"
#mf=ImageFont.truetype("FRADM.TTF", 40)
#m2f=ImageFont.truetype("BROADW.TTF", 52)
dr.text((70,280), msg1, (255,255,0), align="Left")
dr.text((70,330), msg2, (255,0,0), align="Left")
lioni.paste(c3i,(stx, sty,stx+c3x,sty+c3y))
lioni.show()
lioni.save("lion_thumb.jpg")