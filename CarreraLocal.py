def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    mayores = [x for x in lista[1:] if x[1] > pivote[1]]
    menores = [x for x in lista[1:] if x[1] < pivote[1]]

    return quick_sort(menores)+[pivote]+quick_sort(mayores)



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
