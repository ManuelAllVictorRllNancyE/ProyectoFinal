#! /usr/bin/env pyhton

import numpy as np
import random as rd

#Funciones de Mitosis

def Mitosis_c(x,y,A,tipo,hijas):  #La función come las entradas, la matriz, el valor de la célula, la cantidad de cuadros que se quiera replicar
    i = 0
    limit = 0
    while i < hijas: 
        rx, ry = rd.randint(-1,1), rd.randint(-1,1) #Se crean dos dados que pueden oscilar entre -1 y 1
        cell = A[x+rx, y+ry]
        if cell == 0:
            A[x+rx, y+ry] = tipo
            i += 1 #Va a colocar aleatoriamente en un cadrado de 3x3 números hasta igual a la cantidad deseada
        else:
            None
        limit += 1
        if limit == 10: #Depues de diez intentos, si no lo logró, se acaba y rompe el proceso...
            #print("Poco espacio para duplicar")
            break   

def Mitosis_L(x,y,A,tipo,hijas):
    i = 0
    limit = 0
    while i < hijas:
        rx, ry = rd.randint(-1,1), rd.randint(0,1) #Cambiamos los valores que puede tomar uno de los numeros aleatorios para cuando la célula este pegada a la pared izquierda de la caja
        cell = A[x+rx, y+ry]
        if cell == 0:
            A[x+rx, y+ry] = tipo
            i += 1
        else:
            None
        limit += 1
        if limit == 10:
            #print("Poco espacio para duplicar")
            break           

def Mitosis_D(x,y,A,tipo,hijas):
    i = 0
    limit = 0
    while i < hijas:
        rx, ry = rd.randint(-1,1), rd.randint(-1,0) #Cambiamos los valores que puede tomar uno de los numeros aleatorios para cuando la célula este pegada a la pared derecha de la caja
        cell = A[x+rx, y+ry]
        if cell == 0:
            A[x+rx, y+ry] = tipo
            i += 1
        else:
            None
        limit += 1
        if limit == 10:
            #print("Poco espacio para duplicar")
            break   

def Mitosis_Top(x,y,A,tipo,hijas):
    i = 0
    limit = 0
    while i < hijas:
        rx, ry = rd.randint(0,1), rd.randint(-1,1) #Cambiamos los valores que puede tomar uno de los numeros aleatorios para cuando la célula este pegada a la pared izquierda de la caja
        cell = A[x+rx, y+ry]
        if cell == 0:
            A[x+rx, y+ry] = tipo
            i += 1
        else:
            None
        limit += 1
        if limit == 10:
            #print("Poco espacio para duplicar")
            break   

def Mitosis_Flat(x,y,A,tipo,hijas):
    i = 0
    limit = 0
    while i < hijas:
        rx, ry = rd.randint(-1,0), rd.randint(-1,1) #Cambiamos los valores que puede tomar uno de los numeros aleatorios para cuando la célula este pegada a la pared de abajo de la caja
        cell = A[x+rx, y+ry]
        if cell == 0:
            A[x+rx, y+ry] = tipo
            i += 1
        else:
            None
        limit += 1
        if limit == 10:
            #print("Poco espacio para duplicar")
            break               

def Mitosis_SI(x,y,A,tipo,hijas): #Superor izquierda
    i = 0
    limit = 0
    while i < hijas:
        rx, ry = rd.randint(0,1), rd.randint(0,1) #Cambiamos los valores que puede tomar uno de los numeros aleatorios para cuando la célula este pegada en las ezquinas de la caja
        cell = A[x+rx, y+ry]
        if cell == 0:
            A[x+rx, y+ry] = tipo
            i += 1
        else:
            None
        limit += 1
        if limit == 10:
            #print("Poco espacio para duplicar")
            break              
            
def Mitosis_SD(x,y,A,tipo,hijas): #Superor derecha
    i = 0
    limit = 0
    while i < hijas:
        rx, ry = rd.randint(0,1), rd.randint(-1,0)
        cell = A[x+rx, y+ry]
        if cell == 0:
            A[x+rx, y+ry] = tipo
            i += 1
        else:
            None
        limit += 1
        if limit == 10:
            #print("Poco espacio para duplicar")
            break   

