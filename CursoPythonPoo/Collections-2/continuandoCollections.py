
usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

# assistiram = []

# assistiram.extend(usuarios_data_science)

assistiram = usuarios_data_science.copy()

assistiram.extend(usuarios_machine_learning)

print(assistiram)

print(len(assistiram))


print(set(usuarios_data_science) - set(usuarios_machine_learning)) # Está em X mas não em Y

print(set(usuarios_data_science) | set(usuarios_machine_learning)) # Está em X ou em Y

print(set(usuarios_data_science) ^ set(usuarios_machine_learning)) # Está em X e em Y, mas não em ambos

print(set(usuarios_data_science) & set(usuarios_machine_learning)) # Está em X e em Y


print(usuarios_machine_learning.__add__(usuarios_data_science))
