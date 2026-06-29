####################ALTA TENSÃO##############################
print(f'-----CÁLCULOS PARA 230kV:-----')
print(f'CÁLCULO DE 50ABC de 230kV:')
import relay_50ABC_AT
print('\n')

print(f'CÁLCULO DE 51ABC DE 230kV:')
import relay_51ABC_AT
print('\n\n')


####################BAIXA TENSÃO##############################
print(f'-----CÁLCULOS PARA 69kV:-----')
print(f'CÁLCULO DE 50ABC de 69kV:')
import relay_50ABC_BT
print('\n')

print(f'CÁLCULO DE 51ABC DE 69kV:')
import relay_51ABC_BT
print('\n\n')