def Mitosis_II(x,y,A,tipo,hijas): #Inferior izquierda
    i = 0
    limit = 0
    while i < hijas:
        rx, ry = rd.randint(-1,0), rd.randint(0,1)
        cell = A[x+rx, y+ry]
        if cell == 0:
            A[x+rx, y+ry] = tipo
            i += 1
        else:
            None
        limit += 1
        if limit == 10:
            #print("Poco espacio para duplicar")
            break               
            
def Mitosis_ID(x,y,A,tipo,hijas): #Inferior izquierda
    i = 0
    limit = 0
    while i < hijas:
        rx, ry = rd.randint(-1,0), rd.randint(-1,0)
        cell = A[x+rx, y+ry]
        if cell == 0:
            A[x+rx, y+ry] = tipo
            i += 1
        else:
            None
        limit += 1
        if limit == 10:
            #print("Poco espacio para duplicar")
            break               
            
def Mitosis(x,y,A,tipo,hijas): #Al final una función examina en cual de los casos está la célula a dividir y ejecuta depnendiendo sea el caso
    if x == 0 and y == 0:
        Mitosis_SI(x,y,A,tipo,hijas)
    elif x == len(A)-1 and y == len(A)-1:
        Mitosis_ID(x,y,A,tipo,hijas)
    elif x == 0 and y == len(A)-1:
        Mitosis_SD(x,y,A,tipo,hijas)
    elif x == len(A)-1 and y == 0:
        Mitosis_II(x,y,A,tipo,hijas)
    
    elif x == 0:
        Mitosis_Top(x,y,A,tipo,hijas)
    elif x == len(A)-1:
        Mitosis_Flat(x,y,A,tipo,hijas)
    elif y == 0:
        Mitosis_L(x,y,A,tipo,hijas)
    elif y == len(A)-1:
        Mitosis_D(x,y,A,tipo,hijas)
    
    else:
        Mitosis_c(x,y,A,tipo,hijas)

#Funciones de Gemación
def Gema_C(x,y,A,tipo): #Come la localización de la casilla a duplicar, su mariz y el tipo.
    i=0
    limit=0
    while i < 1: #Solo puede tener una hija a la vez 
        r= rd.randint(0,3) #Se suelta un numero  al azar y colocara el número del tipo en la casilla que corresponda al número al azar si la casila está desocupada
        if r == 0 and A[x+1,y] == 0:
            A[x+1,y] = tipo
            i += 1
        elif r == 1 and A[x-1,y] == 0:
            A[x-1,y] = tipo
            i += 1
        elif r == 2 and A[x,y+1] == 0:
            A[x,y+1] = tipo
            i += 1
        elif r == 3 and A[x,y-1] == 0:
            A[x,y-1]= tipo
            i += 1
        else:
            None
        limit += 1
        if limit == 10: #Si depues de 10 intentos no lo logra, lo más porbable es que todas estén ocupadas. se rompe la función
            break   
            
def Gema_L(x,y,A,tipo): #Pared izquierda 
    i = 0 #Al igual que con mitosisi  hay una para cada caso
    limit = 0
    while i < 1:
        r= rd.randint(0,2)
        if r == 0 and A[x+1,y] == 0:
            A[x+1,y] = tipo
            i += 1
        elif r == 1 and A[x-1,y] == 0:
            A[x-1,y] = tipo
            i += 1
        elif r == 2 and A[x,y+1] == 0:
            A[x,y+1] = tipo
            i += 1
        else:
            None
        limit += 1
        if limit == 10:
            break  
            
def Gema_R(x,y,A,tipo): #Pared derecha
    i = 0
    limit = 0
    while i < 1:
        r= rd.randint(0,2)
        if r == 0 and A[x+1,y] == 0:
            A[x+1,y] = tipo
            i += 1
        elif r == 1 and A[x-1,y] == 0:
            A[x-1,y] = tipo
            i += 1
        elif r == 2 and A[x,y-1] == 0:
            A[x,y-1]= tipo
            i += 1
        else:
            None
        limit += 1
        if limit == 10:
            break  

def Gema_F(x,y,A,tipo): #Pared de ababjo (F = floor)
    i = 0
    limit = 0
    while i < 1:
        r= rd.randint(0,2)
        if r == 0 and A[x-1,y] == 0:
            A[x-1,y] = tipo
            i += 1
        elif r == 1 and A[x,y+1] == 0:
            A[x,y+1] = tipo
            i += 1
        elif r == 2 and A[x,y-1] == 0:
            A[x,y-1]= tipo
            i += 1
        else:
            None
        limit += 1
        if limit == 10:
            break  
            
