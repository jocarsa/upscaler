from PIL import Image

imagen = Image.open("persona.jpg")
pixeles = imagen.load()

paso = 64
incremento = 16
pasopequeno = int(paso/8)

for x in range(0,1024,incremento):
    for y in range(0,1024,incremento):
        coordenadas = (x,y,x+paso,y+paso)
        trozo = imagen.crop(coordenadas)
        
        tamanopequeno = (pasopequeno,pasopequeno)
        pequeno = trozo.resize(tamanopequeno)  
        cadena = ""
        for x2 in range(0,pasopequeno):
            for y2 in range(0,pasopequeno):
                if pequeno.load()[x2,y2][0] < 127:
                    cadena += "0"
                else:
                    cadena += "1"
        try:
            trozo.save("trozos/grandes/"+cadena+".jpg")
            pequeno.save("trozos/pequenos/"+cadena+".jpg")
            pequeno.close()
        except:
            print("da error pero continuo")
