class Cuenta:
  #Constructor
  def __init__ (self, titular, cantidad = 0.0):
    #Atributos
    self.titular = titular
    self.__cantidad = cantidad
 #Proteccion de catidad  
  @property
  def cantidad(self):
    return self.__cantidad
  #Metodo mostrar
  def mostrar(self):
    return (f'Titular: ' + self.titular + ' Cantidad: ' + str(self.cantidad))
  #Metodo ingresar
  def ingresar(self,cantidad):
    if cantidad > 0:
      self.__cantidad += cantidad 
    else:
      print('Ingrese una cantidad positiva')  
  #Metodo retirar
  def retirar(self, cantidad):
    if cantidad > 0:
      self.__cantidad -= cantidad
    elif cantidad <0:
      print('Ingrese un monto positivo')
#OPERACIONES   
mi_cuenta = Cuenta('Augusto')
mi_cuenta.ingresar(1000) # Ingreso de dinero
mi_cuenta.ingresar(500)# Ingreso de dinero
mi_cuenta.retirar(5000)# Retiro de dinero de dinero

print('---BANCO PYTHON---')
print(f'''
Hola {mi_cuenta.titular} bienvenido a nuetro banco,
el monto total de dinero en su cuenta es: {mi_cuenta.cantidad}
''')