def Gema_T(x,y,A,tipo): #Pared de arriba (T = top)
    i = 0
    limit = 0
    while i < 1:
        r= rd.randint(0,2)
        if r == 0 and A[x+1,y] == 0:
            A[x+1,y] = tipo
            i += 1
        elif r == 1 and A[x,y+1] == 0:
            A[x,y+1] = tipo
            i += 1
        elif r == 2 and A[x,y-1] == 0:
            A[x,y-1]= tipo
            i += 1
        else:
            None
        limit += 1
        if limit == 10:
            break  
            
def Gema_TL(x,y,A,tipo):
    i = 0
    limit = 0
    while i < 1:
        r= rd.randint(0,1)
        if r == 0 and A[x+1,y] == 0:
            A[x+1,y] = tipo
            i += 1
        elif r == 1 and A[x,y+1] == 0:
            A[x,y+1] = tipo
            i += 1
        else:
            None
        limit += 1
        if limit == 10:
            break  
            
def Gema_TR(x,y,A,tipo):
    i = 0
    limit = 0
    while i < 1:
        r= rd.randint(0,1)
        if r == 0 and A[x+1,y] == 0:
            A[x+1,y] = tipo
            i += 1
        elif r == 1 and A[x,y-1] == 0:
            A[x,y-1] = tipo
            i += 1
        else:
            None
        limit += 1
        if limit == 10:
            break  
            
def Gema_BL(x,y,A,tipo):
    i = 0
    limit = 0
    while i < 1:
        r= rd.randint(0,1)
        if r == 0 and A[x-1,y] == 0:
            A[x-1,y] = tipo
            i += 1
        elif r == 1 and A[x,y+1] == 0:
            A[x,y+1] = tipo
            i += 1
        else:
            None
        limit += 1
        if limit == 10:
            break  
            
def Gema_BR(x,y,A,tipo):
    i = 0
    limit = 0
    while i < 1:
        r= rd.randint(0,1)
        if r == 0 and A[x-1,y] == 0:
            A[x-1,y] = tipo
            i += 1
        elif r == 1 and A[x,y-1] == 0:
            A[x,y-1] = tipo
            i += 1
        else:
            None
        limit += 1
        if limit == 10:
            break  
            
def Gema(x,y,A,tipo):  #Está función examina en que posición está la casilla a duplicar y ejecuta dependiendo el caso
    if x == 0 and y == 0:
        Gema_TL(x,y,A,tipo)
    elif x == len(A)-1 and y == len(A)-1:
        Gema_BR(x,y,A,tipo)
    elif x == 0 and y == len(A)-1:
        Gema_TR(x,y,A,tipo)
    elif x == len(A)-1 and y == 0:
        Gema_BL(x,y,A,tipo)
    elif x == 0:
        Gema_T(x,y,A,tipo)
    elif x == len(A)-1:
        Gema_F(x,y,A,tipo)
    elif y == 0:
        Gema_L(x,y,A,tipo)
    elif y == len(A)-1:
        Gema_R(x,y,A,tipo)
    else:
        Gema_C(x,y,A,tipo)
        
