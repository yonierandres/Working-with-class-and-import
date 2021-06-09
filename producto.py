
class producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.iva = 0.19
        self.stock = 0
        
    def __str__(self):
        datos = ("codigo: "+ self.codigo +"/n"
                +"nombre: "+ self.nombre +"/n"
                +"precio: "+ self.precio +"/n"
                +"iva: "+ self.iva +"/n"
                +"inventario: "+self.stock
                )
        return datos
