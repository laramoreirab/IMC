entrada = input()
A = float(entrada.split()[0])
P = float(entrada.split()[1])
R = P/(A*A)
if (R < 16):
    print("Magreza grave")
elif (R == 16 or R < 17):
    print("Magreza moderada")
elif( R == 17 or R < 18.5):
    print("Magreza leve")
elif (R == 18.5 or R < 25):
    print("Saudavel")
elif ( R == 25 or R < 30):
    print("Sobrepeso")
elif (R == 30 or R < 35):
     print("Obesidade Grau I")
elif (R == 35 or R < 40):
    print("Obesidade Grau II (severa)")
else:
    print("Obesidade Grau III (morbida)")