def Gemaject_C(x,y,M,N,edad): #Pide la entrada de la matriz, la matriz con la edad de la célula, la matriz con la posición de la célula y la edad (Valor de la casilla de edad) en la que va a separarse.
    #Esta función desplaza un cuado en la dirección en la que se ubica la hija respecto de la madre y de uno a ods cuadros perpendiculares
    #Si la hija está sobre la madre, dzplaza otro arriba y de uno a dos caudo a la izaquierda o a la derecha 
    
    if M[x+1,y] == edad and x+2 < len(M)-1: #Si la casilla edad abajo de la casilla de edad de la madre tienen cierta edad y no está cerca del fondo....
        r = rd.randint(-2,2) #Lanza un dado de -2 a 2 
        M[x+2,y+r] = 0 #Vuelve la casilla de edad a la que la hija se va a dezplazar, cero
        M[x+2,y+r] = M[x+1,y] #Vuelve la casilla de edad a la que la hija se va a dezplazar el valor de tiempo en el que se quedó
        M[x+1,y] = 0  #Vuelve la casilla de endad en la que estaba la hija, cero
        
        N[x+2,y+r] = 0 #Vuelve la casilla a la que la hija a a llegar, cero
        N[x+2,y+r] = N[x+1,y] #Desplza a la hijo ahí
        N[x+1,y] = 0 #Desocupa donde estaba la hija...
              
    elif M[x-1,y] == edad and x-2 > 0: 
        r = rd.randint(-2,2)
        M[x-2,y+r] = 0
        M[x-2,y+r] = M[x-1,y]
        M[x-1,y] = 0
            
        N[x-2,y+r] = 0
        N[x-2,y+r] = N[x-1,y]
        N[x-1,y] = 0
             
    elif M[x,y+5] == edad and y+2 < len(M)-1: 
        r = rd.randint(-2,2)
        M[x+r,y+2] = 0
        M[x+r,y+2] = M[x,y+1]
        M[x,y+1] = 0
            
        N[x+r,y+2] = 0
        N[x+r,y+2] = N[x,y+1]
        N[x,y+1] = 0
            
    elif M[x,y-1] == edad and y-2 > 0:
        r = rd.randint(-2,2)
        M[x+r,y-2] = 0
        M[x+r,y-2] = M[x,y-1]
        M[x,y-1] = 0
                
        N[x+r,y-2] = 0
        N[x+r,y-2] = N[x,y-1]
        N[x,y-1] = 0        
                    
def Gemaject_D(x,y,M,N,edad): #El caso cuando la hija está a la derecha y muy cerca de la orilla derecha 
    
    if M[x+1,y] == edad and x+2 < len(M)-1:
        r = rd.randint(-2,2)
        M[x+2,y+r] = 0
        M[x+2,y+r] = M[x+1,y]
        M[x+1,y] = 0
        
        N[x+2,y+r] = 0 
        N[x+2,y+r] = N[x+1,y]
        N[x+1,y] = 0
            
    elif M[x-1,y] == edad and x-2 > 0:
        r = rd.randint(-2,2)
        M[x-2,y+r] = 0
        M[x-2,y+r] = M[x-1,y]
        M[x-1,y] = 0
        
        N[x-2,y+r] = 0
        N[x-2,y+r] = N[x-1,y]
        N[x-1,y] = 0
            
    elif M[x,y+1] == edad and y+2 < len(M)-1:
        r = rd.randint(-2,2)
        M[x+r,y+2] = 0
        M[x+r,y+2] = M[x,y+1]
        M[x,y+1] = 0
        
        N[x+r,y+2] = 0
        N[x+r,y+2] = N[x,y+1]
        N[x,y+1] = 0

        
def Gemaject_I(x,y,M,N,edad): #El caso cuando la hija está a la izquierda y muy cerca de la orilla izquierda 
    
    if M[x+1,y] == edad and x+2 < len(M)-1:
        r = rd.randint(-2,2)
        M[x+2,y+r] = 0
        M[x+2,y+r] = M[x+1,y]
        M[x+1,y] = 0
        
        N[x+2,y+r] = 0 
        N[x+2,y+r] = N[x+1,y]
        N[x+1,y] = 0
            
    elif M[x-1,y] == edad and x-2 > 0:
        r = rd.randint(-2,2)
        M[x-2,y+r] = 0
        M[x-2,y+r] = M[x-1,y]
        M[x-1,y] = 0
        
        N[x-2,y+r] = 0
        N[x-2,y+r] = N[x-1,y]
        N[x-1,y] = 0
            
    elif M[x,y+1] == edad and y+2 < len(M)-1:
        r = rd.randint(-2,2)
        M[x+r,y+2] = 0
        M[x+r,y+2] = M[x,y+1]
        M[x,y+1] = 0
        
        N[x+r,y+2] = 0
        N[x+r,y+2] = N[x,y+1]
        N[x,y+1] = 0
            
