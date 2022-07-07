
idades = [39, 30, 27, 18]

print(idades)

idades.append(74)

print(idades)

idades.extend([23,54,87])

print(idades)

# for elemento in idades:
#     print('Recebi: ',elemento)

idades_no_ano_que_vem = [idade + 1 for idade in idades]

print(idades_no_ano_que_vem)
