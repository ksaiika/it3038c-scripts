from PIL import Image

img1 = Image.open("purple.jpg")

img2 = Image.open("pink.jpg")

img2 = img2.resize(img1.size)

opacity = 115 #choose opacity of img2
img2.putalpha(opacity)

merge = Image.alpha_composite(img1.convert("RGBA"), img2.convert("RGBA"))

merge.save("merged.ppm")

merge.show()
