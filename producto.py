
class producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = str(codigo)
        self.nombre = nombre
        self.precio = precio
        self.iva = str(0.19)
        self.stock = str(0)
        
    def __str__(self):
        datos = ("codigo: "+self.codigo+"/n"
                +"nombre: "+self.nombre+"/n"
                +"precio: "+str(self.precio)+"/n"
                +"iva: "+str(self.iva)+"/n"
                +"inventario: "+str(self.stock)
                )
        return datos
