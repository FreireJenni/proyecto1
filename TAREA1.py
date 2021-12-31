# Nombre: Jenniffer Lissette Freire Higuera
# Curso: 3er Nivel, Software A1

# Tipos de Datos y Acciones elementales 
#Ejercicio º1

lista = ("Hola mundo", "" , "Verdadero", "1", "c", "256", "8>19" )
print(lista)

#Resp: En una colección se almacenan estos datos

#Ejercicio º2

#ejemplo
res = 2 *(4 - 10 + 8)/2* 36 *(1/2)
print(res)
print(type(res))

#Resp: Se almacena el resultado en una variable tipo Float

#Ejercicio º4

num1 = 5
num2 = 7

sum = num1 + num2
res = num1 - num2
mu = num1 * num2
di = num1 / num2
md = num1 % num2

print(sum)
print(res)
print(mu)
print(di)
print (md)

#Ejercicio º5
from math import sqrt
x = 20
y = 6
z = 9
x1 = 0
x2 = 0
if ((y**2)-4*x*z) < 0:
     print("La solución de la ecuación es con numeros complejos")
else:
    x1 = (-y+sqrt(y**2-(4*x*z)))/(2*x)
    x2 = (-y-sqrt(y**2-(4*x*z)))/(2*x)
    print("Las soluciones de la ecuación son:")
    print(x1)
    print(x2)

print("Soluciones: ", x1 , x2)

#Ejercicio º6
import math

cateto1 = float(input("Introducir el cateto 1: "))
cateto2 = float(input("Introducir el cateto 2: "))

hp = math.sqrt((cateto1**2) + (cateto2**2))
print("Hipotenusa es igual a: ", hp)

#Ejercicio º7

n = int(input("Ingrese un número: "))
if n % 2 == 0:
    print("0")
else:
    print("1")

#Ejercicio º9

lista=[]
for v in range(4):
    val=int(input("Ingrese un valor entero: "))
    lista.append(val)

rep = lista.count(1)
if rep % 2 == 0:
    print("El codigo de paridad es 1")
else:
    print("El codigo de paridad es 0")

#Ejercio º10

valor_binario = '1010'

num_decimal = 0

for posicion, digito_string in enumerate(valor_binario[::-1]):
	num_decimal += int(digito_string) * 2 ** posicion

print(f'El número decimal que buscamos es {num_decimal}')

#Ejercicio º11

nume = int(input("Ingrese un numero entero de 4 cifras: "))
unidad_mil = nume / 1000
t = nume % 1000

cen = t / 100
t = t % 100

dec = t / 10
uni = t % 10

print("Unidades de mil : %i" % unidad_mil)
print("Centenas: %i" % cen)
print ("Decenas: %i" % dec)
print("Unidades: %i" % uni)

#Estructuras de Control de Flujo de Datos

#Ejercicio º1

año = 0
lis_1 = []
def string_int(mi_infor):
    for a in mi_infor:
        lis_1.append(int(a))
p_fecha = input("Ingrese la fecha en formato (ddmmaaaa): ")
string_int(p_fecha)

m = lis_1
n = lis_1[6]
o = lis_1[5]
p = lis_1[4]

if año % 4 != 0:
    print(" El año No es bisiesto")
