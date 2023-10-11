# practica1-pablo-alda

# Control Financiero

Este programa en Python te ayudará a llevar un control financiero personalizado, permitiéndote gestionar tus ingresos, gastos y ahorros de manera eficiente. A continuación, se detallan las instrucciones para utilizar el programa correctamente.


## Program Features
*Ingresos Mensuales:
Ingresa tus ingresos mensuales cuando se te solicite. Esto incluye cualquier fuente de ingresos regular que recibas cada mes.

*Hipoteca o Préstamo (opcional):
Indica si tienes que pagar una hipoteca o préstamo mensualmente.
Si respondes "sí", ingresa el monto que pagas mensualmente. Si respondes "no", el programa asumirá que no tienes gastos relacionados con una hipoteca o préstamo.

*Ahorros:
Ingresa la cantidad de dinero que deseas ahorrar este mes.

*Asignar Porcentajes para Gastos:
Ingresa el porcentaje del dinero que deseas gastar en diferentes categorías: ocio, comida, gasolina, luz, etc. Ingresa solo el número sin el símbolo "%".

*Resultados:
El programa calculará cuánto dinero puedes gastar en cada categoría después de tener en cuenta tus ingresos, pagos de hipoteca, ahorros y porcentajes asignados para gastos.
Te mostrará cuánto dinero tienes disponible para gastar este mes en cada categoría.
## Usage/Examples

ingresos_mensuales = float(input("Introduce tus ingresos mensuales: "))
hipoteca = input("¿Tienes que pagar alguna hipoteca o préstamo? (si/no): ")

if hipoteca.lower() == 'si':
   hipoteca_pago = float(input("Introduce el dinero a pagar mensualmente: "))
else:
   hipoteca_pago = 0

ahorro = float(input("Introduce la cantidad de dinero que deseas ahorrar: "))

Ingresar porcentajes para gastos
ocio_porcentaje = float(input("Porcentaje de dinero para ocio (sin el %): "))
comida_porcentaje = float(input("Porcentaje de dinero para comida (sin el %): "))
gasolina_porcentaje = float(input("Porcentaje de dinero para gasolina (sin el %): "))
luz_porcentaje = float(input("Porcentaje de dinero para luz (sin el %): "))
Resultados
(Aquí se mostrarán los resultados obtenidos después de calcular los gastos disponibles en cada categoría)




## Notes
Este programa es una herramienta básica y puede no cubrir todas las complejidades de tu situación financiera.
Asegúrate de ajustar los porcentajes y los gastos según tus necesidades y preferencias personales.
Se recomienda utilizar valores numéricos válidos para obtener resultados precisos.
¡Buena gestión financiera y disfruta usando el programa!
## Authors

- Pablo Alda


