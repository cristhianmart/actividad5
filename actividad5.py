
def ejercicio1():
    print("ejecucion del ejercicio 1: bienvenido al verificador de mayoria de edad versión Colombia")
    edad = int(input("Ingresa tu edad por favor "))
    if (edad >= 18 ):
        print("en efecto, eres mayor de edad en colombia. ¿Vamos por una polas?")
    
    elif (edad < 18):
        print("eres menor de edad, ¡hey, mira estan dando cuento de los hermanos grimm!")
    
    else:
        print("eso no es un numero pillín")
    
    
def ejercicio2():
    print("ejecucion del ejercicio 2")
    print("!oh no¡ acabas de activar el ciclo infinito, si no adivinas el numero correcto del 1 al 10, nunca podras salir de esta opción")
    adivinador = 0
    while adivinador != 7:
        adivinador = int(input("Comienza el juego, ingresa el numero que crees que detendra el bucle "))

def ejercicio3():
    print("ejecucion del ejercicio 3")
    print("así que quieres saber sí te tiraste el semestre, regalame tus 4 notas en el rango de 0 a 5: ")
    notas = []
    total = 0  
    
    for _ in range(4):  
        nota = float(input("Agrega tus notas de una en una: "))
        notas.append(nota)


    for i in notas:
        total += i
    promedio = total / len(notas) 
    print("Tu nota final es:", promedio)

def ejercicio4():
    print("ejecucion del ejercicio 4")
    print("Bienvenido a la calculadora y evaluadora de masa corporal, a continuación ingresa la siguiente información")
    kilos = float (input("Tu peso en kilogramos: "))
    estatura = float(input("Tu estatura en metro: "))
    indice = kilos / estatura ** 2
    print("tu indice de masa corporal es de: ", indice)
    rta = int(input("¿quieres que te interprete los resultado? 1 para SÍ, cualquier otra tecla para NO "))
    if (rta == 1):
        if (indice <= 18.5):
            print ("el era paco el flaco... estas considerado como de 'bajo peso', toca darte complejo B")
        elif (indice <= 24.9):
            print ("ni fu ni fa, buen trabajo eres considerado de 'peso normal'")
        elif (indice <= 29.9):
            print ("Estamos comiendonos toda la sopita ehhh, ojo que ya eres considerado con 'sobrepeso'")
        else:
            print("ajá compadre, bajale a la cuchara que la cosa ya es sería, ya eres considerado 'obeso'")
    else:
        print("hay cosas que es mejor no saber, gracias por utilizar nuestros servicios")
        
def ejercicio5():
    print("ejecucion del ejercicio 5")
    print("Hola, soy el detector de palabras palíndromas, si no sabes que es un palindromo ¡goglealo!")

    palabra = input("ingresa la palabra a adivinar: ")
    inverso = ""
    for letra in palabra:
        inverso = letra + inverso
    if (palabra == inverso):
        print("La palabra sí es un palíndromo")
    else:
        print("la palabra no es un palíndromo")
   
        

   



print("Menu de ejercicios")
print("Seleccione una opcion: (1-5)")
print("1. ejercicio 1")
print("2. ejercicio 2")
print("3. ejercicio 3")
print("4. ejercicio 4")
print("5. ejercicio 5")

opcion= int(input("Ingrese el numero deseado: "))

if opcion==1:
    ejercicio1()
elif opcion==2:
    ejercicio2()
elif opcion==3:
    ejercicio3()
elif opcion==4:
    ejercicio4()
elif opcion==5:
    ejercicio5()