elif año % 4 == 0 and año % 100 != 0:
    print(" El año Es bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0:
    print("El año No es bisiesyo")
elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0:
    print("El año Es bisiesto")

#Ejercicio º2 

lis_2 = []

def string_int(mi_infor):
    for a in mi_infor:
        lis_2.append(int(a))

p_num = input("Ingrese un numero entero de 5 digitos: ")
string_int(p_num)

m = lis_2[0]
n = lis_2[1]
o = lis_2[2]
p = lis_2[3]
q = lis_2[4]

if m == q:
    if n == p:
        print("El número ingresado es capicúa")
    else:
        print("El número ingresado NO es capicúa")
else:
    print("El número ingresado no es capicúa")

#Ejercicio º3

hora = int(input("Ingrese la cantidad de horas: "))
min= int(input("Ingrrese la cantidad de minutos: "))

h_a_s = hora * (3600)
m_a_s = min *(60)
total_seg = h_a_s +m_a_s

print("El total de segundos es: ", total_seg)

#Ejercicio º4

seg = int(input("Ingrese los segundos: "))

if seg > 0 :
    min = seg / 60
    horas = seg / 3600
    d = seg / 86400

    print("\n La cantidad de minutos es: ", min)
    print("\n La cantidad de horas es: ", horas)
    print("\n La cantidad de días es: ", d)
else:
    print("Ingrse una cantidad de segundos válida")

#Ejercicio º5

X = int(input("Ingrese el primero entero positivo: "))

if X > 0:
    Y = int(input("Ingrese el el segundo entero positivo: "))
    if Y > 0:
        Z = int(input("Ingrese el Tercer entero positivo: "))
        if Z > 0:
            if X > Y and X > Z:
                print("\n El mayor es: ", X)
                if Y > Z:
                    print("\n El segundo mayor es: ", Y)
                else:
                    print("\n El segundo mayor es: ", Z)
            elif Y > X and Y > Z:
                print("\n EL numero mayor es: ", Y)
                if X > Z:
                    print("\n El segundo mayor es: ", X)
                else: 
                     print("\n El segundo mayor es: ", Z)
            elif Z > X and Z > Y:
                print("\n EL numero mayor es: ", Z)
                if X > Y:
                    print("\n El segundo mayor es: ", X)
                else:
                    print("\n El segundo mayor es: ", Y)
            else:
                print("No se ha podido deteerminar el mayor de los 3 numeros") 
        else:
            print("Por favor ingrese un numero entero positivo")
    else:
        print("Por favor ingrese un numero entero positivo")
else:
    print("Por favor ingrese un numero entero positivo")

#Ejercicio º6

horas_e = int(input("Ingrese las horas en formato de 12 en la que se estaciono:"))
if horas_e >= 0 and horas_e <= 12:   
    min_e = int(input("Ingrese el o los minutos en la que se estaciono: "))   
    if min_e >= 0 and min_e < 60: 
        am_pm_e  = input("SI usted se estaciono en la mañana ingrese la letra A y si ingreso pasado del medio dìa ingrese la letra P: ") 
        if am_pm_e == "A" or am_pm_e == "P" :
            horas_s = int(input("Ingrese la hora en formato de 12 en la que sale del estacionamiento: "))
            if horas_s >= 0 and horas_s <= 12:
                s_s= int(input("Ingrese la hora en la que sale del estacionamiento: ")) 
                if s_s >= 0 and s_s < 60:
                    am_pm_sale = input("SI usted sale del estacionamiento en la mañana ingrese la letra A y si salio pasado del medio dìa ingrese la letra P: ")
                    if am_pm_sale == "A" or am_pm_sale == "P" :
                        if am_pm_e == "A" and am_pm_sale == "A" or am_pm_e == "A" and am_pm_sale == "P" or am_pm_e == "P" and am_pm_sale == "P":
                            if am_pm_e == "A" and am_pm_sale == "A" or am_pm_e == "P" and am_pm_sale == "P":
                                res_H = horas_e - horas_s
                                T_Horas = res_H * 4
                                res_M = min_e - s_s
                                T_Min = res_M/30
                                T_Min_2 = 0
                                if T_Min < 0 :
                                    T_Min_2 = 2.50
                                    T_Tiempo = T_Horas + T_Min_2
                                    print("El Valor a pagar es: Bs", T_Tiempo)
                            elif am_pm_e == "A" and am_pm_sale == "P":
                                horas_s+=12
                                rest_Horas = horas_e - horas_s
                                Total_Horas = rest_Horas * 4
                                rest_min = min_e - s_s
                                Total_Min = rest_min/3
                                Total_Min_2 = 0
                                if Total_Min < 0 :
                                    Total_Min_2 = 2.50
                                    Total_Tiempo = Total_Horas + Total_Min_2
                                    print("El Valor a pagar es: Bs", Total_Tiempo)
                        else:
                            print("Los datos de entrada y salida no coinciden")
                    else:
                        print("Ingrese una Letra Valida")
                else:
                    print("Ingrese unos minutos de salida valido")        
            else:
                print("Ingrese una hora de salida valida")
        else:
            print("Ingrese una letra valida")    
    else:
        print("Ingrese una cantidad de minutos valido")   
else:
    print("Ingrese una hora de entrada valida")

#Ejercicio º7

libras = float(input("Ingrese su peso en Libras: "))
cm = int(input("Ingrese su Altura en Centimetros: "))

peso = libras*0.453592
altura = cm /100

prom = peso/(altura * altura)

print("Su peso en Kg es: ", peso)
print("Su altura en Metros es: ", altura)
print("Su promedio es: ", prom)

if prom < 16 :
    print("Su categoria es Criterio de ingreso.")
elif prom >= 16 and prom <= 16.9:
    print("Su categoria es infra peso.")
elif prom >= 17 and prom <= 18.4:
    print("Su categoria es bajo peso.")
elif prom >= 18.5 and prom <= 24.9:
    print("Su categoria es peso normal.")
elif prom >= 25 and prom <= 29.9:
    print("Su categoria es sobrepeso.")
elif prom >= 30 and prom <= 34.9:
    print("Su categoria es obesidad pre-mórbida.")
elif prom >= 40 and prom <= 45:
    print("Su categoria es obesidad mórbida.")
elif prom > 45 :
    print("Su categoria es obesidad híper-mórbida.")

#Ejercicio º8

r = int(input("Ingrese un dia correspondiente al 2014: "))
if r > 0 and r < 31:
    mes = int(input("Ingrese un numero de mes correspondiente al 2014: "))
    if mes > 0 and mes <=12 :
        d_Mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        x = 0
        acum = 0
        while x <= mes - 1:
            acum = acum + d_Mes[x]
            i = i + 1
        total = acum + r
        print("\n EL total de dias que han transcurrido desde el 1 de enero del 20154 hasta la fecha que solicito es: ", total)

#Ejercicio ª9

mes = int(input("Ingrese un numero entre el 1 y el 12: "))
if mes > 0 and mes <= 12 :
    if mes == 1 :
        print("Enero")
    elif mes ==2 :
        print("Febrero")
    elif mes ==3 :
        print("Marzo")
    elif mes ==4 :
        print("Abril")
    elif mes ==5 :
        print("Mayo")
    elif mes ==6 :
        print("Junio")
    elif mes ==7 :
        print("Julio")
    elif mes ==8 :
        print("Agosto")
    elif mes ==9 :
        print("Septiembre")
    elif mes ==10 :
        print("Octubre")
    elif mes ==11:
        print("Noviembre")
    elif mes ==12 :
        print("Diciembre")       
else:
    print("Ingrese un numero valido")

#Ejercicio º10

u = float(input("Ingrese la cantidad a pagar en el almacen: "))

if u > 1000:
    tot = u * 0.80
    print("SU total a pagar aplicando el descuento de la tienda es de: Bs", tot)
else:
    print("Su total a pagar es de: Bs", u)

#Estructuras Iterativas

#Ejercicio º1

import math
nume = int(input("Ingrese un número entero: "))
if nume > 0:
    dg = int(math.log10(nume))+1
    print(dg)
elif nume == 0:
    dg = 1
    print(dg)
elif nume < 0:
    print("Ingrese un número válido")

#Ejercicio º2

def invertir_numero(n):
    n3 = 0
    while n!= 0:
        n3 = 10*n3+n % 10
        n //= 10
    return n3

def cap(n3):
    return n3 == invertir_numero(n3)

nums = [11, 20, 123, 9889, 2811, 1801, 777, 12321, ]

for n3 in nums:
    es_cap = cap(n3)
    print(f"El número {n3} es capicúa? {es_cap}")

#Ejercicio º3

def es_p(n4):
    con = 0

    for a in range(1, n4+1):
        if n4 % a == 0:
            con += 1
    
    if con == 2:
        print("Es un numero primo")
        return True
    else:
        print("No es un numero primo")
        return False
n5 = int(input("Ingrese un numero primo positico: "))
if n5 > 0:
    print(es_p(n5))  

#Ejercicio º4

A = int(input("Ingrese un numero entero: "))
if A >= 0 :
    B = 1
    C = 1
    while B <= A:
        C = C *B 
        B += 1
    print("El factorial de ",A," es: ",C)
else:
    print("No se pudo calcular el factorial")

#Ejercicio º5

def vali(valor):
    	return False

v = 0
while not v:
    contraseña = input("Introduzca una contraseña con al menos 10 digitos: ")
    v = len(contraseña) >= 10
print("\n Felicidades has ingresado una contraseña valida")

#Ejercicio º6

def secuencia_menor_mayor():
    ingresa = True
    lista = []
    while ingresa:
        valor = int(input("Ingresa un valor o 0 para finalizar, debe ser un valor entero: "))
        if valor == 0:
            break
        else:
            lista.append(valor) 
    print(lista)
    print(u'Menor %s' % min(lista)) 
    menor = lista[0] 
    mayor = lista[0] 
    for elemento in lista: 
        if elemento < menor: 
            menor = elemento
    for elemento in lista:
        if elemento > mayor:
            mayor = elemento
    print(u'Menor %s' % menor)
    print(u'Mayor %s ' % max(lista))
    print(u'Mayor %s ' % mayor)

#Ejercicio º7

def secuencia(self):
            edad=[18,24,25,30,35,36]
            p=[40,50,60,70,80]
            esta=[1.40,1.45,1.50,1.55,1.60,1.70]
            p_edad=(sum())/len()
            p_peso=(sum(p))/len(p)
            p_es=(sum(p))/len(esta)
            c=0
            x=0
            while c<8:
                x+=(p_edad.count(18+c))
                c+=1  
            c=1
            mayores_36=0  
            while c<150:
                mayores_36+=(p_edad.count(36+c))
                c+=1
            c=0
            freire=0
            while c<36:
                freire=[i for i,x in enumerate(p_edad) if x>=18 and x<=35]
                c+=1
            suma=0
            c=0
            while c<len(freire):
                suma+=p[freire[0+c]]
                c+=1
            print(freire)
            print("promedio de la edad :", p_edad)
            print("promedioa del peso : ", p_peso)
            print("promedio de la  estatura : " ,p_es)
            print("un rango entre 18 y 25 : ", x)
            print("personas mayores : " , mayores_36)
            print("promedio de pesos de todas las personas : " , suma/len(freire))

#Ejercicio º8

def algoritmo(self):
        for w in range (10):
            print("tabla de mult: "+str(w+1))
            for v in range (12):
                print(str(+1)+"*"+str(v+1)+"="+str(w+1)* (v+1))
                print ("\n")  

#ejercicio 9 y 10
def fichas(self):
        for o in range(0,7):
            for e in range(0, o+1):
                print("|" + str(o) + "|" + str(e) + "|")

def numeros_positivos(self):
        c=0
        numeros_posi=0
        while True:
            nume=int(input("Ingrese  números positivos: "))
            if nume==0:
                break
            elif nume > 1:
                numeros_posi+=nume
                c+=1
                prome1=numeros_posi/c
            print("serie promedio : " ,prome1 )       

#Prodecimientos (Acciones y Funciones)

#Ejercicio º1

def edades_usuarios(self):
        c=0
        e_ma=0
        while True:
            print("presione [enter] para dejar de ingresar notas!")
            edades=(input("ingrese las edades a promediar:"))
            if edades=='':
                break
            elif edades >= "18":
                edades=int(edades)
                e_ma+=edades
                c+=1
                pro=e_ma/c
        return pro

#Ejercicio º2

def Eleva(self):
    ba=int(input("ingrese la base: "))
    exponente=int(input("ingrese el exponente: "))
    exponente= 2
    result=ba**exponente
    print(f"El resultado es: {result} ")

#Ejercicio º3

def peri(self):
    lado=float(input("Ingrese el valor de uno de los lados del pentágono:"))
    perimetro=5*lado
    return perimetro

#Ejercicio º4
def calcula_pago(horas, valor, extra=False):
    if extra:
        total = round(horas * valor, 2)
        return total + ((total*35) / 100.0)
    return round(horas * valor, 2)

def horas_extras():
    i = 1
    data = []
    datos = {}
    while i <= 5:
        empleado = input("Identificación del empleado: ")
        valor = float(input("Valor por hora, debe ser un valor numerico: "))
        horas = int(input("Horas laboradas, debe ser un valor entero: "))
        datos = {'identificacion': empleado, 'valor': valor, 'horas': horas}
        data.append(datos)
        i += 1
    for d in data:
        if int(d['horas']) <= 40:
            print(u'Empleado: %s, valor_hora: %s, horas_lab: %s, extras: %s, TOTAL_PAGO: %s, TOTAL_EXTRAS: %s' %(d['identificacion'], d['valor'], d['horas'], 0, calcula_pago(d['valor'], d['horas']), 0))
        else:
            print(u'Empleado: %s, valor_hora: %s, horas_lab: %s, extras: %s, TOTAL_PAGO: %s, TOTAL_EXTRAS: %s' % (d['identificacion'], d['valor'], d['horas'], d['horas'] - 40, calcula_pago(d['valor'], 40), calcula_pago(d['valor'], int(d['horas']) - 40, True)))

#Ejercicio º5

def horas(self):
        def MillasAKilometros(mi):
            kilome=mi*1.60935
            return kilome
        ci=['']*12
        xyz=['A','B','','C','D','','F','G','','H','I']
        ind=0
        while ind<=11:
            if ind==0 or ind==1 or ind==3 or ind==4 or ind==6 or ind==7 or ind==9 or ind==10:
                while ci[ind]<='':
                    ci[ind]=input(f"Ingrese ciudad {xyz[0+ind]}: ")
                ind+=1
            else:
                while ci[ind]<='':
                    ci[ind]=input(f"Ingrese distancia entre ciudades en millas: ")
                ind+=1
        print(f"\nEntre {ci[0]} y {ci[1]}, hay {MillasAKilometros(int(ci[2])):.2f} Km de distancia\n")
        print(f"Entre {ci[3]} y {ci[4]}, hay {MillasAKilometros(int(ci[5])):.2f} Km de distancia\n")
        print(f"Entre {ci[6]} y {ci[7]}, hay {MillasAKilometros(int(ci[8])):.2f} Km de distancia\n")
        print(f"Entre {ci[9]} y {ci[10]}, hay {MillasAKilometros(int(ci[11])):.2f} Km de distancia\n")


    





       
           
               
    
               
     
        

            


            


