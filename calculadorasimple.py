for i in range(100):
    numero1 = int(input("Di el primer numero: "))
    operacion = str(input("Como quieres operar: "))

    numero2 = int(input("Di el segundo numero: "))

    if operacion == "*":
        resultado = numero1 * numero2
        print(f"{numero1}*{numero2}= {resultado}")
    if operacion == "/":
        resultado = numero1 / numero2
        print(f"{numero1}/{numero2}= {resultado}")
        
    if operacion == "+":
        resultado = numero1 + numero2
        print(f"{numero1}+{numero2}= {resultado}")
        
    if operacion == "-":
        resultado = numero1 - numero2
        print(f"{numero1}-{numero2}= {resultado}")