from PIL import Image

imagen = Image.open("persona.jpg")
pixeles = imagen.load()

paso = 64
incremento = 16
pasopequeno = int(paso/4)

for x in range(0,1024,incremento):
    for y in range(0,1024,incremento):
        coordenadas = (x,y,x+paso,y+paso)
        trozo = imagen.crop(coordenadas)
        trozo.save("trozos/grandes/"+str(x)+"-"+str(y)+".jpg")
        tamanopequeno = (pasopequeno,pasopequeno)
        pequeno = trozo.resize(tamanopequeno)
        pequeno.save("trozos/pequenos/"+str(x)+"-"+str(y)+".jpg")
