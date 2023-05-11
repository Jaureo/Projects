#Encender o apagar
Power = 0
if Power == 0:
    Power = 1
#Reloj
import time
Segundos = 0
while Power == 1:
    time.sleep(1)
    Segundos = Segundos +1
    print (Segundos)
