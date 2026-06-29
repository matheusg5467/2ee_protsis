import sys
import math, cmath
import numpy as np

# O pick-up de 50ABC deve ser MAIOR do que a maior corrente de curto REMOTO
icc_max_BT = 1434.6 # Curto Trifásico na Barra Remota (BT)
icc_max_AT = 803.9

if icc_max_BT > icc_max_AT:
    print(f'Função 50ABC inútil neste cenário, corrente mínima de curto-circuito '
          f'na Barra REMOTA maior do que as correntes de curto da barra de AT\n')
else:
    print(f'OK! Definir corrente de pick-up baseando-se nos curtos em AT\n')