def Gemaject_A(x,y,M,N,edad): #El caso cuando la hija está arriba y muy cerca de la orilla superior
    
    if M[x+1,y] == edad and x+2 < len(M)-1:
        r = rd.randint(-2,2)
        M[x+2,y+r] = 0
        M[x+2,y+r] = M[x+1,y]
        M[x+1,y] = 0
        
        N[x+2,y+r] = 0 
        N[x+2,y+r] = N[x+1,y]
        N[x+1,y] = 0
            
    elif M[x,y+1] == edad and y+2 < len(M)-1:
        r = rd.randint(-2,2)
        M[x+r,y+2] = 0
        M[x+r,y+2] = M[x,y+1]
        M[x,y+1] = 0
        
        N[x+r,y+2] = 0
        N[x+r,y+2] = N[x,y+1]
        N[x,y+1] = 0
            
    elif M[x,y-1] == edad and y-2 > 0:
        r = rd.randint(-2,2)
        M[x+r,y-2] = 0
        M[x+r,y-2] = M[x,y-1]
        M[x,y-1] = 0
        
        N[x+r,y-2] = 0
        N[x+r,y-2] = N[x,y-1]
        N[x,y-1] = 0        
                                                
def Gemaject_B(x,y,M,N,edad): #El caso cuando la hija está abajo y muy cerca de la orilla inferior
            
    if M[x-1,y] == edad and x-2 > 0:
        r = rd.randint(-2,2)
        M[x-2,y+r] = 0
        M[x-2,y+r] = M[x-1,y]
        M[x-1,y] = 0
        
        N[x-2,y+r] = 0
        N[x-2,y+r] = N[x-1,y]
        N[x-1,y] = 0
            
    elif M[x,y+1] == edad and y+2 < len(M)-1:
        r = rd.randint(-2,2)
        M[x+r,y+2] = 0
        M[x+r,y+2] = M[x,y+1]
        M[x,y+1] = 0
        
        N[x+r,y+2] = 0
        N[x+r,y+2] = N[x,y+1]
        N[x,y+1] = 0
            
    elif M[x,y-1] == edad and y-2 > 0:
        r = rd.randint(-2,2)
        M[x+r,y-2] = 0
        M[x+r,y-2] = M[x,y-1]
        M[x,y-1] = 0
        
        N[x+r,y-2] = 0
        N[x+r,y-2] = N[x,y-1]
        N[x,y-1] = 0        

        
def Neubauer(N,tipo):
    
    Cuentos=0
    for x in range (len(N)): #Recorre toda la matriz
        for y in range(len(N)):
            if N[x,y]==tipo: #Si encuentras una csilla con el valor indicado
                Cuentos= Cuentos+1 #Añade un uno al contador 
    return Cuentos      #Regresa la cantidad que contaste

def plant_rand(N,cantidad, tipo): Come una matriz, la cantidad de células a plantar y el valor que tendrán
    i=0
    while i < cantidad: #Mientras o exedas la cantidad a plantar
        rx, ry = rd.randint(0,len(N)-1), rd.randint(0,len(N)-1) #Elije un espacio al azar
        if N[rx, ry] == 0: #Si está desocupado
            N[rx, ry] = tipo #Planta una célula ahi, ambiando el valor de la casilla de cero a la del tipo
            i += 1
            
def sensor(x,y,M,tipo): #Come corrodenadas, la matriz y el tipo de célula que queremos identificar
    i = 0
    for n in range(-1,2): #Los for rcorren las casidllas aledañas
        for m in range(-1,2):
            if M[x+n,y+m] == tipo: #Si encuentras una del tipo a buscar, vuelve a i=1
                i = i + 1
    if i > 0: #Si encontraste manda un true
        return True
    else: #Si no, manda un false
        return False
    
def citoeat(x,y,M,T,alimento): #Pide las cooordenadas de la célula, la matríz en la que está, la metriz de edad asocidad a la del cultivo y la cantidad de células a comer
    i = 0
    while i < alimento:
        for n in range(-1,2): #Los dos for buscan an las casillas de alrededor
            for m in range(-1,2):
                if M[x+n,y+m] != 0: #Si encuentras una célula
                    M[x+n,y+m] = 0 #Matala, desocupa ese espació
                    T[x+n,y+m] = 0 #como el espacio está desocupado, no hay célula que envejesca 
                    i = i + 1  
                    
def Gemaject(x,y,M,N,edad): #Función que aplicará la función de desplazamiento adecuado dependiedno de caso de la célula
    if x == 2:
        Gemaject_A(x,y,M,N,edad)#<>
    elif y == 2:
        Gemaject_I(x,y,M,N,edad)
    elif x == len(N)-2:
        Gemaject_B(x,y,M,N,edad)
    elif y == len(N)-2:
        Gemaject_D(x,y,M,N,edad)
    else:
        Gemaject_C(x,y,M,N,edad)