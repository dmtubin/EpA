from scipy import comb
import matplotlib.pyplot as plt
import numpy as np

from scipy import *
import numpy as np

def simulacion(distribucion,contador):
    for i in range (0,1000):
        dist=np.random.binomial(33,0.5)
        if dist==18:
            contador+=1
            i+=1
    print(contador)
    return contador

dist=0.0
c=0.0
lista=[]
for i in range (0,100):
    lista.append(simulacion(dist,c))
print(mean(lista),std(lista))


#funcion que simula mil votaciones 100 veces para calcular un promedio de las mediciones



p = 0.0
a = 0.0
b = 0.0
c = 0.0 
p1 = 0.0

pdf_x = []
pdf_y = []
for r in range(0,1000):
	a = comb (33,18)*((float(r*0.001))**18)*((1-float(r*0.001))**15)
	p+=a
	pdf_x.append(r*0.001)
	r+=1

for r in range(0,1000):
    c = comb (33,18)*((float(r*0.001))**18)*((1-float(r*0.001))**15)
    p2 = c/p
    pdf_y.append(p2)
    
    p1+=p2
    r+=1
 #hasta aca solo se definieron los ejes del primer grafico de la pdf    
    
print(max(pdf_y))
for i in range (0,len(pdf_y)):
    if pdf_y[i]==max(pdf_y):
        print(pdf_x[i])

#aca se calculo la ubicacion del  maximo de la distribucion


print(len(pdf_y))
aux=0.0
for i in range (500,1000):
    aux+=pdf_y[i]
print(aux)

#aqui se calculo la pregunta d :D


cdf_x = []
cdf_y = []

cdf1 = 0
cdf2 = 0
for i in range(0,1000):
	cdf1 = pdf_y[i]
	cdf2+=cdf1
	cdf_y.append(cdf2)
	cdf_x.append(i*0.001)
	#print cdf2
	i+=1

#calculo de la cdf
	
print(np.trapz(pdf_y,dx=1)) #integrador

plt.figure(1)
plt.plot(pdf_x,pdf_y, 'r-')
plt.ylabel("P(r|X)")
plt.title("PDF de la distribucion de r ")
#plt.show()

plt.figure(2)
plt.plot(cdf_x, cdf_y, 'r-')
plt.title("CDF de la distribucion de r vs r")
plt.ylabel("CDF")
plt.show()	
