import sys
import math, cmath
import numpy as np


i_nominal_69kV = 100*(10**6) / (math.sqrt(3) * 69000)
i_nominal_230kV = 100*(10**6) / (math.sqrt(3) * 230000)

print("Usaremos a curva NORMAL INVERSA (N. I.) onde α = 0.02 e β = 0.14")
alfa = 0.02
beta = 0.14

# Tempo de atuação para proteção instantânea igual à 0.5 segundos
t_instant = 0.5

# Intervalo de tempo para coordenação definido como 0.4 segundos
cti = 0.4

fator_sobrecarga = 1.4

# Curto trifásico na barra de 69kV nos fornece a corrente máxima em 230kV
icc_max_230kV = 1434.6

i_pickup = 1.4 * i_nominal_230kV

multiplo_sensi =  icc_max_230kV / i_pickup
if multiplo_sensi < 2: 
    sys.exit("Erro, múltiplo de sensibilidade está abaixo do esperado!")
t_51_fase_230kV = t_instant + cti

tms_51_fase_230kV = t_51_fase_230kV * (multiplo_sensi**alfa - 1) / beta
print(f"Usando pickup PRIMÁRIO para a função 51 fase de 230kV igual à {round(i_pickup, 3)} A")
print(f"tms para a função 51 fase de 230 kV: {round(tms_51_fase_230kV, 3)}")
