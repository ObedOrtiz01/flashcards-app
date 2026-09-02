# main.py - FlashCards App (Primer Avance Funcional)

def mostrar_menu():
    print("\n--- FLASHCARDS APP ---")
    print("1. Crear tarjeta")
    print("2. Ver todas las tarjetas")
    print("3. Eliminar tarjeta")
    print("4. Salir")

def main():
    tarjetas = []
    
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ")
        
        if opcion == "1":
            pregunta = input("Ingresa la pregunta: ")
            respuesta = input("Ingresa la respuesta: ")
            tarjetas.append({"pregunta": pregunta, "respuesta": respuesta})
            print("¡Tarjeta creada exitosamente!")
            
        elif opcion == "2":
            if not tarjetas:
                print("No hay tarjetas registradas.")
            else:
                for idx, t in enumerate(tarjetas, 1):
                    print(f"{idx}. P: {t['pregunta']} | R: {t['respuesta']}")
                    
        elif opcion == "3":
            if not tarjetas:
                print("No hay tarjetas para eliminar.")
            else:
                for idx, t in enumerate(tarjetas, 1):
                    print(f"{idx}. P: {t['pregunta']}")
                try:
                    num = int(input("Número de tarjeta a eliminar: ")) - 1
                    if 0 <= num < len(tarjetas):
                        tarjetas.pop(num)
                        print("Tarjeta eliminada.")
                    else:
                        print("Número de tarjeta inválido.")
                except ValueError:
                    print("Por favor, ingresa un número válido.")
                    
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
