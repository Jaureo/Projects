#Encendre o apagar
Power = 0
if Power == 0:
    Power = 1
#Rellotje
import time
Segons = 0
while Power == 1:
    time.sleep(1)
    Segons = Segons +1
    print (Segons)
