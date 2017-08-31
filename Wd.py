# -*- coding: utf-8 -*-
import os
os.system("cls") #czyszczenie
import pandas as pd


#kolumny ["Nazwa","Węgiel ","Wodor","Azot","Tlen","Siarka","Popioł","Woda","Chlor","Fosfor"]
paliwa=pd.read_csv('paliwa.csv',)
    
#Pętla dodawania paliw
b = 't'
while b == 't':
    nazwa=input("Podaj nazwę paliwa "   )
    c=input("Zawartość węgla ")
    c=int(c)/100
    h=input("Zawartość wodoru ")
    h=int(h)/100
    o=input("Zawartość tlenu ")
    o=int(o)/100
    s=input("Zawartość siarki ")
    s=int(s)/100
    a=input("Zawartość popiołu ")
    #popiol a, nie p#
    a=int(a)/100
    w=input("Zawartość wilgoci ")
    w=int(w)/100
    cl=input("Zawartość chloru ")
    cl=int(cl)/100
    p=input("Zawartość fosforu ")
    p=int(p)/100
    #Obliczanie azotu jako uzupełnianie    
    n=1-c-h-o-s-a-w-cl-p
    if n<0 :
        print("Nie realny skład !!!")
        break
    #zaokrąglanie#
    iwo=[c,h,n,o,s,a,w,cl,p]
    for i, x in enumerate(iwo): 
        iwo[i] = round(x, 3)
    paliwa.loc[nazwa]=iwo
    #Wpisy do bazy danych
    #bd=input("Dodać paliwo do bazy danych ? (t/n):") 
    #if bd == 't' :
    #   paliwa.to_csv('paliwa.csv')
    b = input('Dodać inne paliwo? (t/n): ')
        

#Obliczanie wartosci opalowej
wzory=["Bossela ","Dulonga ", "Mahlera ", "KTiUZO"]
print(wzory)
ktory=input("Wg. Jakiego wzoru obliczać podaj numer ? ") 
ktory=int(ktory)
if ktory == 1 :
    paliwa["Wartość opałowa wg. wzoru Bossela, Guanolda "]=(34.8*paliwa["Wegiel"]+93.9*paliwa["Wodor"]+10.5*paliwa["Siarka"]+6.3*paliwa["Azot"]-10.8*paliwa["Tlen"])*1000
elif ktory == 2 :
    paliwa["Wartość opałowa wg. wzoru Dulonga "]=33900*paliwa["Wegiel"]+121400*(paliwa["Wodor"]-(paliwa["Tlen"]/8))+10500*paliwa["Siarka"]+2500*paliwa["Woda"]
elif ktory == 3 :
    paliwa["Wartość opałowa wg. wzoru Mahlera "]=34080*paliwa["Wegiel"]+144450*paliwa["Wodor"]-12560*(paliwa["Tlen"]-paliwa["Azot"])-2500*(9*h+paliwa["Woda"])
elif ktory == 4 :    
    paliwa["Wartość opałowa wg. wzoru KTiUZO "]=33900*paliwa["Wegiel"]+10500*paliwa["Siarka"]+121400*(paliwa["Wodor"]-paliwa["Chlor"])-((paliwa["Tlen"])/8)-2500*paliwa["Woda"]

    
#Wyniki do Excela 
b=input("Zapisać wyniki w arkuszu kalkulacyjnym ? (t/n):") 
if b == 't' :
    writer = pd.ExcelWriter('Paliwa.xlsx')
    paliwa.to_excel(writer,'Baza paliw')
    writer.save()
else :
    print(paliwa)
    input("Kliknij, aby zakończyć.")