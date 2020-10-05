# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
n = int(input("Введите целое число от 0 до 99: "))
if (n >= 10 and n <= 19):
    
    if n == 11:
        print("одиннадцать");
    if n == 12:
        print("двенадцать");
    if n == 13:
        print("тринадцать");
    if n == 14:
        print("четрынадцать");
    if n == 15:
        print("пятнадцать");
    if n == 16:
        print("шестнадцать");
    if n == 17:
        print("семндацать");
    if n == 18:
        print("восемнадцать");
    if n == 19:
        print("девятнадцать");
    if n == 10:
        print("десять");
a = int( n / 10);    
b = n % 10;        
if a == 2: 
    print ("двадцать", end =" ");
if a == 3: 
    print ("тридцать", end =" ");
if a == 4: 
    print ("сорок", end =" ");
if a == 5: 
    print ("пятьдесят", end =" ");  
if a == 6: 
    print ("шестьдесят", end =" ");
if a == 7: 
    print ("семьдесят", end =" ");
if a == 8: 
    print ("восемьдесят", end =" ");
if a == 9: 
    print ("девяноста", end =" ");
if a == 0: 
    print ("ноль");
if b == 1: 
    print ("один");
if b == 2: 
    print ("два");
if b == 3: 
    print ("три");
if b == 4: 
    print ("четыре");
if b == 5: 
    print ("пять");
if b == 6: 
    print ("шесть");
if b == 7: 
    print ("семь");
if b == 8: 
    print ("восемь");
if b == 9: 
    print ("девять");