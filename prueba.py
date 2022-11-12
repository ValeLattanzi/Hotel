archivo = open("TipoDocumento.txt", "r")

lineas = archivo.readlines()
lista = []
for i in range(len(lineas)):
    pension = lineas[i][:-1]
    lista.append(pension)

print(tuple(lista))

# Ingresar DNI
# Cargar los datos del cliente segun el DNI
# Se cargan los datos del cobro
# Se cambia el estado de la estadia
# Se registra