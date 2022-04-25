import subprocess
import matplotlib.pyplot as pl
import numpy as np
lista_3M = []
for i in range(1,33):
    subprocess.call(['/usr/local/bin/ITGDec','/home/ubuntu/Desktop/DITG/receivers/receiver_'+str(i)+'.log','-d','600000','delay_'+str(i)+'.dat'])
    M3 = open('delay_'+str(i)+'.dat','r')
    lineas_3M = M3.readlines()
    linea_datos_3M = lineas_3M[1]
    dato_3M = linea_datos_3M.split(' ') 
    lista_3M.append(float(dato_3M[1]))
    subprocess.call(['sudo','rm','delay_'+str(i)+'.dat']) 

desviacion_3M = np.std(lista_3M)
media_3M = np.mean(lista_3M)
resultado_3M = (desviacion_3M/media_3M)*100

print "LA MEDIA ES:"
print media_3M

pl.figure()
pl.plot(lista_3M,label='3M')
pl.xlabel('Measurements')
pl.ylabel('Delay [ms]')
pl.savefig('Delay_'+str(media_3M)+'.png',format='png')