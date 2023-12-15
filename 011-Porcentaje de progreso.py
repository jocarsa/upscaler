from PIL import Image
import os

def mapear(valor, min1, max1, min2, max2):
    mapeado = (valor - min1) / (max1 - min1) * (max2 - min2) + min2
    return mapeado

carpeta = 'entrenamiento'

archivos = os.listdir(carpeta)

paso = 64
incremento = 4
pasopequeno = int(paso/8)

contador = 0
total = (1024/incremento)*(1024/incremento)*len(archivos)

for archivo in archivos:
    imagen = Image.open(carpeta+"/"+archivo)
    pixeles = imagen.load()

    

    for x in range(0,1024,incremento):
        for y in range(0,1024,incremento): 
            if (contador/total)*100 % 10 == 0:
                print(str((contador/total)*100)+"%")
            contador += 1
            coordenadas = (x,y,x+paso,y+paso)
            trozo = imagen.crop(coordenadas)
            
            tamanopequeno = (pasopequeno,pasopequeno)
            pequeno = trozo.resize(tamanopequeno)  
            cadena = ""
            for x2 in range(0,pasopequeno):
                for y2 in range(0,pasopequeno):
                    cadena += str(int(mapear(pequeno.load()[x2,y2][0], 0, 255, 0, 9)))
            try:
                trozo.save("trozos/grandes/"+cadena+".jpg")
            except:
                print("da error pero continuo")
