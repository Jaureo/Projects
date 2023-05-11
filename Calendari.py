#Encendre o apagar
Power = 0
if Power == 0:
    Power = 1
#Rellotje
import time
Segons = 0
Minuts = 0
Hores = 0
Dia = 0
while Power == 1:
    time.sleep(0.05)
    Segons = Segons +1
    if Segons == 60:
        Minuts = Minuts + 1
        Segons = 0
    if Minuts == 60:
        Hores = Hores + 1
        Minuts = 0
    if Hores == 24:
        Dia = Dia +1
        Hores = 0
    print (Dia, Hores, Minuts, Segons)
