def quick_sort(lista,clave):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    mayores = [x for x in lista[1:] if x[1][clave] > pivote[1][clave]]
    menores = [x for x in lista[1:] if x[1][clave] < pivote[1][clave]]

    return quick_sort(menores,clave)+[pivote]+quick_sort(mayores,clave)



carrera = {}
opcion = 0
while opcion !=4:
    print("--- MENÚ DE OPCIONES ---")
    print("1. Agregar participante")
    print("2. Mostrar participantes ordenados por nombre")
    print("3. Mostrar participantes ordenados por edad")
    print("4. Salir")
    opcion = int(input("Seleccione una opcion: "))

    match opcion:
        case 1:
            print("=== Registrar participante ===")
            try:
                cantidad = int(input("Cantidad de participantes que desea registrar: "))
            except ValueError:
                print("Error: no ha ingresado un numero")
                continue

            for j in range(cantidad):
                print(f"Participante {j+1}")
                dorsal = int(input("Numero de Dorsal: "))
                nombre = input("Nombre del participante: ")
                edad = int(input("Edad: "))
                categoria = input("Categoria(Juvenil,adulto,master): ")
                carrera[dorsal]={
                    "nombre": nombre,
                    "edad": edad,
                    "categoria": categoria
                }

        case 2:
            corredores= list(carrera.items())
            print("=== Mostrar participante ordenado por nombre ===")
            resultado = quick_sort(corredores,"nombre")
            for dorsales,datos in resultado:
                print(f" {datos['nombre']} (Dorsal {dorsales}, Edad: {datos['edad']}, Categoria: {datos['categoria']})")


