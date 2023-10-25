from PIL import Image

img = Image.open("purple.jpg") #replace purple.jpg with your file name (make sure both script and jpg are in the same file)

img.save("prpl.ppm")

img = Image.open("prpl.ppm")

print(img.format, img.size, img.mode)
img.show()
