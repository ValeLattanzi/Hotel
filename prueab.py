def buscarElementoPorDNI(dni: str, indice: int,  i : int = 0, lineas = open("RegistroEstadia.txt", "r", encoding = "utf-8").readlines()):
    if i >= len(lineas):
        return None
    elif lineas[i].split(",")[6] == dni and lineas[i].split(",")[9] == "PendienteCobro":
        xd = (lineas[i].split(",")[indice])
        return xd
    else:
        i += 1
        buscarElementoPorDNI(dni, indice, i)
print(buscarElementoPorDNI("44899289", 9))