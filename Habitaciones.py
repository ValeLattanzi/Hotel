archivo = open("Habitaciones.txt","w")
for i in range(1,4):
    for j in range(1, 11):
        if j < 10:
            archivo.write(str(i) + "0" + str(j) + "\n")
        else:
            archivo.write(str(i) + str(j) + "\n")