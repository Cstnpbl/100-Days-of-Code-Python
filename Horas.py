hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

print(str((round((hour+(dura/60))))%24) + ":" + str((mins+dura)%60))

# Toma la hora y minutos de inicio y con la duracion estima la hora de finalizacion