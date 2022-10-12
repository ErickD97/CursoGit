from math import sqrt, sin, cos, tan, atan, pi


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self,xm,ym):
        xr = self.x + xm
        yr = self.y + ym
        return [xr, yr]

    def distance(self, xd, yd):
        d = sqrt((self.x - xd)*(self.x - xd) + (self.y - yd)*(self.y - yd))
        return d

    def angle(self):
        d = sqrt(self.x * self.x + self.y * self.y)
        angulo_eje_x = (atan(self.y/self.x))*360/(2*pi)
        angulo_eje_y = (atan(self.x/self.y))*360/(2*pi)
        values = [d, angulo_eje_x, angulo_eje_y]
        return values

try:
    x = int(input('Valor de coordenada x: '))
    y = int(input('Valor de coordenada y: '))
except ValueError:
    x = int(input('Valor de coordenada x: '))
    y = int(input('Valor de coordenada y: '))
point1 = Point(x,y)
print(f'''Tiene las siguientes opciones:
a) Mover el punto
b) Hallar la distancia entre el mismo y otro punto que usted proporcione
c) Hallar el ángulo entre la recta que una este punto con el origen y los ejes coordenados, ademas de la longitud de 
dicha recta
''')
command = input('Que desea hacer? ')
if command.upper() == 'A':
    xa = int(input('Introduzca el desplazamiento en x: '))
    ya = int(input('Introduzca el desplazamiento en y: '))
    print(f'El desplazamiento resultaría en la posición: {point1.move(xa,ya)}')
elif command.upper() == 'B':
    xd = int(input('Introduzca el valor de coordenada x: '))
    yd = int(input('Introduzca el valor de coordenada y: '))
    print(f'La distancia es: {point1.distance(xd,yd)}')
elif command.upper() == 'C':
    [distancia, angulox, anguloy] = point1.angle()
    print(f'El punto esta a {distancia} unidades, tiene un ángulo con el eje X de {angulox} grados y con el eje Y de {anguloy} grados')
else:
    print('No ha ingresado una opción válida')

