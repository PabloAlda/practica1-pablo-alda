#El programa se va a encargar de hacer un control financiero sobre la situación económica del usuario
#Pedimos al usuario los ingresos mensuales
ingresos_mensuales = float(input("Introduce tus ingresos mensuales: "))
#Preguntamos al usuario si tiene que pagar alguna hipoteca o prestamo
hipoteca = input("¿Dispone de alguna hipoteca o prestamo que abonar?(Introduzca si o no): ")
#Si es así, le preguntamos cuanto es, si la respuesta es no, la hipoteca vale 0.
if hipoteca == 'si':
   hipoteca_pago = float(input("Introduzca el dinero a pagar mensualmente: "))
else:
   hipoteca_pago = 0
#Pedimos al usuario cuanto dinero desea ahorrar
ahorro = float(input("Introduce la cantidad de dinero que desea ahorrar: "))
#Si se desea ahorrar mas de lo que se genera se imprime el sigueinte mensaje.
if ahorro > ingresos_mensuales + hipoteca_pago:
    print("No dispones de tanto dinero para ahorrar.")
#Una vez calculado todo le decimos el dinero que dispone para gastar este mes
#Primero calculamos cuanto es con una función.
def dinero_disponible (ingresos_mensuales,hipoteca_pago,ahorro):
    dinero = ingresos_mensuales-hipoteca_pago-ahorro
    return dinero
#Guardo el valor del dinero
dinero_calculado = dinero_disponible(ingresos_mensuales,hipoteca_pago,ahorro)
#Muestro por pantalla el dinero restante.
print(f"Dispone de {dinero_calculado}€ para gastar este mes.")
#Ahora le preguntamos del dinero restante, cuanto quiere dedicar a cada cosa.
ocio_porcentaje = float(input("¿Qué porcentaje del dinero desea gastar en ocio?(Intoriducir solo el numero sin el %):"))
comida_porcentaje = float(input("¿Qué porcentaje del dinero desea gastar en comida?(Intoriducir solo el numero sin el %):"))
gasolina_porcentaje = float(input("¿Qué porcentaje del dinero desea gastar en gasolina?(Intoriducir solo el numero sin el %):"))
luz_porcentaje = float(input("¿Qué porcentaje del dinero desea gastar en luz?(Intoriducir solo el numero sin el %):"))
#Ahora calculamos cada valor que corresponde a esos porcentajes.
#Empezamos por el ocio
def ocio (ocio_porcentaje,dinero_calculado):
    dinero_ocio = ocio_porcentaje*dinero_calculado/100
    return dinero_ocio
#Guardamos el valor
ocio_calculado = ocio(ocio_porcentaje,dinero_calculado)
#Mostramos por pantalla el dinero.
print(f"Dispone de {ocio_calculado}€ para gastar este mes en ocio.")

#Ahora con la camida
def comida (comida_porcentaje_porcentaje,dinero_calculado):
    dinero_comida = comida_porcentaje*dinero_calculado/100
    return dinero_comida
#Guardamos el valor
comida_calculado = comida(comida_porcentaje,dinero_calculado)
#Mostramos por pantalla el dinero.
print(f"Dispone de {comida_calculado}€ para gastar este mes en comida.")

#Ahora con la gasolina
def gasolina (gasolina_porcentaje,dinero_calculado):
    dinero_gasolina = gasolina_porcentaje*dinero_calculado/100
    return dinero_gasolina
#Guardamos el valor
gasolina_calculado = gasolina(gasolina_porcentaje,dinero_calculado)
#Mostramos por pantalla el dinero.
print(f"Dispone de {gasolina_calculado}€ para gastar este mes en gasolina.")

#Ahora con la luz
def luz (luz_porcentaje,dinero_calculado):
    dinero_luz = luz_porcentaje*dinero_calculado/100
    return dinero_luz
#Guardamos el valor
luz_calculado = luz(luz_porcentaje,dinero_calculado)
#Mostramos por pantalla el dinero.
print(f"Dispone de {luz_calculado}€ para gastar este mes en luz.")
