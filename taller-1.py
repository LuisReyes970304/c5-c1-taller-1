saldo = 1000
pregunta_operacion = int(input("Cuantas Operaciones deseas realizar?: "))

for i in range(pregunta_operacion):
    print("Que operacion deseas realizar: \n1 → Consultar saldo \n2 → Retirar dinero \n3 → Depositar dinero")
    pregunta_operacion_2 = input("Selecciona una operacion: ")

    if pregunta_operacion_2 == "1":
        print("Tu saldo es de: ", saldo)

    if pregunta_operacion_2 == "2":
        retirar_dinero = int(input("Cuanto dinero deseas retirar?: "))

        while retirar_dinero < 0:
            print("No puedes retirar una cantidad negativa, por favor ingresa una cantidad valida")
            retirar_dinero = int(input("Cuanto dinero deseas retirar?: "))

        if retirar_dinero > saldo:
            print("No tienes suficiente saldo para realizar esta operacion")

        else:
            saldo -= retirar_dinero
            print(f"Operacion realizada con exito, tu nuevo saldo es de: {saldo}")

    if pregunta_operacion_2 == "3":
        depositar_dinero = int(input("Cuanto dinero deseas depositar?: "))

        while depositar_dinero < 0:
            print("No puedes depositar una cantidad negativa, por favor ingresa una cantidad valida")
            depositar_dinero = int(input("Cuanto dinero deseas depositar?: "))

        if depositar_dinero > 0:
            saldo += depositar_dinero
            print(f"Operacion realizada con exito, tu nuevo saldo es de: {saldo}")
            
    if pregunta_operacion_2 not in ["1", "2", "3"]:
        print("Operacion no valida")

print("Gracias por usar nuestro servicio, hasta luego!")        