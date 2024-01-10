import csv
import os

def interpolazione(lista, v1, v2, k):
    vf=v2+k*(v1-v2)
    return vf

cwd=os.getcwd()
print("Scegli:\t[1] Tensione di vapore (P data T);\n\
\t[2] Tensione di vapore (T data P).\n")
test=True
while test==True:
    n=int(input("Inserire un valore: "))
    if n==1:
        file="waterpressure"
        test=False
    else:
        if n==2:
            file="waterpressure"
            test=False
        else:
            print("Valore non valido!")

csv_path=os.path.join(cwd, f"{file}.csv")
file=open(csv_path, newline="")
table=csv.reader(file)

#creo una lista per ogni colonna della tabella
T_list=[]
P_list=[]

for row in table:
    T_list.append(float(row[0]))
    P_list.append(float(row[1]))
    
#leggo le temperature minima e massima
T_inf=T_list[0] #temperatura limite inferiore
T_sup=T_list[-1]    #temperatura limite superiore
#leggo le pressioni minima e massima
P_inf=P_list[0] #pressione limite inferiore
P_sup=P_list[-1]    #pressione limite superiore
cond=True
while cond==True:
    if n==1:
        #input temperatura
        T=float(input("Inserire una temperatura [°C]: "))
        #-----
        if T>=T_inf and T<=T_sup:
            if T in T_list:
                i=T_list.index(T)
                P=P_list[i]
                
            else:
                for j in range(len(T_list)):
                    if T>T_list[j]:
                        i=j
                    k=(T_list[i+1]-T)/(T_list[i+1]-T_list[i])
                    P=round(interpolazione(P_list, P_list[i], P_list[i+1], k), 7)

            print(f"\nTensione di vapore (acqua) a {T}°C: P = {P} MPa.")
            print(80*"-")#,"\n")

        else:
            if T>T_sup:
                print(f"\n\tATTENZIONE! Valore troppo alto (max {T_sup} °C).\n")
            elif T<T_inf:
                print(f"\n\tATTENZIONE! Valore troppo basso (min {T_inf} °C).\n")
        #-----
    elif n==2:
        #input pressione
        P=float(input("Inserire una pressione [MPa]: "))
        if P>=P_inf and P<=P_sup:
            if P in P_list:
                        i=T_list.index(P)
                        T=T_list[i]
            else:
                for j in range(len(P_list)):
                    if P>P_list[j]:
                        i=j
                    k=(P_list[i+1]-P)/(P_list[i+1]-P_list[i])
                    T=round(interpolazione(T_list, T_list[i], T_list[i+1], k), 2)
            print(f"\nTemperatura di evaporazione (acqua) a {P} MPa: T = {T} °C.")
            print(80*"-")#,"\n")
        
        else:
            if P>P_sup:
                print(f"\n\tATTENZIONE! Valore troppo alto (max {P_sup} MPa).\n")
            elif P<P_inf:
                print(f"\n\tATTENZIONE! Valore troppo basso (min {P_inf} MPa).\n")
