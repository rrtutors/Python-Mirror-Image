from PIL import Image
upright_image = Image.open("C:/Users/Kevoh/Pictures/ilovepython.png")
mirrored_img = upright_image.transpose(method=Image.FLIP_TOP_BOTTOM)
mirrored_img.save("python.png")
upright_image.close()
mirrored_img.close()
