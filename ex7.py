dia = int(input("digite o dia: "))
hora = int(input("digite a hora: "))
minuto = int(input("digite o minuto: "))
segundo = int(input("digite o segundo: "))

dia = dia *24 * 60 * 60
hora = hora * 60 * 60
minuto = minuto *  60
total_segundos = dia + hora + minuto + segundo
print(f"o total de segundos é {total_segundos}")