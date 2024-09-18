print("progranacion Poo")
#definicion de clase
class perro:
    #funciones dentro de la clase
    def morder(self):
        print("El Perro me mordio")
    def Datos_Perro(self,nombre,edad):
        print(f"nombre: {nombre}, edad:{edad}")

#zona de creacion de objetos
pitbull=perro()

#zona de uso de objetos

pitbull.Datos_Perro("Bobby", 4)
pitbull.morder()