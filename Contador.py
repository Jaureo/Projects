s=0
m=0
h=0
#Sumar i calcular
while h < 23:
  s = s+1
  if s >= 60:
    s = 0
    m = m+1

  if m >= 60:
    m = 0
    h = h+1

  if h >= 24:
    h = 0

  def formataDos(x):
    if (x < 10):
        return '0'+ str(x)
    else:
        return str(x)
  print (formataDos(h) + ':' + formataDos(m) + ':' + formataDos(s))
