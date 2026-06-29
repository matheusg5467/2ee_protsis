import sys
import math, cmath
import numpy as np

# O pick-up de 50ABC deve ser MAIOR do que a maior corrente de curto REMOTO
icc_max_AT = 701.2 # Curto Trifásico na Barra Remota (AT)
icc_max_BT = 4781.9 

if icc_max_AT > icc_max_BT:
    print(f'Função 50ABC inútil neste cenário, corrente mínima de curto-circuito '
          f'na Barra REMOTA maior do que as correntes de curto da barra de AT\n')
else:
    print(f'OK! Definir corrente de pick-up baseando-se nos curtos em BT\n')

i_nominal_69kV = 100*(10**6) / (math.sqrt(3) * 69000)
i_nominal_230kV = 100*(10**6) / (math.sqrt(3) * 230000)

print(f'Corrente Nominal de 69kV: {round(i_nominal_69kV, 3)} A\n')

i_pickup = 1700 # Mais de 2x a corrente nominal e a corrente de curto na barra remota

print(f'Corrente de pick-up PRIMÁRIA definida: {i_pickup} A')
