from PIL import Image

imagen = Image.open("persona.jpg")
pixeles = imagen.load()

print(pixeles[0,0])
