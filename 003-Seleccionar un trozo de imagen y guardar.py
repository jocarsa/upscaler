from PIL import Image

imagen = Image.open("persona.jpg")
pixeles = imagen.load()

print(pixeles[0,0])
coordenadas = (0,0,64,64)
trozo = imagen.crop(coordenadas)
trozo.save("trozo.jpg")
