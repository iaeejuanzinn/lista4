def calcular_area_quadrado(lado):
    area= lado ** 2
    area= calcular_area_quadrado(lado)
    return area
area= float(input('dgite a area do quadrado: '))
dobro_area= area ** 2
print(f'aréa do quadrado é {area}.')
print(f'o dobro da area do quadrado é {dobro_area}')