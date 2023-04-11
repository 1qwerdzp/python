from PIL import Image
from PIL import ImageDraw


csi=(200, 200)
rarea=[(0,0), (100,100)]
linec=[(0,200), (200,0)]
carea=[(100,100), (200,200)]

newi=Image.new("RGB", csi, "orange")
dri=ImageDraw.Draw(newi)
dri.rectangle(rarea, fill="red", outline="yellow")
dri.line(linec, fill="blue", width=4)
dri.ellipse(carea, fill="green", outline="red")

newi.show()
newi.save("imag.jpg")