#Calculos Matematicos
#calculo del area y perimetro  de un circulo

def area_circulo(radio):
     area = 3.141516 * ( radio ** 2)
     return area
def  perimetro_circulo(radio):
      perimetro = 2 *  3.141516 * radio
      return perimetro
      #calculo del area y perimetro de un triangulo
def area_triangulo(base, altura):
    area = (base*altura)/2
    return area
def perimetro_triangulo(lado1, lado2, lado3):
    perimetro = lado1 + lado2 + lado3   
    return perimetro
#calculo del area y perimetro de un retangulo
def area_rectangulo(largo, ancho):
    area = largo * ancho
    return area
def perimetro_rectangulo(largo, ancho):
    perimetro = (2*largo) + (2*ancho)  
    return perimetro
  