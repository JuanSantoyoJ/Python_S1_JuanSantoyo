import json

def abrirJSON():
    coco={}
    with open('./coco.json','r') as openFile:
        coco=json.load(openFile)
    return coco

def guardarJSON(coco):
    with open('.\coco.json','w') as outFile:
        json.dump(coco,outFile)
inicio=True
while inicio == True:
    print("\nBienvenido a Electrodomesticos Alkosto")
    print("1. Si quiere ver nuestros productos")
    print("5. Si desea salir")
    opc=int(input("Ingresa: "))
    if opc == 1:
        print("\n")
        Electrodomesticos={}
        Electrodomesticos=abrirJSON()
        for i in range(len(Electrodomesticos["productos"])):
            print("\nProducto", i+1)
            print("Nombre:",Electrodomesticos["productos"][i]["nombre"])
            print("Categoria:",Electrodomesticos["productos"][i]["categoria"])
            print("Precio:",Electrodomesticos["productos"][i]["precio"])
            print("Cantidad disponible:",Electrodomesticos["productos"][i]["cantidad disponible"])
            print("Marca:",Electrodomesticos["productos"][i]["Marca"])
            print("Descuento:",Electrodomesticos["productos"][i]["descuento"])
            print("Caracteristicas:",Electrodomesticos["productos"][i]["nombre"]["caracteristicas"])

            
    if opc==5:
        print("Gracias por su compra")
        inicio=False
    