# vamos a hacer un proytecto con todo lo visto de pooo 
# vamos a usar polimorfism0 , erencia, saber instanciar una clase , sobreeescritura , 
#dependensia 


# hacer un proyecto donde una  persona , dueno de un restaurante que quuiere hacer una lista para su restaurante , pueda agreagar difernetes cosas 
import os 
class CartaRestaurante:
    def __init__(self, nombre, precio  ):
        self.nombre = nombre
        self.precio  = precio 
        

    
        
    def _hacerPostre(self, ingredientes): 
        return 'nombre del postre : {}, Precio {}, ingredientes: {} Euros'.format(self.nombre, self.precio ,ingredientes)
    def _platoFuerte(self, ingredientes):
        return 'Nombre del plato : {}, Precio: {}, Ingredientes: {} Euros'.format(self.nombre, self.precio, ingredientes)
    def _hacerbebida(self):
        return 'Nombre de la bebida : {} , precio :{} Euros'.format(self.nombre, self.precio)

   
        
        




def hacer_platos():
    print('Bienvenido preparado para hacer tu carta de restaurante ....')
    while True:
        print(''' 
        Por donde quieres iniciar :
        1) hacer los platos fuertes 
        2) hacer los postres 
        3) bebidas que vas a vender''')
        try:
            
            respuesta = int(input('ingresa una opcion :'))
            if respuesta ==1 :
                nombrecarta1 = 'platosfuertes/'
                crear_directorio(nombrecarta1)
                print('''
                Vamos a crear los platos furtes de tu tienda : ''')
                nombre_plato = input( 'Dime el nombre quieres ponerle a el plato fuerte  ')
                precio_plato = int(input (  'Dime el precio del plato  '))
                ingredientes_plato = input('dim2e los ingredientes del plato ')
                platofuerte1 =  CartaRestaurante(nombre_plato, precio_plato)
                platonombre = platofuerte1._platoFuerte(ingredientes_plato)
                with open (nombrecarta1 +  nombre_plato + '.txt', 'a') as plato2:
                    plato2.write(platonombre)
                print('Tu plato fuerte ha sido agregado correctamente')

                
            elif respuesta ==2:
                nombrecarta= 'Postres/'
                crear_directorio(nombrecarta)
                print('''
                Vamos A Crear os postres de tu tienda : ''')
                nombre_postres = input('Dime el nombre del postre: ')
                precio_postre= int(input ( 'Dime el precio del postre : '))
                ingredientes_postre= input('dime los ingredientes que contiene el postre ')
                
                postre = CartaRestaurante(nombre_postres,precio_postre)
                postreventa = postre._hacerPostre(ingredientes_postre)
                with open( nombrecarta + nombre_postres + '.txt', 'a' ) as carta : 
                    carta.write(postreventa)
                print('Tu postre ha sido agregada correctamente ')

                
            elif respuesta == 3: 
                nombrecarta= 'bebida/'
                crear_directorio(nombrecarta)
                print('''
                Vamos A Agregar las bebidas de tu tienda : ''')
                nombre_bebida = input('Dime el nombre de la bebida:  ')
                precio_bebida= int(input ( 'Dime el precio de la bebida  :  '))
                
                
                postre = CartaRestaurante(nombre_bebida,precio_bebida)
                bebidaventa = postre._hacerbebida()
                with open( nombrecarta + nombre_bebida + '.txt', 'a' ) as carta : 
                    carta.write(bebidaventa)
                print('Tu bebida ha sido agregada correctamente')
        except: 
            print('Ocurrio un error , Porfavor asegurate de ingresar solo valores numericos ')








def crear_directorio(CARPETA):
    if not os.path.exists(CARPETA):  
        os.makedirs(CARPETA) 
    else:
        print(f'\r\n la carpeta: {CARPETA} fue creada anteriormente  \r\n')



hacer_platos()
        
        