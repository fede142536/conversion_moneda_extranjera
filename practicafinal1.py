#Inicio:

#    1: Definir el valor actual del euro y dolar respecto al peso mexicano
 
#    Definir tipo_cambio_eur_a_mex = 23.70
#    Definir tipo_cambio_usd_a_mex = 20.75
eur_mex = 23.70
usd_mex = 20.75
#    2. Solicitar al usuario el tipo de conversion (usd a mex o eur a mex)
#    Solicitar al usuario el tipo de conversion (EUR/USD)
#    Mostrar mensaje "Ingrese la moneda origen para la conversion"
tipo_de_conversion = input("Ingrese el tipo de moneda a convertir (EURO / USD): ")
#    3. Solicitar el monto a convertir
#    Mostrar mensaje "Ingrese el monto a convertir"
monto = float(input("ingrese el monto a convertir: $"))
#    4. Realizar la conversion
#    5. Mostrar resultado
if tipo_de_conversion == "EURO":
    conversion_euro = eur_mex * monto 
    print("El resultado de la conversion de EURO a MEX es: ", conversion_euro)
elif tipo_de_conversion == "USD":
    conversion_usd = usd_mex * monto
    print("El resultado de la conversion de USD a MEX es: ", conversion_usd)
else:
    print("No esta disponible este tipo de conversion actualmente")

#    Si tipo_conversion == "eur":
#        calcular_resultado = monto_a_convenir * tipo_cambio_eur_a_mex
#        Mostrar "El resultado de la conversion de EUR a MEX es: ", resultado
#    Sino si tipo_conversion == "usd":    
#        calcular_resultado = monto_a_convenir * tipo_cambio_usd_a_mex
#        Mostrar "El resultado de la conversion de USD a MEX es: ", resultado
#    Sino:
#        Mostrar: "No esta disponible este tipo de conversion actualmente"    