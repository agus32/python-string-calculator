def string_calculator(cadena):
    if cadena == "":
        return 0
    else:
        if cadena.startswith("//"):
            delimitador = cadena[2]
            cadena = cadena.split("\n")[1]
            cadena = cadena.replace(delimitador, ",")
        numeros = cadena.replace("\n", ",")
        
        numeros_enteros = list(map(int, numeros.split(",")))

        if any(num < 0 for num in numeros_enteros):
            raise ValueError(f"No se permiten negativos: {', '.join(str(num) for num in numeros_enteros if num < 0)}")

        return sum(numeros_enteros)
