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

# Curto trifásico na barra de 69kV nos fornece a corrente máxima em 69kV
icc_max_69kV = 4781.9

i_sobrecarga = 1.4 * i_nominal_69kV
print(f"Sobrecarga = {i_sobrecarga}")

icc_min_69kV = 239.2 # Curto Bifásico na barra de 230kV
i_pickup = 220 # Pois deve ser sensível ao menor curto (239.2 A)!
print(f"Pickup = {i_pickup}\n")

if i_pickup < i_sobrecarga: 
    print(f"PRECISAREMOS DE 51 V EM SÉRIE, POIS A CORRENTE DO MENOR CURTO OBSERVADO ({icc_min_69kV} A) "
          f"FAZ COM QUE SEJA NECESSÁRIO A DEFINIÇÃO DE UMA CORRENTE DE PICK-UP ({i_pickup} A) "
          f"MENOR DO QUE A CORRENTE OBSERVADA SOBRE SOBRECARGA ({i_sobrecarga} A)\n")

multiplo_sensi =  icc_max_69kV / i_pickup
if multiplo_sensi < 2: 
    sys.exit("Erro, múltiplo de sensibilidade está abaixo do esperado!")
t_51_fase_69kV = t_instant + cti

tms_51_fase_69kV = t_51_fase_69kV * (multiplo_sensi**alfa - 1) / beta
print(f"Encontramos um múltiplo de sensibilidade igual a: {multiplo_sensi}")
print(f"Usando pickup PRIMÁRIO para a função 51 de fase do relé de 230kV igual à: {round(i_pickup, 3)} A")
print(f"TMS para a função 51 fase de kV: {round(tms_51_fase_69kV, 3)}\n")
