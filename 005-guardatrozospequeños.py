from PIL import Image

imagen = Image.open("persona.jpg")
pixeles = imagen.load()

paso = 64

for x in range(0,1024,64):
    for y in range(0,1024,64):
        coordenadas = (x,y,x+64,y+64)
        trozo = imagen.crop(coordenadas)
        trozo.save("trozos/grandes/"+str(x)+"-"+str(y)+".jpg")
        tamanopequeno = (16,16)
        pequeno = trozo.resize(tamanopequeno)
        pequeno.save("trozos/pequenos/"+str(x)+"-"+str(y)+".jpg")
