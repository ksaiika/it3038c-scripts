from PIL import Image

img = Image.open("purple.jpg")

segments = 20

kds = Image.new("RGB", img.size)

angle = 420 / segments

for i in range(segments):
	rotate = img.rotate(i * angle)

kds.paste(rotate, (0,0))

kds.save("kldscp.ppm")

kds.show()
