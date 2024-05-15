import math

def caucular_area_circulo(raio):
    area= math.pi * raio ** 2 
    return area 
raio= float(input('digite o raio do circulo: '))
area= caucular_area_circulo(raio)
print(f'a area do circulo com raio {raio} é {area:.2f}.')