#El programa se va a encargar de hacer un control financiero sobre la situación económica del usuario
#Pedimos al usuario los ingresos mensuales
ingresos_mensuales = float(input("Introduce tus ingresos mensuales: "))
#Pedimos al usuario cuanto dinero desea ahorrar
ahorro = float(input("Introduce la cantidad de dinero que desea ahorrar: "))
#Si se desea ahorrar mas de lo que se genera se imprime el sigueinte mensaje.
if ahorro > ingresos_mensuales:
    print("No dispones de tanto dinero para ahorrar.")
